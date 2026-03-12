from unittest import result


class Calculator:
    def __init__(self):
        self._current_val = 0 # Private attribute to store the current value
        
    def multiply(self, x, y):
        result = x * y
        self._current_val = result
        return result
        
    def add(self, x, y):
        result = x + y
        self._current_val = result # update_current_val 
        return result

    def subtract(self, x, y):
        result = x - y
        self._current_val = result
        return result

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Division by zero is not allowed!") # Constraint
        result = x / y
        self._current_val = result
        return result

