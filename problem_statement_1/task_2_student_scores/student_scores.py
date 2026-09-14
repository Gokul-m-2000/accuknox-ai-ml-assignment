import requests
import matplotlib.pyplot as plt


API_URL="https://api.slingacademy.com/v1/sample-data/files/student-scores.json"

def fetch_student_scores():

    try:
        response=requests.get(API_URL,timeout=10)

        response.raise_for_status()

        data=response.json()
        
        return data

    except requests.RequestException as e:
        print(f"failed to fetch student details ,{e}")
        return None


def calculate_avg(marks):
    if marks:
        return sum(marks)/len(marks)
    
    return None


def visualize(subjects, averages):
    plt.bar(subjects, averages)

    plt.xlabel("Subjects")
    plt.ylabel("Average Score")
    plt.title("Average Score by Subject")

    plt.ylim(0, 100)
    plt.xticks(rotation=30)

    plt.tight_layout()
    plt.show()






student_details = fetch_student_scores()

if student_details is not None:

    subjects = [
        "Math",
        "History",
        "Physics",
        "Chemistry",
        "Biology",
        "English",
        "Geography"
    ]

    score_fields = [
        "math_score",
        "history_score",
        "physics_score",
        "chemistry_score",
        "biology_score",
        "english_score",
        "geography_score"
    ]

    averages = []

    for field in score_fields:

        scores = []

        for student in student_details:
            score = student.get(field)

            if score is not None:
                scores.append(score)

        average = calculate_avg(scores)
        averages.append(average)

    print("Average scores by subject:")

    for subject, average in zip(subjects, averages):
        print(f"{subject}: {average:.2f}")

    visualize(subjects, averages)