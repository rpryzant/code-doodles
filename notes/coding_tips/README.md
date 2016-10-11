# Coding Tips

10/11/16

These are a collection of odds-and-ends tips and tricks I've written to myself over the last few months. 
Right now they're mosly python-specific.
This is very disorganized and gross, but I just wanted a place to brain dump all of this.

* To avoid cycles in DFS, mark as visited 
* To avoid cycles in BFS, mark as visited **before each enqueueing** 
* To use queues in Python:  
``from Queue import Queue``  
``q.get()``/``q.add()``
* Add together list lengths (??)
* Think in terms of current, previous
* Be careful with ``is X``. It tests for
  * False
  * 0
  * None  
  The wrong thing might slip in
* For OOD problems, have a ``UserManager`` class
* To copy a 2d array, copy **each sublist**: ``[x[:] for x in A]``
* Only copy passed objects to recursive methods
* If you want a mutable literal (e.g. int) in Python, make it a 1-element list: ``[1]`` and pass that around to methods and stuff
* Conditional expressions: ``y = x+ if c else x-``
* Always check for bad input!! E.g. what if empty input string??
* **You can't return or assign statements!!** e.g. ``return a += 3`` => NO
* Be careful about going out of bounds
* Thing of problem in terms of what properties will be true in the postcondition
* Be careful about changing the state of an object (e.g. matrix) as you're operating on it - don't want to fill a row with zeros if you expect to be visiting non-zero elements in those spots in the future
* Ask yourself what would be true **if**... (e.g. if there was no solution)
* When brainstorming
  * brute force
  * sorted? n log n?
  * data structure? (hashmap, prefix tree, heap, stack, queue, etc)
  * multiple passes?
* Ask if sign should be preserved for bit problems
* ``A[start (inclusive) : end (exclusive) : step]``
* **Logical right** fills sign bit with zero. **arithmatic right** fills with 1 if negative num
* SUM (x - i) = X (X + 1) / 2
  * Intuition: pair up elements. You'll get x/2 pairs, each of which sum to x + 1
* Quadratic formula: -b +/- sqrt(b^2 - 4ac) / 2a
* Load balencing for minimization problems, e.g. in egg drop problem: distribute droppings evenly! Make each egg drop count as much as possible
* Ask questions! Be careful!
* Guard against OOB exceptions with checks at top of loops
* ``insert(index, val)`` is a **statement**. Inserts **before** given index
* Copy arrays before recursion!!!
* Consider group/merging cases by returned value
* **PYTHON INHERITANCE**
  * ``class classname (superclass):``
  * ``super().__init__()``
  * ``@staticmethod``
  * ``def f(*x)`` => variable num params, passed as tuple of unknown length
* hashtables are your ~friend~
* use epsilon for floating point calculations
* consider tries!
* Sometimes it may be helpful to think of string problems in terms of substring chunks!
* ``id(x)`` returns unique int for obj x
* consider modifying given structures (e.g. chopping ll after you know its length). Ask if this is ok!
* X^(power of 2) = X^(n/2) * X^(n/2)
* ``"a" * 2`` => ``"aa"``
* ``"a" + "a"`` => ``"aa"``
* **TUPLES ARE IMMUTABLE** 
* Count num bits wit hthis cool trick!
  * ``c = c & (c - 1)`` (clears least significant bit)
* don't name variables the same as builtin stuff
* ``sorted(l, key=lambda....)`` => not in place, statement
* ``l.sort(key=lambda...)`` => in place, not statement
* Think in terms of what local properties must be true - sometimes all you have to do is local operations to get those properties valid for the global solution to hold
* Be wary of **integer overflow**!!
* Negative => 1 is in sign bit
* VERIFY INPUTS!!
* SUM 2^i = 2^(n + 1) - 1
  * intuition: each summand gets one bit
* If not next() => StopIteration
  * throw StopIteration if you want early stopping in generator function
* ``try: ------  except: --------``
* ``map()`` is an expression (produces something)
* good ll strategy: fast runner (2 steps), slow runner (1 step)
* It's ok to use timestamps: ``time.time()``
* can't pop from empty lists
* consider adding data (e.g. size) to strucures/nodes
* ``(a or b)[1]`` is valid
* little endian: >        (size refers to whats on the RIGHT)
* big endian: <           (size refers to whats on the RIGHT)
* ask if should be cleaning/sanatizing input
* Sometimes its best not to work corner cases into main logic. Test and account for seperatly
* Z = integers. N = natural nums
* ``sorted()`` => increasing order
* HEAP CHILDREN: 2i + 1, 2i + 2
* HEAP PARENT: (i - 1) / 2
* ``"s".join()`` only places s **between** strings
* Do length gaurding conditional first thing in loops
* DFS can be applied anytime you want to search a space  
``for -------:``  
``sofar.append(---)``  
``dfs recurse...``  
``sofar.pop()``  
* ask if called once or many times
* consider mapping states (e.g. boards) to ints
* don't be afraid to scrap your work and start in a new direction if its not going anywhere!
* tuples are immutable
* check if ctr > max after loops
* mention python 2 if casting to float (py3.+ does it automatically)
* don't start coding until you know your algorithm!
* 3 way conditional expression: ``x = a if --- else b if --- else c``
* clean dups from list: ``list(set(l))``
* To compare dicts: ``len(set(a.items()) ^ set(b.items())) == 0``
  * can use bitwise ops on sets
* Consider lazy eval as potential speedup!
* be wary of changing list len if you pop/add as you're looping 
* ``d.items()``
* ``re.split()``
* ``getattr(n, 'next', None)``
* Check for dups: ``len(l) != len(set(l))``
* ``random.sample([], #)``
* ``random.choice([])``
* take min/max of tuple list for argmax
* think about whether **argument order** matters
* when in doubt, escape with backlash in regex!
* ask if input is sorted!! Always consider sorting!!
* For bst problems consider inorder/preorder/postorder traversal
* ``sys.setrecursionlimit(X)`` fun little thing
* ``_, a, b = (throwaway, keep, keep)``

