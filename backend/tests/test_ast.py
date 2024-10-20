# backend/tests/test_ast.py
import unittest
from ast import Node

class TestAST(unittest.TestCase):
    def test_ast_creation(self):
        root = Node("operator", left=Node("operand", value={"field": "age", "operator": ">", "value": 30}), right=None)
        self.assertEqual(root.type, "operator")
        self.assertEqual(root.left.value["field"], "age")
