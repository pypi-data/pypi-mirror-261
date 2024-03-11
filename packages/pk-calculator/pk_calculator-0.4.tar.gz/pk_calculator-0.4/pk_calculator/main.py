def add(x, y):
    print("Addition: ", x + y)
 
def subtract(x, y):
    print("Subtraction: ", x - y)

  
def multiply(x, y):
    print("Multiplication: ", x * y)

   
def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    print("Division: ", x / y)