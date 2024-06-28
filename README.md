# smartfin-Ai-based
# Import necessary libraries
import json
from datetime import datetime

# User Database (for demonstration purposes)
user_db = {}

# Simple in-memory database for expenses
expense_db = {}

# Function to register a new user
def register_user(username, password):
    if username in user_db:
        return "Username already exists."
    user_db[username] = {
        'password': password,
        'budget': 0,
        'expenses': []
    }
    return "User registered successfully."

# Function to authenticate a user
def authenticate_user(username, password):
    if username in user_db and user_db[username]['password'] == password:
        return "Authentication successful."
    return "Invalid username or password."

# Function to set a budget for the user
def set_budget(username, budget):
    if username in user_db:
        user_db[username]['budget'] = budget
        return "Budget set successfully."
    return "User not found."

# Function to log an expense
def log_expense(username, amount, category, description):
    if username not in user_db:
        return "User not found."
    
    expense = {
        'amount': amount,
        'category': category,
        'description': description,
        'date': datetime.now().isoformat()
    }
    user_db[username]['expenses'].append(expense)
    
    return "Expense logged successfully."

# Function to get user's expense summary
def get_expense_summary(username):
    if username not in user_db:
        return "User not found."
    
    budget = user_db[username]['budget']
    expenses = user_db[username]['expenses']
    total_expense = sum(expense['amount'] for expense in expenses)
    
    return {
        'budget': budget,
        'total_expense': total_expense,
        'expenses': expenses
    }

# Example usage
print(register_user('john_doe', 'password123'))
print(authenticate_user('john_doe', 'password123'))
print(set_budget('john_doe', 5000))
print(log_expense('john_doe', 50, 'Food', 'Lunch at restaurant'))
print(log_expense('john_doe', 20, 'Transport', 'Bus ticket'))
print(json.dumps(get_expense_summary('john_doe'), indent=2))
