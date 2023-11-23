import itertools

def linebreak():
    """Prints a linebreak."""
    print('----------------------------------------')
    
def format_formula(formula):
    """
    Format the formula to be more readable.
    """
    if type(formula) is str:
        return formula
    elif type(formula) is bool:
        return formula
    elif formula == []:
        return None
    
    op = formula[0]

    if op in ['AND', 'OR']:
        return "(" + "".join(f"{op} {format_formula(var)} " for var in formula[1:])[len(op):] + ")"
    elif op == 'NOT':
        return f"({op} {format_formula(formula[1])})"
    elif op == 'IMPLIES':
        return f"({format_formula(formula[1])} {op} {format_formula(formula[2])})"
    elif op == 'EQUIV':
        return f"({format_formula(formula[1])} {op} {format_formula(formula[2])})"
    else:  # Variable
        return formula
    
def evaluate(formula, assignment):
    """
    Recursively evaluate the formula based on the assignment.
    """
    if type(formula) is str:
        try:
            return assignment.get(formula, False)
        except:
            return False
    elif type(formula) is bool:
        return formula
    elif formula == []:
        return None
    
    op = formula[0]

    if op in ['AND', 'OR']:
        results = [evaluate(sub_formula, assignment) for sub_formula in formula[1:]]
        return all(results) if op == 'AND' else any(results)
    elif op == 'NOT':
        return not evaluate(formula[1], assignment)
    elif op == 'IMPLIES':
        return not evaluate(formula[1], assignment) or evaluate(formula[2], assignment)
    elif op == 'EQUIV':
        return evaluate(formula[1], assignment) == evaluate(formula[2], assignment)
    else:  # Variable
        # in case a boolean value is passed in
        if assignment in [True, False]:
            return assignment
        return assignment.get(formula, False)

def getAllVars(formula):
    """
    Get all possible assignments for the variables in the formula.
    """
    variables = []
    if type(formula) is str:
        variables.append(formula)
    elif type(formula) is bool or formula == []:
        return []
    else:
        op = formula[0]
        if op in ['AND', 'OR']:
            for sub_formula in formula[1:]:
                variables += getAllVars(sub_formula)
        elif op == 'NOT':
            variables += getAllVars(formula[1])
        elif op == 'IMPLIES':
            variables += getAllVars(formula[1])
            variables += getAllVars(formula[2])
        elif op == 'EQUIV':
            variables += getAllVars(formula[1])
            variables += getAllVars(formula[2])
        else:  # Variable
            variables.append(formula)
    return list(set(variables))

def logical_satisfiability(formula):
    """Prints whether the formula is tautology, unsatisfiable or satisfiable."""
    res = False
    suiting_assignments = []
    vars_ = getAllVars(formula)
    all_assignments = assignments = [dict(zip(vars_, values)) for values in itertools.product([False, True], repeat=len(vars_))]

    for assignment in assignments:
        cur = evaluate(formula, assignment)
        res = res or cur
        if cur:
            suiting_assignments.append(assignment)
    if res:
        if suiting_assignments == all_assignments:
            print('Result: Tautology')
        else:
            for suiting_assignment in suiting_assignments:
                print('Result: Satisfiable, Assignments: {}'.format(suiting_assignment))
    else:
        print('Result: Unsatisfiable')
    linebreak()
    
if __name__ == '__main__':
    formulas = [
        ['OR', ['IMPLIES', ['AND', 'a', 'b'], ['OR', 'a', 'a']], ['IMPLIES', 'b', ['NOT', 'a']]],
        ['IMPLIES', ['EQUIV', ['EQUIV', 'a', 'a'], ['NOT', 'a']], 'b'],
        ['IMPLIES', ['NOT', ['OR', 'b', 'a']], ['NOT', 'b']],
        ['NOT', ['OR', ['OR', 'b', 'a'], ['IMPLIES', 'a', 'a']]],
        ['NOT', ['IMPLIES', ['AND', 'a', 'a'], ['OR', 'a', 'a']]],
        ['EQUIV', ['EQUIV', ['EQUIV', 'a', 'b'], ['IMPLIES', 'b', 'b']], ['EQUIV', ['IMPLIES', 'a', 'b'], ['IMPLIES', 'a', 'a']]]
    ] 

    # Evaluate the formula
    for i, formula in enumerate(formulas):
        print(f"Formula {i+1}: {format_formula(formula)}")
        logical_satisfiability(formula)
