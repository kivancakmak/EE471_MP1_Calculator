from custom_classes import Calculator

calc = Calculator()
print(calc._current_val)  # Accessing the private attribute (not recommended)

#(10 + 5) * 2 / 3
result = calc.divide(calc.multiply(calc.add(10,5),2),3)

print(result)
