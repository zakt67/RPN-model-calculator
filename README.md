# Python reverse polish notation (RPN) operations interpreter
Scripts made with python. It allows you to interpret RPN operations and find the result.

## Authors
- [@zakt67](https://github.com/zakt67)

## Usage
Clone the project :
```bash
  git clone https://github.com/zakt67/ReversePolishNotation.git
```

Go to the project directory :
```bash
  cd ./ReversePolishNotation
```

Create a new python file and import *rpn.py* file :
```py
  from rpn import *
```

Call the funcitons as needed :
```python
  # Digits only usage
  digits_calculation("your operation goes here")

  # Basic numbers usage
  numbers_calculation("your operation goes here")

  # Floats support usage
  float_calculation("your operation goes here")
```

Format exemple : 
```py
  numbers_calculation("1245-*+") # It calculate : 1 + 2 * (4 - 5)
```

Add assertion tests (Optionnal) :
```python
    # Digits
  assert digits_calculation("132-+") == 2

  # Numbers
  assert numbers_calculation("(120)(10)*") == 1200

  # Floats
  assert float_calculation("(2.4)8/") == 0.3
```
