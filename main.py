from custom_classes import Calculator

calc = Calculator()
print(calc._current_val)  # Accessing the private attribute (not recommended)

# Ödevdeki örnek: (10 + 5) * 2 / 3
try:
    step1 = calc.add(10, 5)
    step2 = calc.multiply(step1, 2)
    result = calc.divide(step2, 3)
    print(f"Final Result: {result}")
except ValueError as e:
    print(e)