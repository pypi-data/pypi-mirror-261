import pathlib
import sqlite3
import os
import sh
import shortuuid
import urllib.parse
import json
import re
import tempfile
import collections


class SHADB:

  def __init__(self, git_path, init=True, id_key='id', type_key='type'):
    self._type_key = type_key
    self._id_key = id_key
    self._git_path = pathlib.Path(git_path).absolute()
    self._sqlite_path = self._git_path / 'idx.db'
    self._git = sh.git.bake(C=self._git_path)
    try:
      self._git.status()
    except sh.ErrorReturnCode_128 as e:
      if init:
        self._git.init()
        with open(self._git_path/'.gitignore', 'w') as f:
          f.write('idx.db\n')
        self._git.add('.gitignore')
        self._git.commit('.gitignore', m='added .gitignore')
        
      else: raise e
    if not hasattr(self, 'idx'):
      self.idx = Indices()
    self._init_db()
  
  def _init_db(self):
    with self._connect() as conn:
      cur = conn.cursor()
      cur.execute("CREATE TABLE IF NOT EXISTS indexed_state (name TEXT NOT NULL PRIMARY KEY, last_hash TEXT NOT NULL);")
  
  def _update_git_path(self, git_path, init=True):
    self.__init__(git_path, init=init)
    for idx in self.idx.__dict__.values():
      idx._init_db()

  def add_index(self, name, f, **kwargs):
    if hasattr(self.idx, name): raise Exception('conflicting name')
    index = Index(self, name, f, **kwargs)
    index.update()
    setattr(self.idx, name, index)

  def _connect(self):
    conn = sqlite3.connect(self._sqlite_path)
    #conn.set_trace_callback(print)
    return conn
    

  def status(self):
    changes = self._git.status('--porcelain')
    changes = changes.strip()
    changes = changes.splitlines()
    changes = [s.split() for s in changes if s]
    return changes
  
  def log(self, *fns):
    changes = []
    change = None
    with tempfile.NamedTemporaryFile() as tf:
      print('tf.name', tf.name)
      self._git.log(*fns, output=tf.name)
      with open(tf.name,'r') as f:
        for line in f.readlines():
          if line.startswith(' '): continue
          line = line.strip()
          if line.startswith('commit'):
            change = {'commit':line.split()[1]}
            changes.append(change)
          if line.startswith('Author:'):
            author = line.split()[1:]
            change['author'] = {
              'name': ' '.join(author[:-1]),
              'email': author[-1],
            }
          if line.startswith('Date:'):
            _, date = line.split(maxsplit=1)
            change['date'] = date
    print('changes', changes)
    return changes
  
  def store(self, *objects, commit=False):
    fns = []
    for o in objects:
      id = o.get(self._id_key)
      if not id:
        o[self._id_key] = id = shortuuid.uuid()
      sig = urllib.parse.quote(id)
      resource_type = o.get(self._type_key, 'obj')
      dn = os.path.join(resource_type, *sig[:4])
      if not os.path.isdir(os.path.join(self._git_path, dn)):
        os.makedirs(os.path.join(self._git_path, dn), exist_ok=True)
      fn = os.path.join(dn, f'{resource_type}-{sig}.json')
      self.dump(o, fn, _update_idx=False)
      fns.append(fn)
    if commit:
      self.commit(*fns)
    self.idx.update(also_fns=fns)
    return fns[0] if len(objects)==1 else fns
  
  def dump(self, o, fn, commit=False, _update_idx=True):
    exists = os.path.isfile(os.path.join(self._git_path, fn))
    with open(os.path.join(self._git_path, fn),'w') as f:
      json.dump(o, f, indent=2, sort_keys=True)
    #print('dumping', fn, o.json())
    if not exists:
      self._git.add(fn)
    if commit:
      self.commit(fn)
    elif _update_idx:
      self.idx.update(also_fns=[fn])

  def load(self, fn, ignore_fnf=False):
    try:
      with open(os.path.join(self._git_path, fn),'r') as f:
        return json.load(f)
    except FileNotFoundError as e:
      if ignore_fnf: return None
      else: raise e

  def delete(self, *fns, commit=False):
    self._git.rm('-f', *fns)
    if commit:
      self.commit(*fns)
    else:
      self.idx.update(also_fns=fns)

  def commit(self, *fns_or_objects, update=True):
    if not fns_or_objects: return
    fns = [s.__fhir_fn__ if hasattr(s,'__fhir_fn__') else s for s in fns_or_objects]
    self._git.commit(*fns, m='fhirdb')
    if update:
      self.idx.update()
  



class Index:

  def __init__(self, db, name, f, *, version=1, unique=False, index=True, index_None=False, fts=False):
    if name.startswith('_'): raise Exception('illegal name - starts with _')
    if not name.isidentifier(): raise Exception('illegal name - not a python identifier')
    if unique and fts: raise Exception('you cannot set unique=True and fts=True')
    self._tbl_name = 'idx_%s__v%i' % (name, version)
    self._name = name
    self._db = db
    self._f = f
    self._unique = unique
    self._index_None = index_None
    self._index = index
    self._fts = fts
    self._init_db()
  
  def _init_db(self):
    with self._connect() as conn:
      cur = conn.cursor()
      cur.execute('BEGIN;')
      if self._fts:
        cur.execute(f'''
          CREATE VIRTUAL TABLE IF NOT EXISTS "{self._tbl_name}" USING fts5(fn, value);
        ''')
      else:
        cur.execute(f'''
          CREATE TABLE IF NOT EXISTS "{self._tbl_name}"(
            value TEXT {"" if self._index_None else "NOT NULL"} {"PRIMARY KEY" if self._unique else ""},
            fn TEXT NOT NULL
          );
        ''')
      if self._index and not self._fts:
        if not self._unique:
          cur.execute(f'CREATE INDEX IF NOT EXISTS "{self._tbl_name}_value_idx" on "{self._tbl_name}" (value);')
        cur.execute(f'CREATE INDEX IF NOT EXISTS "{self._tbl_name}_fn_idx" on "{self._tbl_name}" (fn);')
      conn.commit()
      
  def _connect(self):
    return self._db._connect()
  
  def load(self, value):
    if self._unique:
      return self._db.load(self[value], ignore_fnf=True)
    else:
      return [self._db.load(fn) for fn in self[value]]
  
  def update(self, also_fns=[]):
    with self._connect() as conn:
      #conn.set_trace_callback(print)
      cur = conn.cursor()
      cur.execute('BEGIN')
      results = cur.execute('select last_hash from indexed_state where name=?', (self._tbl_name,)).fetchone()
      last_hash = results[0] if results else getattr(self._db._git, 'hash-object')('/dev/null', t='tree').strip()
      current_hash = getattr(self._db._git, 'rev-parse')('HEAD').strip()
      # git diff ignores --no-color so use ansi2txt
      with tempfile.NamedTemporaryFile() as tf:
        self._db._git.diff('--name-status', last_hash, 'HEAD', output=tf.name)
        with open(tf.name,'r') as f:
          changes = f.read().strip()
      changes = changes.splitlines()
      changes = [s.split() for s in changes if s]
      for fn in also_fns:
        changes.append(('M',fn))
      for status, fn, *other in changes:
        #print('status, fn', status, fn, other)
        if not fn.endswith('.json'): continue
        # https://git-scm.com/docs/git-diff#:~:text=Possible%20status%20letters%20are%3A
        if status=='R100':
          cur.execute(f'update "{self._tbl_name}" set fn=? where fn=?', (other[0], fn))
        if status in 'D' or (status=='M' and not self._unique) or (status.startswith('R') and status!='R100'):
          cur.execute(f'delete from "{self._tbl_name}" where fn=?', (fn,))
        if status in 'ACM' or (status.startswith('R') and status!='R100'):
          if status.startswith('R'):
            fn = other[0]
          try:
            o = self._db.load(fn)
          except FileNotFoundError as e:
            print('FileNotFound:', fn)
            continue
          value = self._f(o)
          if value is not None or self._index_None:
            values = value if isinstance(value, list) else [value]
            for value in values:
              normalized_value = self._normalize(value)
              try:
                cur.execute(f'{"replace" if self._unique else "insert"} into "{self._tbl_name}" (fn,value) values (?,?)', (fn, normalized_value))
              except sqlite3.InterfaceError as e:
                print('failed to set', value, 'for', fn)
                raise e
      cur.execute('replace into indexed_state values (?,?)', (self._tbl_name,current_hash))
      conn.commit()
  
  def all(self):
    with self._connect() as conn:
      cur = conn.cursor()
      q = cur.execute(f'select fn from "{self._tbl_name}"')
      results = q.fetchall()
      return [r[0] for r in results]
  
  def _normalize(self, value):
    if not isinstance(value,str):
      value = json.dumps(value, sort_keys=True)
    return value
      
  def __getitem__(self, value):
    if self._fts:
      cmd_words = set('and or not'.split())
      split_respect_quotes = re.findall(r'(?:[^\s,"]|"(?:\\.|[^"])*")+', value)
      split_respect_quotes = [s.upper() if s.lower() in cmd_words else s for s in split_respect_quotes]
      split_respect_quotes = ['"%s"'%s.strip('"') if re.search('[-/]',s) else s for s in split_respect_quotes]
      value = ' '.join(split_respect_quotes)
      print('value', value)
    with self._connect() as conn:
      cur = conn.cursor()
      limit = ' limit 1' if self._unique else ''
      if value is None:
        q = cur.execute(f'select fn from "{self._tbl_name}" where value is null'+limit)
      else:
        normalized_value = self._normalize(value)
        cmp_o = 'like' if '%' in normalized_value else '='
        if self._fts: cmp_o = 'MATCH'
        q = cur.execute(f'select fn from "{self._tbl_name}" where value {cmp_o} ?'+limit, (normalized_value,))
      if self._unique:
        result = [r[0] for r in q.fetchall()]
        return result[0] if result else None
      else:
        results = q.fetchall()
        return list(dict.fromkeys([r[0] for r in results]))

  def values(self, like=None):
    with self._connect() as conn:
      cur = conn.cursor()
      if like:
        q = cur.execute(f'select distinct value from "{self._tbl_name}" where value like ?', (like,))
      else:
        q = cur.execute(f'select distinct value from "{self._tbl_name}"')
      results = q.fetchall()
      return [r[0] for r in results]
  
  def items(self):
    ret = collections.defaultdict(list)
    with self._connect() as conn:
      cur = conn.cursor()
      q = cur.execute(f'select value, fn from "{self._tbl_name}"')
      for value, fn in q.fetchall():
        ret[value].append(fn)
    if self._unique:
      ret = {k:(v[0] if v else None) for k,v in ret.items()}
    return ret
  
  def value_counts(self):
    with self._connect() as conn:
      cur = conn.cursor()
      q = cur.execute(f'select value, count(1) from "{self._tbl_name}" group by value')
      results = q.fetchall()
      return {r[0]:r[1] for r in results}
  
  def __contains__(self, value):
    return bool(self.__getitem__(value))
     
      
    
    

class Indices:

  def update(self, **kwargs):
    for idx in self.__dict__.values():
      idx.update(**kwargs)




