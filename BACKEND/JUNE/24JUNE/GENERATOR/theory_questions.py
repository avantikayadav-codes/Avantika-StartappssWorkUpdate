"""
Q1. What is a generator in Python and how is it different from a normal function?

Answer: A generator is a special function that uses yield to produce values one at a time. Unlike a normal function, it pauses after each yield and resumes from the same point on the next call.


Q2. What is the difference between yield and return?

Answer: return ends the function and returns a final value, whereas yield pauses the function, returns a value, and allows execution to continue from the same point later.


Q3. How does a generator save memory compared to lists?

Answer: A generator creates values only when needed (lazy evaluation), while a list stores all values in memory at once. Therefore, generators are more memory-efficient for large datasets.


Q4. What is generator iteration and how does it work internally?

Answer: Generator iteration works by repeatedly calling next() on the generator object. Each call resumes execution from the last yield, returns the next value, and pauses again until the function ends.


Q5. What are generator expressions and how are they different from list comprehensions?

Answer: Generator expressions use () and return a generator object that generates values lazily. List comprehensions use [] and create the entire list in memory immediately.


Q6. What is the purpose of the next() function in generators?

Answer: next() starts or resumes the generator, executes it until the next yield, returns that value, and pauses the generator again.


Q7. What happens when a generator function reaches the end?

Answer: When the generator function finishes execution, Python automatically raises the StopIteration exception to indicate that no more values are available.


Q8. What is the role of the StopIteration exception?

Answer: StopIteration signals that the generator or iterator has no more values to produce. It tells loops like for to stop iterating.


Q9. Can a generator be reused after it is exhausted? Why or why not?

Answer: No. Once a generator is exhausted, it raises StopIteration and cannot be reset. A new generator object must be created by calling the generator function again.


Q10. What are real-world use cases of generators in Python?

Answer: Generators are commonly used for reading large files, processing large datasets, streaming data, generating infinite sequences, handling log files, and working with APIs where data is produced one item at a time.
"""