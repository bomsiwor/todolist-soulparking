from typing import Any
from httpx import Response
from app.server import app
from fastapi.testclient import TestClient

# Create client instance
client = TestClient(app)


def create_todo_payload():
    return {"title": "Testing title", "description": "Testing description"}


def get_response_data(response: Response) -> Any:
    json = response.json()

    return json["data"]


def test_get_all_todo():
    response = client.get("/api/todos")

    assert response.status_code == 200
    response_data = get_response_data(response)

    assert len(response_data) == 0


def test_create_todo():
    # Create a todo
    response = client.post("/api/todos", json=create_todo_payload())

    assert response.status_code == 201
    response_data = get_response_data(response)

    # Assert content
    assert response_data["title"] == "Testing title"
    assert response_data["description"] == "Testing description"

    # Asssert that the ID is accessible
    response = client.get(f"api/todos/{response_data['id']}")
    assert response.status_code == 200

    # Assert list
    response = client.get("/api/todos")
    response_data = get_response_data(response)

    assert len(response_data) == 1


def test_create_multiple_todo():
    # Create multiple todos
    for i in range(1, 3):
        client.post("/api/todos", json=create_todo_payload())

    # Assert list have exact multiple todo count
    response = client.get("/api/todos")
    response_data = get_response_data(response)

    assert len(response_data) == 3


def test_update_todo():
    # Create new too
    # Get the ID
    response_todo = client.post("/api/todos", json=create_todo_payload())
    todo_id = get_response_data(response_todo)["id"]

    # Update todo with new data
    response = client.put(
        f"/api/todos/{todo_id}", json={**create_todo_payload(), "title": "Updated"}
    )
    response_data = get_response_data(response)

    assert response.status_code == 200
    assert response_data["title"] == "Updated"


def test_finish_todo():
    # Create new too
    # Get the ID
    response_todo = client.post("/api/todos", json=create_todo_payload())
    todo_id = get_response_data(response_todo)["id"]

    # Finish todo
    response = client.patch(f"api/todos/{todo_id}/finish")
    response_data = get_response_data(response)

    assert response.status_code == 200
    assert response_data["finishedAt"] is not None


def test_double_finish_todo():
    # Create new too
    # Get the ID
    response_todo = client.post("/api/todos", json=create_todo_payload())
    todo_id = get_response_data(response_todo)["id"]

    # Finish todo
    response = client.patch(f"api/todos/{todo_id}/finish")
    response_data = get_response_data(response)

    assert response.status_code == 200
    assert response_data["finishedAt"] is not None

    # Finish for the 2nd time
    response = client.patch(f"api/todos/{todo_id}/finish")
    response_data = get_response_data(response)

    assert response.status_code == 409


def test_delete_todo():
    # Create new too
    # Get the ID
    response_todo = client.post("/api/todos", json=create_todo_payload())
    todo_id = get_response_data(response_todo)["id"]

    # Delete todo
    response = client.delete(f"api/todos/{todo_id}")

    assert response.status_code == 200

    # Assert that the data is not found after deleted
    response_detail = client.get(f"/todo/{todo_id}")

    assert response_detail.status_code == 404
