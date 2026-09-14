# AccuKnox AI/ML Trainee Assignment

This repository contains my implementation of the AccuKnox AI/ML Trainee assignment.

## Project Structure

```text
accuknox-ai-ml-assignment/
│
├── problem_statement_1/
│   ├── task_1_books_api/
│   │   └── books_api.py
│   │
│   ├── task_2_student_scores/
│   │   └── student_scores.py
│   │
│   └── task_3_csv_to_database/
│       ├── csv_to_database.py
│       └── users.csv
│
├── requirements.txt
├── .gitignore
└── README.md



## Setup

Python 3.x is required.

Create a virtual environment:

python -m venv .venv

For Git Bash:

source .venv/Scripts/activate

Install dependencies:

python -m pip install -r requirements.txt

## Problem Statement 1

### Task 1 — API Data Retrieval and Storage
Retrieves book data from the Open Library API, stores selected fields in SQLite, and displays the records.

Run:
python problem_statement_1/task_1_books_api/books_api.py

### Task 2 — Data Processing and Visualization
Retrieves student score data from an API, calculates subject-wise average scores, and generates a bar chart.

Run:
python problem_statement_1/task_2_student_scores/student_scores.py

### Task 3 — CSV Data Import to Database
Reads user information from a CSV file and imports it into a SQLite database.

Run:
python problem_statement_1/task_3_csv_to_database/csv_to_database.py

## Assumptions

- Multiple authors for a book are stored as a comma-separated value.
- Missing student scores are excluded from the corresponding subject average.
- The generated SQLite database files are not committed to the repository.