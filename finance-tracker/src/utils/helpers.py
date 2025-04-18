def format_date(date_string):
    from datetime import datetime
    
    try:
        return datetime.strptime(date_string, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Incorrect date format, should be YYYY-MM-DD")

def validate_expense_data(expense_data):
    required_fields = ['amount', 'category', 'date', 'description']
    for field in required_fields:
        if field not in expense_data:
            raise ValueError(f"Missing required field: {field}")
    
    if not isinstance(expense_data['amount'], (int, float)) or expense_data['amount'] <= 0:
        raise ValueError("Amount must be a positive number")
    
    return True