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