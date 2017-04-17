# Dictionary

Implementation of a dictionary in Python 3 as a Binary Search Tree, which functions similarly to the builtin dict. The initial 
naive implementation stored the key-value pairs as a list of two-element lists. To improve lookup and insertion time from O(n) 
to O(log(n)), I created a BST class with recursive structure and methods due the natural recursion of a binary search tree. I 
then rewrote each function in the dictionary to use BST methods. The entire project was tested with the python unittest module.
