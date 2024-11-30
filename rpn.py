def math_to_rpn(operation):
    """
    Convert a math operation to a reverse polish notation operation.
    This function works only with the following operators: +, -, *, /.
    This function allows multiple digits numbers.
    
    :param operation: The math operation to convert.
    :type operation: str
    :return: Reverse Polish Notation representation of the input operation
    :rtype: str
    """
    # Remove all spaces from the operation
    operation = operation.replace(' ', '')
    
    # Define operator precedence
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    
    # Stacks for operators and output
    operator_stack = []
    output_queue = []
    
    # Flag and temporary storage for multi-digit numbers
    current_number = ''
    
    # Process each character in the operation
    i = 0
    while i < len(operation):
        char = operation[i]
        
        # Handle multi-digit numbers
        if char.isdigit():
            current_number += char
            
            # Look ahead to check if next character is also a digit
            if i + 1 < len(operation) and operation[i + 1].isdigit():
                i += 1
                continue
            
            # Add complete number to output
            if current_number:
                output_queue.append(current_number)
                current_number = ''
        
        # Handle parentheses
        elif char == '(':
            operator_stack.append(char)
        
        elif char == ')':
            # Pop operators until matching opening parenthesis
            while operator_stack and operator_stack[-1] != '(':
                output_queue.append(operator_stack.pop())
            
            # Remove the opening parenthesis
            if operator_stack and operator_stack[-1] == '(':
                operator_stack.pop()
        
        # Handle operators
        elif char in '+-*/':
            # Compare precedence and handle operator stacking
            while (operator_stack and 
                   operator_stack[-1] != '(' and 
                   precedence.get(operator_stack[-1], 0) >= precedence.get(char, 0)):
                output_queue.append(operator_stack.pop())
            
            operator_stack.append(char)
        
        i += 1
    
    # Add any remaining operators
    while operator_stack:
        output_queue.append(operator_stack.pop())
    
    # Convert output to string
    return ''.join(output_queue)

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