
# Django-cash-management

## Introduction

a cash management system using Django and Django Rest Framework. The system should allow users to manage their cash flow by creating and updating transactions, tracking balances, and generating reports.## Features

- **User Authentication**: Register, login, and manage your user account.

- **Transaction Management**:
    Users  be able to create, retrieve, update, and delete transactions.
    Each transaction  include the following information:

    - Amount: The amount of money involved in the transaction.
    - Type: The type of transaction (e.g., income, expense).
    - Category: The category of the transaction (e.g., groceries, utilities).
    - Date: The date of the transaction.

    Users  be able to filter and sort transactions based on different criteria (e.g., date, category).
- **Balance Tracking**:
    - The system  keep track of the user's balance by calculating the current balance based on the transactions.
    - The balance  be updated automatically whenever a new transaction is created or updated.
- **Reports**:
    - Users should be able to generate reports to analyze their cash flow.
    - The system should provide at least one type of report, such as a monthly summary or a category-wise expense report.

## Photos:
![ERD](/cash_management.png)

## Project Structure

```
.
├── users              # User account management
├── core               # Core functionalities
├── meetings           # meeting management
├── reservations       # reservation management
├── teams               # team management
├── app                # Project settings
├── manage.py          # Django management script
└── requirements       # Project dependencies
```

## Requirements

- Python 3.x
- Django 4.2
- Django REST Framework 3.14.0
- simplejwt 5.3.1
- spectacular 0.26.5


## Installation

1. Clone the repository:

    ```
    git clone https://github.com/mohahmadi2001/django-cash-managments.git
    ```

2. Navigate to the project directory:

    ```
    cd Django-chash-managements
    ```

3. Create a virtual environment and activate it:

    ```
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venvScriptsactivate`
    ```

4. Install the required packages:

    ```
    pip install -r requirements/developments.txt
    ```

5. Apply migrations:

    ```
    python manage.py migrate
    ```

6. Run the server:

    ```
    python manage.py runserver
    ```
7. Run with Docker

    ```
    docker-compose up --build
    ```
## Usage

To use the application, navigate to `http://localhost:8000/` in your web browser. You'll find options to manage meetings and reservations.