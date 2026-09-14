# AccuKnox AI/ML Trainee Assignment

This repository contains my submission for the AccuKnox AI/ML Trainee assignment.

## Project Structure

- problem_statement_1/
  - task_1_books_api/
    - books_api.py
  - task_2_student_scores/
    - student_scores.py
  - task_3_csv_to_database/
    - csv_to_database.py
    - users.csv
- assignment_2/
  - Gokul_M_AccuKnox_AI_ML_Assignment.pdf
  - Gokul_M_AccuKnox_AI_ML_Assignment.docx
- requirements.txt
- .gitignore
- README.md

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

## Assignment 2 — Written Responses

The detailed written responses are provided in the following documents:

- [Assignment 2 – PDF](./assignment_2/Gokul_M_AccuKnox_AI_ML_Assignment.pdf)
- [Assignment 2 – DOCX](./assignment_2/Gokul_M_AccuKnox_AI_ML_Assignment.docx)

The written assignment covers:

- AI/ML self-assessment
- LLM chatbot architecture
- Vector databases and database selection

## Most Complex Python Code

[View run_pipeline.py](https://github.com/Gokul-m-2000/churn-analytics-platform/blob/main/backend/run_pipeline.py)

## Most Complex Database Code

[View models.py](https://github.com/Gokul-m-2000/churn-analytics-platform/blob/main/backend/app/models.py)

## Assumptions

- Multiple authors for a book are stored as a comma-separated value.
- Missing student scores are excluded from the corresponding subject average.
- The generated SQLite database files are not committed to the repository.