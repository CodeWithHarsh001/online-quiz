
from app import app


def test_home_page():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_quiz_page():
    client = app.test_client()
    response = client.get("/quiz")
    assert response.status_code == 200


def test_submit_quiz():
    client = app.test_client()
    response = client.post("/submit", data={
        "question_0": "Python",
        "question_1": "Hyper Text Markup Language",
        "question_2": "Docker",
        "question_3": "GitHub Actions",
        "question_4": "Automate testing and deployment"
    })

    assert response.status_code == 200
    assert b"5" in response.data