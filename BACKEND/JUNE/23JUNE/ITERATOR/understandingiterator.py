"""
iter()  -> creates an iterator
it      -> iterator object
next()  -> asks iterator for next value

interable- collections like list tuple dict in which we can traverse, and use loop
interator- it is the object that traverse in the iterables, it-it is iterator

Iterator
What:
An iterator is an object that provides values one-by-one and remembers its current position.
Why:
It allows data to be processed lazily (one item at a time) instead of requiring all data to be loaded or handled at once, which can save memory for large datasets.

Generator
What:
A generator is a special function that automatically creates an iterator using yield.
Why:
It was introduced to make iterator creation much simpler and more readable, without manually writing __iter__() and __next__().

Real Syntax
Create Iterator
iterator = iter(iterable)

Example:
nums = [10,20,30]
it = iter(nums)

Get Next Value
next(iterator)

Example:
print(next(it))
print(next(it))
print(next(it))

Output:
10
20
30

Internally For Loop
Tum likhti ho:
for x in nums:
    print(x)
Python internally:
it = iter(nums)
while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        break

Ye interview favorite question hai 🔥


The class in iterator is used to make the custome iterator
class MyIterator:
    def __iter__(self):
        return self
    def __next__(self):
        return value
"""