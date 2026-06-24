"""
11. What is the difference between an iterable and an iterator?

Answer: An iterable is a collection of data that can be looped over (e.g., list, tuple, string), whereas an iterator is an object that returns elements one by one and keeps track of its current position.


12. Can a single iterator object be reused after it is exhausted? Why or why not?

Answer: No. Once an iterator is exhausted, it raises StopIteration and cannot be reset. A new iterator must be created from the iterable.


13. How does a for loop internally work with iterators?

Answer: A for loop first calls iter() on the iterable to get an iterator, then repeatedly calls next() until StopIteration is raised.


14. What will happen if __next__() never raises StopIteration?

Answer: The iterator becomes infinite, and a for loop using it will continue forever unless manually stopped.


15. Which module in Python provides built-in infinite iterators? Name at least three such functions.

Answer: The itertools module provides built-in infinite iterators. Examples are:

itertools.count()
itertools.cycle()
itertools.repeat()
"""