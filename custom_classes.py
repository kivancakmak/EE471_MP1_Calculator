class Calculator:
    def __init__(self):
        self._current_val = 0 # Private attribute to store the current value
        
    def add(self, x, y):
    result = x + y
    self._current_val = result # update_current_val 
    return result

    def subtract(self, x, y):
    result = x - y
    self._current_val = result
    return result

 