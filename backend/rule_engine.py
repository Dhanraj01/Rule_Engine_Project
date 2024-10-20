
from rule_ast import Node

def create_rule(rule_string):
    pass  

def combine_rules(rules):
    
    pass  

def evaluate_rule(ast, data):
    if ast.type == "operand":
        # Evaluate simple condition
        return eval_condition(ast, data)
    elif ast.type == "operator":
        # Combine left and right node based on operator (AND/OR)
        left_result = evaluate_rule(ast.left, data)
        right_result = evaluate_rule(ast.right, data)
        if ast.value == "AND":
            return left_result and right_result
        elif ast.value == "OR":
            return left_result or right_result
    return False

def eval_condition(node, data):
    return eval(f"{data[node.value['field']]} {node.value['operator']} {node.value['value']}")
