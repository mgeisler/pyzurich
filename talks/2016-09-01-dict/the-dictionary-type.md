name: inverse
layout: true
class: center, middle, inverse

---

# The Python Dictionary

Martin Geisler  
martin@geisler.net

2016-09-01 — PyZurich

.small[https://github.com/mgeisler/pyzurich/]


---

layout: false

# The Mighty Dictionary

* This talk borrows the MIT licensed slides and material from Brandon
  Craig Rhodes, PyCon 2010 Atlanta

* https://github.com/brandon-rhodes/pycon2010-mighty-dictionary

---

# Agenda

* Looking things up

* Dictionaries in Python

* Hashing and collisions

* Real-life performance

* Conclusion

---

# Martin Geisler

* Backend Engineer at Centralway Numbrs

* Helps organize Python meetups

---

template: inverse
class: bgimg
background-image: url(ram.jpg)

# Random Access Memory

---

# RAM: Random Access Memory

* Vast array of memory cells

* Addressed using integers

* Accessing any location takes the same time

---

# The List

* RAM is the fundamental constant-time storage operation

* The perfect building block for a Python `list`!

```python
timeit('lst[0]', 'lst = range(10000)')
# --> 0.053692102432250977
#     ~50 ns per getitem

timeit('lst[9000]', 'lst = range(10000)')
# --> 0.051460027694702148
#     ~50 ns per getitem

```

---

# The Dictionary

* Uses *keys* instead of *integers*

* We still want constant time access

* Keys can be almost anything:

```python
>>> d = {
...    'Brandon': 35,
...    3.1415: 'pi',
...    'flickr.com': '68.142.214.24',
...    (2, 6, 4): 'Python version',
...    }

```

---

# Implementing a Dictionary

> How can we turn  
> the **keys** dictionaries use  
> into **indexes** that reach memory quickly?  

---

# The Three Rules

1. **A dictionary is really a list**

---

# Empty Dictionary

```python
>>> # An empty dictionary is an 8-element list!
>>> d = {}

```

![](figures/insert0.png)

---

# Empty Dictionary

```python
>>> # This “list” of “items” is managed
>>> # as a “hash table” containing “slots”

```

![](figures/insert0.png)

---

# The Three Rules

1. A dictionary is really a list
2. **Keys are *hashed* to produce indexes**

---

template: inverse
class: bgimg
background-image: url(roesti.jpg)


# Hashing and Collisions

.credit[CC BY-SA 3.0: Benutzer:Mussklprozz, https://commons.wikimedia.org/wiki/File:Roesti.jpg]

---

# Hashing

* Turns almost anything into an integer

* Python exposes its hashing through the `hash()` builtin

```python
>>> for key in 'Monty', 3.1415, (2, 6, 4):
...     print bits(hash(key)), key
01100111100110010110110011111110 Monty
01101010101011010000100100000010 3.1415
01000111010110111010001100110111 (2, 6, 4)

```

---

# Hashing

> Quite similar values often have  
> very different hashes

```python
>>> k1 = bits(hash('Monty'))
>>> k2 = bits(hash('Money'))
>>> diff = ('^ '[a==b] for a,b in zip(k1, k2))
>>> print k1; print k2; print ''.join(diff)
01100111100110010110110011111110
01100110101101001000101011101001
       ^  ^ ^^ ^^^^  ^^    ^ ^^^

```

---

# Hashing

> Hashes look crazy, but the **same** value  
> always returns the **same** hash!

```python
>>> for key in 3.1415, 3.1415, 3.1415:
...     print bits(hash(key)), key
01101010101011010000100100000010 3.1415
01101010101011010000100100000010 3.1415
01101010101011010000100100000010 3.1415

```

---

# Keys and Indexes

> To build an index, Python uses  
> the bottom **n** bits of the hash

```python
>>> b = bits(hash('ftp'))
print b
11010010011111111001001010100001
>>> print b[-3:]  # last 3 bits = 8 combinations
001

```

---

# Insertion

```python
>>> d['ftp'] = 21

>>> print bits(hash('ftp'))[-3:]
001

```

![](figures/insert1a.png)

---

# Insertion

```python
>>> d['ftp'] = 21

>>> print bits(hash('ftp'))[-3:]
001

```

![](figures/insert1b.png)

---

# Insertion

```python
>>> d['ssh'] = 22

>>> print bits(hash('ssh'))[-3:]
101

```

![](figures/insert2a.png)

---

# Insertion

```python
>>> d['ssh'] = 22

>>> print bits(hash('ssh'))[-3:]
101

```

![](figures/insert2b.png)

---

# Insertion

```python
>>> d['smtp'] = 25

>>> print bits(hash('smtp'))[-3:]
100

```

![](figures/insert3a.png)

---

# Insertion

```python
>>> d['smtp'] = 25

>>> print bits(hash('smtp'))[-3:]
100

```

![](figures/insert3b.png)

---

# Insertion

```python
>>> d['time'] = 37

>>> print bits(hash('time'))[-3:]
111

```

![](figures/insert4a.png)

---

# Insertion

```python
>>> d['time'] = 37

>>> print bits(hash('time'))[-3:]
111

```

![](figures/insert4b.png)

---

# Insertion

```python
>>> d['www'] = 80

>>> print bits(hash('www'))[-3:]
010

```

![](figures/insert5a.png)

---

# Insertion

```python
>>> d['www'] = 80

>>> print bits(hash('www'))[-3:]
010

```

![](figures/insert5b.png)

---

# Insertion

```python
# final dictionary
d = {'ftp': 21, 'ssh': 22,
     'smtp': 25, 'time': 37,
     'www': 80}
```

![](figures/insert6.png)

---

# Lookup: Same 3 Steps

* Compute the hash

* Truncate it

* Look in that slot

---

```python
>>> print d['smtp']
25

>>> print bits(hash('smtp'))[-3:]
100

```

![](figures/lookup1a.png)

---

# Consequence #1


> Dictionaries tend to return their  
> contents in a crazy order

---

# Iteration

```python
>>> # Different than our insertion order:
>>> print d
{'ftp': 21, 'www': 80, 'smtp': 25, 'ssh': 22,
 'time': 37}
>>> # But same order as in the hash table!

```

![](figures/insert6.png)

---

# Iteration

```python
>>> # keys and values also in table order
>>> d.keys()
['ftp', 'www', 'smtp', 'ssh', 'time']
>>> d.values()
[21, 80, 25, 22, 37]

```

![](figures/insert6.png)

---

# The Three Rules


1. A dictionary is really a list
2. Keys are *hashed* to produce indexes
3. **If at first you don't succeed, try, try again**

---

# Collision

> When two keys in a dictionary  
> want the same slot

* Python uses *open addressing* to resolve collisions

---

# Collisions

```python
>>> # start over with a new dictionary
>>> d = {}

```

![](figures/insert0.png)

---

# Collisions

```python
>>> # first item inserts fine
>>> d['smtp'] = 21

```

![](figures/collide1a.png)

---

# Collisions

```python
>>> # first item inserts fine
>>> d['smtp'] = 21

```

![](figures/collide1b.png)

---

# Collisions

```python
>>> # second item collides!
>>> d['dict'] = 2628

```

![](figures/collide2a.png)

---

# Collisions

```python
>>> # second item collides!
>>> d['dict'] = 2628

```

![](figures/collide2b.png)

---

# Collisions

```python
>>> # third item also finds empty slot
>>> d['svn'] = 3690

```

![](figures/collide3a.png)

---

# Collisions

```python
>>> # third item also finds empty slot
>>> d['svn'] = 3690

```

![](figures/collide3b.png)

---

# Collisions

```python
>>> # fourth item has multiple collisions
>>> d['ircd'] = 6667

```

![](figures/collide4a.png)

---

# Collisions

```python
>>> # fourth item has multiple collisions
>>> d['ircd'] = 6667

```

![](figures/collide4b.png)

---

# Collisions

```python
>>> # fifth item collides, but less deeply
>>> d['zope'] = 9673

```

![](figures/collide5a.png)

---

# Collisions

```python
>>> # fifth item collides, but less deeply
>>> d['zope'] = 9673

```

![](figures/collide5b.png)

---

# Collisions

```python
# Only 2/5 of the keys in this dictionary
# can be found in the right slot

```

![](figures/collide5b.png)

---

# Collision Resolution

* Python uses open addressing

* Next index computed as `i = (5 * i + 1) mod 2**j`

* For a table with `2**j == 8`, the sequence is

```x
0 -> 1 -> 6 -> 7 -> 4 -> 5 -> 2 -> 3 -> 0 -> ...
```

* The high-order hash bits are included too:

```c
#define PERTURB_SHIFT 5

mask = size - 1 // for computing "mod 2**j"
for (perturb = hash; ; perturb >>= PERTURB_SHIFT {
    i = (i * 5 + perturb + 1) & mask
    // ...
}

```

---

# Collision Resolution

* Simple math, very fast to compute next probe index

* Sequential keys are handled well by recurrence relation

* Probe sequence eventually depends on every bit in hash

---

# Consequence #2

> Because collisions move keys  
> away from their natural hash values,  
> key order is quite sensitive  
> to dictionary history

---

# Key Order

```python
>>> d = {'smtp': 21, 'dict': 2628,
...   'svn': 3690, 'ircd': 6667, 'zope': 9673}
>>> d.keys()
['svn', 'dict', 'zope', 'smtp', 'ircd']

```

![](figures/keyorder1.png)

---

# Key Order

```python
>>> e = {'ircd': 6667, 'zope': 9673,
...   'smtp': 21, 'dict': 2628, 'svn': 3690}
>>> e.keys()
['ircd', 'zope', 'smtp', 'svn', 'dict']

```

![](figures/keyorder2.png)

---

# The Same Yet Different

* These two dictionaries are considered equal

* Different histories put their keys in a different order

```python
>>> d == e
True
>>> d.keys()
['svn', 'dict', 'zope', 'smtp', 'ircd']
>>> e.keys()
['ircd', 'zope', 'smtp', 'svn', 'dict']

```

---

# Consequence #3

> The lookup algorithm is actually  
> more complicated than  
> “hash, truncate, look”

---

# Consequence #3

> It's more like “until you find  
> an empty slot, keep looking,  
> it could be here somewhere!”

---

# Lookup

```python
>>> # Successful lookup, length 1
>>> # Compares HASHES then compares VALUES
>>> d['svn']
3690

```

![](figures/collide5d.png)

---

# Lookup

```python
>>> # Successful lookup, length 4
>>> d['ircd']
6667

```

![](figures/collide5e.png)

---

# Lookup

```python
>>> # Unsuccessful lookup, length 1
>>> d['nsca']
Traceback (most recent call last):
  ...
KeyError: 'nsca'

```

![](figures/collide5f.png)

---

# Lookup

```python
>>> # Unsuccessful lookup, length 4
>>> d['netstat']
Traceback (most recent call last):
  ...
KeyError: 'netstat'

```

![](figures/collide5g.png)

---

# Consequence #4


> Not all lookups are created equal.

--

> Some finish at their first slot  
> Some loop over several slots

---

# Consequence #5

> When deleting a key,  
> you need to leave  
> “dummy” keys

---

# Deletion

```python
del d['smtp']

# Can we simply make its slot empty?

```

![](figures/collide5c.png)

---

# Deletion

```python
del d['smtp']

# But what would happen to d['ircd']?

```

![](figures/collide5e.png)

---

# Deletion

> When a key is deleted,  
> its slot *cannot* simply  
> be marked as empty

--

> Otherwise, any keys  
> that collided with it would  
> now be impossible to find!

--

> So we create a dummy key instead

---

# Dummy Keys

```python
>>> # Creates a <dummy> slot that
>>> # can be re-used as storage

>>> del d['smtp']

```

![](figures/collide5h.png)

---

# Dummy Keys

```python
>>> # That way, we can still find d['ircd']

>>> d['ircd']
6667

```

![](figures/collide5i.png)

---

template: inverse

# Real-Life Collisions

---

# Dictionaries Refuse to Get Full

> To keep collisions rare,  
> dicts resize when only ⅔ full

--

> When < 50k entries, size ×4  
> When > 50k entries, size ×2

---

# Resizing

> Let's watch a dictionary in action  
> against words pulled from the standard  
> dictionary on a Ubuntu box

```python
>>> wordfile = open('/usr/share/dict/words')
>>> text = wordfile.read().decode('utf-8')
>>> words = [ w for w in text.split()
...     if w == w.lower() and len(w) < 6 ]
>>> words
[u'a', u'abaci', u'aback', u'abaft', u'abase',
 ..., u'zoom', u'zooms', u'zoos', ...]

```

---

# Resizing

```python
d = {}
# Again, an empty dict has 8 slots
# Let's start filling it with keys

```

![](figures/insert0.png)

---

# Resizing

```python
d = dict.fromkeys(words[:5])
# collision rate 40%
# but now 2/3 full — on verge of resizing!

```

![](figures/words5.png)

---

# Resizing

```python
d['abash'] = None
# Resizes ×4 to 32, collision rate drops to 0%

```

![](figures/words6.png)

---

# Resizing

```python
d = dict.fromkeys(words[:21])
# 2/3 full again — collision rate 29%

```

![](figures/words21.png)

---

# Resizing

```python
d['abode'] = None
# Resizes ×4 to 128, collision rate drops to 9%

```

![](figures/words22.png)

---

# Resizing

```python
d = dict.fromkeys(words[:85])
# 2/3 full again — collision rate 33%

```

![](figures/words85.png)

---

# Dictionary Life Cycle

* Gradually more crowded as keys are added

* Then suddenly less as dict resizes

* Collision rate is normally low

---

# Consequence #6

> Average dictionary  
> performance is excellent

---

# Real-Life Collisions

A dictionary of common words:

```python
>>> wfile = open('/usr/share/dict/words')
>>> words = wfile.read().split()[:1365]
>>> print words
['A', "A's", ..., "Backus's", 'Bacon', "Bacon's"]

```

We can examine which keys collide:

```python
>>> pmap = _dictinfo.probe_all_steps(words)

```

---

# Real-Life Collisions

Some keys are in the first slot probed:

```python
>>> pmap['Ajax']
[1330]
>>> pmap['Agamemnon']
[2020]

```

While some keys collided several times:

```python
>>> pmap['Aristarchus']  # requires 5 probes
[864, 1089, 801, 1108, 74]
>>> pmap['Baal']         # requires 16 probes!
[916, 1401, 250, 1359, 399, 1156, 1722, 420, 53,
 266, 1331, 512, 513, 518, 543, 668]

```

---

class: middle

![](figures/average_probes.png)

---

# Real-Life Collisions

Probes are very fast

```python
>>> setup = "d=dict.fromkeys(%r)" % words
>>> fast = timeit("d['Ajax']", setup)
>>> slow = timeit("d['Baal']", setup)
>>> '%.1f' % (slow/fast)
'1.7'

```

---

class: middle

![](figures/average_time.png)

---

# Consequence #7


> Because of resizing,  
> a dictionary can completely reorder  
> during an otherwise innocent insert

```python
>>> d = {'Double': 1, 'double': 2, 'toil': 3,
...      'and': 4, 'trouble': 5}
>>> d.keys()
['toil', 'Double', 'and', 'trouble', 'double']
>>> d['fire'] = 6
>>> d.keys()
['and', 'fire', 'Double', 'double', 'toil',
 'trouble']
```

---

# Consequence #8

> Because an insert can radically  
> reorder a dictionary, key insertion  
> is prohibited during iteration

```python
>>> d = {'Double': 1, 'double': 2, 'toil': 3,
...     'and': 4, 'trouble': 5}
>>> for key in d:
...     d['fire'] = 6
Traceback (most recent call last):
  ...
RuntimeError: dictionary changed size during
  iteration

```

---

# Take-away #1

> Hopefully “the rules”  
> now make a bit more sense  
> and seem less arbitrary

* Don't rely on order

* Don't insert while iterating

* Can't have mutable keys

---

# Take-away #2

> Dictionaries trade space for time

> If you need more space,  
> there are alternatives

* Tuples or namedtuples

* Give classes `__slots__`

---

# Take-away #3

> If your class needs its own `__hash__()`  
> method you now know how hashes  
> should behave

* Scatter bits like crazy

* Equal instances *must* have equal hashes

* Must also implement `__eq__()` method

* Make hash and equality quick!

---

# Hashing your own classes

* Start with `^` xor'ing the hashes of your instance variables

```python
 class Point(object):
     def __init__(self, x, y):
         self.x, self.y = x, y

     def __eq__(self, p):
         return self.x == p.x and self.y == p.y

     def __hash__(self):
         return hash(self.x) ^ hash(self.y)

```

---

# Take-away #4

> Equal values  
> should have equal hashes  
> regardless of their type!

```python
>>> hash(9)
9
>>> hash(9.0)
9
>>> hash(complex(9, 0))
9
```

---

# The End

![](figures/insert5b.png)

> May your hashes be unique,  
> Your hash tables never full,  
> And may your keys rarely collide

