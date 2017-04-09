class EmptyTree:
    def empty(self):
        return True                                                              
                                                                                 
    def __len__(self):
        return 0                                                                 
                                                                                  
class BST:                                                                       
    def __init__(self, value):                                
        self._value = value                                                       
        self._left = EmptyTree()                                                 
        self._right = EmptyTree()                                                 
                                                                                  
    def empty(self):                                                             
        return False                                                             
                                                                                  
    def insert(self, value):                                                     
        if value > self._value:
            if self._right.empty():
                self._right = BST(value)
            else:
                self._right.insert(value)
        elif value < self._value:
            if self._left.empty():
                self._left = BST(value)
            else:
                self._left.insert(value)                                              
            return                                                                
        else:                                 
            raise ValueError(str(value))

    def __len__(self):
        return 1 + len(self._right) + len(self._left)


