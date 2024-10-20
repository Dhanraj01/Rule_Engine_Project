# backend/models.py
from db import db

class Rule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rule_string = db.Column(db.String(500))
    ast_representation = db.Column(db.Text)  # Store AST as a JSON or string

    def __repr__(self):
        return f"<Rule {self.rule_string}>"