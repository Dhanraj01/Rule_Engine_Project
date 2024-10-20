# Rule_Engine_Project
 
Rule Engine API
This is a simple Rule Engine application built using Flask, SQLAlchemy, and Flask-Migrate. The rule engine allows you to create, combine, and evaluate rules using Abstract Syntax Tree (AST) logic. The project provides a RESTful API for creating and managing rules.

Features
Create Rule: Create a new rule and save it to the database.
Combine Rules: Combine multiple rules into a single rule.
Evaluate Rule: Evaluate a rule against data to check its validity.
Tech Stack
Backend: Flask (Python)
Database: SQLite (or any database configured with SQLAlchemy)
Frontend: HTML (served via Flask templates)
Migrations: Flask-Migrate for database migration
API: REST API with JSON for creating, combining, and evaluating rules

Folder Structure
Rule_Engine_Project/
│
├── backend/
│   └── api.py           # Flask app and API logic
├── ui/
│   └── templates/
│       └── index.html   # Frontend HTML template
│
├── migrations/          # Database migration files (created by Flask-Migrate)
├── venv/                # Python virtual environment
├── requirements.txt     # Python dependencies
├── README.md            # This README file
└── rules_data.db        # SQLite database (auto-generated after setup)

Prerequisites
Before setting up the project, ensure you have the following installed:

Python 3.7+
Virtualenv
SQLite (for development)

Setup Instructions
1. Clone the Repository

git clone https://github.com/your-username/rule-engine.git
cd rule-engine


2. Create a Virtual Environment
python -m venv venv

Activate the virtual environment:
venv\Scripts\activate


3. Install Dependencies
pip install -r requirements.txt

4. Run Database Migrations
flask db init
flask db migrate
flask db upgrade

5. Start the Application

python backend/api.py
Your Flask app will run locally at http://127.0.0.1:5000/.

API Endpoints
1. Create Rule
URL: /create_rule
Method: POST
Content-Type: application/json
Body:
{
  "rule_string": "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)"
}
Response:

{
  "message": "Rule created successfully!"
}

2. Combine Rules
URL: /combine_rules
Method: POST
Content-Type: application/json
Body:
json
{
  "rules": ["rule1", "rule2"]
}
Response:
json
{
  "combined_ast": "Combined rule AST representation"
}


3. Evaluate Rule
URL: /evaluate_rule
Method: POST
Content-Type: application/json
Body:
json
{
  "ast": "Abstract Syntax Tree (AST) string",
  "data": {
    "age": 35,
    "department": "Sales",
    "salary": 60000
  }
}

json
Copy code
{
  "result": true
}


Frontend
The project includes an HTML template (index.html) served through the Flask app. The template can be found in the ui/templates folder.

Database
The default configuration uses SQLite. You can modify the SQLALCHEMY_DATABASE_URI in the api.py file if you want to switch to a different database like PostgreSQL or MySQL.
