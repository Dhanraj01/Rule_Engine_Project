from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from rule_engine import create_rule as create_rule_logic, combine_rules, evaluate_rule

app = Flask(__name__)

CORS(app)

# Set up a simple SQLite database for rules
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rules_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Rule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rule_string = db.Column(db.String(500), nullable=False)


@app.route('/')
def index():
    return render_template('index.html')  


@app.route('/create_rule', methods=['POST'])
def create_rule_route():
    data = request.get_json()
    rule_string = data.get('rule_string')
    
    
    if not rule_string:
        return jsonify({"error": "Invalid rule string"}), 400
    
    
    new_rule = Rule(rule_string=rule_string)
    db.session.add(new_rule)
    db.session.commit()

    return jsonify({"message": "Rule created successfully!"}), 201


@app.route('/combine_rules', methods=['POST'])
def combine_rules_route():
    data = request.get_json()
    rules = data.get('rules')
    
    if not rules:
        return jsonify({"error": "No rules provided"}), 400
    
    combined_ast = combine_rules(rules)
    return jsonify({"message": "Rules combined successfully!", "combined_ast": str(combined_ast)}), 200

# Route to evaluate a rule
@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule_route():
    data = request.get_json()
    ast = data.get('ast')
    input_data = data.get('data')
    
    if not ast or not input_data:
        return jsonify({"error": "AST or data missing"}), 400
    
    result = evaluate_rule(ast, input_data)
    return jsonify({"message": "Rule evaluated successfully!", "result": result}), 200

# Explicitly create tables in the main block
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Ensure tables are created on startup
    app.run(host='127.0.0.1', port=3000, debug=True)
