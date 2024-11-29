def digits_calculation(operation: str) -> int:
    """
        Calcul the result of the reverse polish notation operation given in parameters.
        This funciton works only with digits and the following operators: +, -, *, /.
        
        :param operation: The reverse polish notation operation to calcul.
        :type operation: str
        :return Integer:
    """
    operation.replace(' ', '') # Remove spaces
    stack = []
    for c in operation:
        if not c in "+-*/":
            stack.append(int(c))
        else:
            b = stack.pop()
            a = stack.pop()
            stack.append(a + b if c == "+" else a - b if c == "-" else a * b if c == "*" else a // b)

    return stack[0]

assert digits_calculation("132-+") == 2
assert digits_calculation("82/") == 4
assert digits_calculation("99+") == 18
assert digits_calculation("123*+") == 7
print('Function digits_calculation() : all tests passed')

def numbers_calculation(operation: str) -> int:
    """
        Calcul the result of the reverse polish notation operation given in parameters.
        This funciton works only with the following operators: +, -, *, /.
        This function allows multiple digits numbers.
        
        :param operation: The reverse polish notation operation to calcul.
        :type operation: str
        :return Integer:
    """
    operation.replace(' ', '') # Remove spaces
    stack = [] 
    multiple_digits = False
    temp = ""
    for c in operation:
        if not c in "+-*/" and not c in "()" and not multiple_digits:
            stack.append(int(c))
        elif c == "(":
            multiple_digits = True
        elif c == ")":
            multiple_digits = False
            stack.append(int(temp))
            temp = ""
        elif multiple_digits:
            temp += c
        else:
            b = stack.pop()
            a = stack.pop()
            stack.append(a + b if c == "+" else a - b if c == "-" else a * b if c == "*" else a // b)

    return stack[0]
    

assert numbers_calculation("1(32)+") == 33
assert numbers_calculation("(24)8/") == 3
assert numbers_calculation("(10)5-") == 5
assert numbers_calculation("(120)(10)+") == 130
assert numbers_calculation("2(3)*") == 6
print('Function numbers_calculation() : all tests passed')

def float_calculation(operation: str) -> float:
    """
        Calcul the result of the reverse polish notation operation given in parameters.
        This funciton works only with the following operators: +, -, *, /.
        This function allows float numbers and return a float. 
        
        :param operation: The reverse polish notation operation to calcul.
        :type operation: str
        :return Float:
    """
    operation.replace(' ', '') # Remove spaces
    stack = []
    multiple_digits = False
    temp = ""
    for c in operation:
        if not c in "+-*/" and not c in "()" and not multiple_digits:
            stack.append(int(c))
        elif c == "(":
            multiple_digits = True
        elif c == ")":
            multiple_digits = False
            stack.append(float(temp))
            temp = ""
        elif multiple_digits:
            temp += c
        else:
            b = stack.pop()
            a = stack.pop()
            stack.append(a + b if c == "+" else a - b if c == "-" else a * b if c == "*" else a / b)

    return stack[0]

assert float_calculation("1(3.2)+") == 4.2
assert float_calculation("(2.4)8/") == 0.3
assert float_calculation("(1.0)5-") == -4.0
assert float_calculation("(12.0)(10)+") == 22.0
assert float_calculation("2(3.0)*") == 6.0
print('Function float_calculation() : all tests passed')