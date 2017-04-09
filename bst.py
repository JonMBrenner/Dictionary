class EmptyTree:
    def empty(self):
        return True

    def __len__(self):
        return 0

    def lookup(self, key):
        return False

class BST:
    def __init__(self, key, value):
        self._key = key
        self._value = value
        self._left = EmptyTree()
        self._right = EmptyTree()

    def empty(self):
        return False

    def insert(self, key, value):
        if key > self._key:
            if self._right.empty():
                self._right = BST(key, value)
            else:
                self._right.insert(key, value)
        elif key < self._key:
            if self._left.empty():
                self._left = BST(key, value)
            else:
                self._left.insert(key, value)
            return
        else:
            raise keyError(str(key))

    def __len__(self):
        return 1 + len(self._right) + len(self._left)

    def lookup(self, key):
        return (self._key == key or self._right.lookup(key)
                or self._left.lookup(key))

