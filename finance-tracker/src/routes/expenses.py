from flask import Blueprint, request, jsonify
from src.services.expense_service import fetch_expenses, create_expense, remove_expense

expenses_bp = Blueprint('expenses', __name__)

@expenses_bp.route('/expenses', methods=['GET'])
def get_expenses():
    expenses = fetch_expenses()
    return jsonify(expenses), 200

@expenses_bp.route('/expenses', methods=['POST'])
def add_expense():
    data = request.json
    expense = create_expense(data)
    return jsonify(expense), 201

@expenses_bp.route('/expenses/<int:expense_id>', methods=['DELETE'])
def delete_expense(expense_id):
    success = remove_expense(expense_id)
    if success:
        return jsonify({'message': 'Expense deleted successfully'}), 200
    return jsonify({'message': 'Expense not found'}), 404