#  Banking Management System

A full-stack Banking Management System built with **FastAPI** (Backend) and **Streamlit** (Frontend).
The application allows you to create, view, update, and delete bank accounts seamlessly.

##  Features

- **Create Account:** Add new bank accounts with Name, Email, and Initial Balance.
- **View Accounts:** Fetch and display all existing accounts from the database.
- **Update Account:** Modify the Name and Email of an existing account.
- **Delete Account:** Remove an account securely using its ID.

##  Technology Stack

- **Backend:** Python, FastAPI, SQLAlchemy, PostgreSQL (Psycopg2), Uvicorn
- **Frontend:** Python, Streamlit, Requests

##  Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/gitRit123/Banking-Management-System-FastApi-.git
cd Banking-Management-System-FastApi-
```

### 2. Backend Setup
1. Navigate to the `backend` directory:
   ```bash
   cd backend
   ```
2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up your PostgreSQL database and update the configuration in `database.py`.
5. Run the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```
   *The API will be available at `http://127.0.0.1:8000`.*

### 3. Frontend Setup
1. Open a new terminal and navigate to the `frontend` directory:
   ```bash
   cd frontend
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```
   *The frontend will open in your browser, typically at `http://localhost:8501`.*

##  API Endpoints

- `POST /accounts` - Create a new account
- `GET /accounts` - Retrieve all accounts
- `GET /accounts/{acc_id}` - Retrieve a specific account
- `PUT /accounts/{acc_id}` - Update an account
- `DELETE /accounts/{acc_id}` - Delete an account

---

Happy banking!
