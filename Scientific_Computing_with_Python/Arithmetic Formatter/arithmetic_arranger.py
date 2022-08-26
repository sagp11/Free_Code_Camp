
def arithmetic_arranger(problems, condition = False):
    # Handling ERROR for TOO MANY problems
    if len(problems) > 5:
        arranged_problems = 'Error: Too many problems.'
        return arranged_problems

    #Initiating strings for final result printing
    line_1 = ""
    line_2 = ""
    line_3 = ""
    line_4 = ""

    for problem in problems:
        problem = problem.strip()
        pieces = problem.split()

        # Handling ERROR for incorrect operators
        if pieces[1] != '+' and pieces[1] != '-':
            arranged_problems = 'Error: Operator must be \'+\' or \'-\'.'
            return arranged_problems
        try:
            # Handling ERROR for maximum value of digits
            if int(pieces[0]) > 9999 or int(pieces[2]) > 9999:
                arranged_problems = 'Error: Numbers cannot be more than four digits.'
                return arranged_problems
        except:
            # Handling ERROR for non-digit values of operands
            arranged_problems = 'Error: Numbers must only contain digits.'
            return arranged_problems

        temp_string = arrange_string(pieces[0], pieces[1], pieces[2], condition)

        # Appending the lines for final results
        line_1 = line_1 + '    ' + temp_string[0]
        line_2 = line_2 + '    ' + temp_string[1]
        line_3 = line_3 + '    ' + temp_string[2]
        if condition == True:
            line_4 = line_4 + '    ' + temp_string[3]

    if condition == True:
        arranged_problems = line_1[4:] +'\n' + line_2[4:] + '\n' + line_3[4:] + '\n' + line_4[4:]
        return arranged_problems
    else:
        arranged_problems = line_1[4:] +'\n' + line_2[4:] + '\n' + line_3[4:]
        return arranged_problems


def arrange_string(operand_1, operator, operand_2, condition):
    length = max(len(operand_1),len(operand_2))
    line_1 = operand_1.rjust(length + 2) #'+ 2' length for compensating the "operator" and a "space" in second line
    line_2 = operator + ' ' + operand_2.rjust(length)
    line_3 = '-'*(length + 2)
    if condition == True:
        if operator == '+':
            result = str(int(operand_1) + int(operand_2))
        elif operator == '-':
            result = str(int(operand_1) - int(operand_2))
        line_4 = result.rjust(length + 2)
        return [line_1, line_2, line_3, line_4]
    else:
        return [line_1, line_2, line_3]
