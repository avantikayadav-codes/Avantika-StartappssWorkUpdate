"""
q8 Why does __iter__() usually return self in most custom iterator implementations?

-Because the object itself is acting as the iterator, so __iter__() returns the same object (self) that already implements __next__().
"""