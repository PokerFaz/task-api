from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Task API is running"}


def test_get_tasks():
    response = client.get("/tasks")

    assert response.status_code == 200

    tasks = response.json()

    assert len(tasks) == 2
    assert tasks[0]["title"] == "Learn CI/CD"
    assert tasks[1]["title"] == "Deploy to Kubernetes"
