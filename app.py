from flask import Flask, render_template, request

app = Flask(__name__)

questions = [
    {
        "question": "Which language is mainly used with Flask?",
        "options": ["Python", "Java", "C++", "PHP"],
        "answer": "Python"
    },
    {
        "question": "What does HTML stand for?",
        "options": [
            "Hyper Text Markup Language",
            "High Text Machine Language",
            "Hyper Tool Multi Language",
            "Home Text Markup Language"
        ],
        "answer": "Hyper Text Markup Language"
    },
    {
        "question": "Which technology is used to create containers?",
        "options": ["Docker", "Git", "HTML", "MySQL"],
        "answer": "Docker"
    },
    {
        "question": "Which platform is commonly used for CI/CD workflows?",
        "options": ["GitHub Actions", "MS Word", "Paint", "Notepad"],
        "answer": "GitHub Actions"
    },
    {
        "question": "What is the purpose of a CI/CD pipeline?",
        "options": [
            "Automate testing and deployment",
            "Only write HTML",
            "Only store images",
            "Only create databases"
        ],
        "answer": "Automate testing and deployment"
    }
]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/quiz")
def quiz():
    return render_template("quiz.html", questions=questions)


@app.route("/submit", methods=["POST"])
def submit():
    score = 0

    for i, question in enumerate(questions):
        user_answer = request.form.get(f"question_{i}")

        if user_answer == question["answer"]:
            score += 1

    return render_template(
        "result.html",
        score=score,
        total=len(questions)
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)