from flask import Flask
from database.connection import create_connection
from routes.expenses import expenses_bp

app = Flask(__name__)

# Initialize database connection
db_connection = create_connection()

# Register routes
app.register_blueprint(expenses_bp)

if __name__ == "__main__":
    app.run(debug=True)