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
        self.__index = -1
        self.__objects = []
        self.init_stack_data(data)

    def init_stack_data(self, data:list = None):
        if data is not None:
            self.__objects = data       
            self.__index = len(data) - 1
    
    def __len__(self):
        return len(self.__objects)

    def __contains__(self, obj):
        return True if self.__objects.count(obj) >0 else False

    def __iter__(self):
        self.__iter_index = self.__index
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
        self.__index += 1

    def peek(self):
        index = self.__index
        return self.__objects[index] if index >= 0 else None 

    def pop(self):
        if self.__index >= 0:
            result = self.__objects.pop(self.__index)
            self.__index -= 1
            return result
        else:
            raise IndexError('pop from empty stack')

    def clear(self):
        self.__objects.clear()
        self.__index = -1