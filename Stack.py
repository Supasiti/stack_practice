# Python Version 3.9.1
# Create Stack with the following methods:
#  - Clear    : - 
#  - Contains : - 
#  - Peek     : -
#  - Pop      : - 
#  - Push     : -
#  - iterator : -

class Stack:

    def __init__(self, data: list = None):
        self.__iter_index = -1
        self.__objects = [] if data is None else data
    
    def __len__(self):
        return len(self.__objects)

    def __contains__(self, obj):
        return True if self.__objects.count(obj) >0 else False

    def __iter__(self):
        self.__iter_index = self.__len__() - 1
        return self

    def __next__(self):
        index = self.__iter_index
        if index >= 0:
            self.__iter_index -= 1
            return self.__objects[index]
        else:
            raise StopIteration

    def __iadd__(self, other):
        self.push(other)
        return self

    def push(self, obj):
        self.__objects.append(obj)

    def peek(self):
        return self.__objects[-1] if self.__len__() > 0 else None 

    def pop(self):
        if self.__len__() > 0:
            return self.__objects.pop(-1)
        else:
            raise IndexError('pop from empty stack')

    def clear(self):
        self.__objects.clear()