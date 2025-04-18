# Finance Tracker

## Overview
The Finance Tracker is a personal finance management application that allows users to track their expenses efficiently. It provides a simple interface to add, view, and delete expenses while storing the data securely in an SQL database.

## Features
- Add new expenses with details such as amount, category, date, and description.
- View a list of all recorded expenses.
- Delete expenses that are no longer needed.
- Data is stored in a structured SQL database for easy access and management.

## Project Structure
```
finance-tracker
├── src
│   ├── app.py                # Entry point of the application
│   ├── database
│   │   ├── connection.py     # Database connection logic
│   │   └── models.py         # Data models for expenses
│   ├── routes
│   │   └── expenses.py       # Routes for handling expenses
│   ├── services
│   │   └── expense_service.py # Business logic for expenses
│   └── utils
│       └── helpers.py        # Utility functions
├── requirements.txt          # Project dependencies
├── .env                      # Environment variables
└── README.md                 # Project documentation
```

## Setup Instructions
1. Clone the repository:
   ```
   git clone <repository-url>
   cd finance-tracker
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Configure your environment variables in the `.env` file. Make sure to include your database connection string.

5. Run the application:
   ```
   python src/app.py
   ```

## Usage
- Access the application through your web browser at `http://localhost:5000`.
- Use the provided routes to manage your expenses.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.