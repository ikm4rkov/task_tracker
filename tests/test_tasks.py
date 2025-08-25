import uuid

def test_create_task(client):
    response = client.post("/api/tasks/", json={"title": "Test Task", "description": "Desc"})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Task"
    assert data["description"] == "Desc"
    assert "id" in data

def test_create_task_without_description(client):
    response = client.post("/api/tasks/", json={"title": "No Description"})
    assert response.status_code == 200
    data = response.json()
    assert data["description"] is None

def test_get_tasks(client):
    client.post("/api/tasks/", json={"title": "Task 1"})
    client.post("/api/tasks/", json={"title": "Task 2"})
    response = client.get("/api/tasks/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 2

def test_get_task_by_id(client):
    create_response = client.post("/api/tasks/", json={"title": "Single Task"})
    task_id = create_response.json()["id"]
    response = client.get(f"/api/tasks/{task_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == task_id

def test_update_task_title(client):
    create_response = client.post("/api/tasks/", json={"title": "Old Title"})
    task_id = create_response.json()["id"]
    response = client.put(f"/api/tasks/{task_id}", json={"title": "New Title"})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "New Title"

def test_update_task_description(client):
    create_response = client.post("/api/tasks/", json={"title": "Task", "description": "Old"})
    task_id = create_response.json()["id"]
    response = client.put(f"/api/tasks/{task_id}", json={"description": "New"})
    assert response.status_code == 200
    data = response.json()
    assert data["description"] == "New"

def test_update_nonexistent_task(client):
    random_id = str(uuid.uuid4())
    response = client.put(f"/api/tasks/{random_id}", json={"title": "Update"})
    assert response.status_code == 404

def test_delete_task(client):
    create_response = client.post("/api/tasks/", json={"title": "To Delete"})
    task_id = create_response.json()["id"]
    delete_response = client.delete(f"/api/tasks/{task_id}")
    assert delete_response.status_code == 200
    get_response = client.get(f"/api/tasks/{task_id}")
    assert get_response.status_code == 404

def test_delete_nonexistent_task(client):
    random_id = str(uuid.uuid4())
    response = client.delete(f"/api/tasks/{random_id}")
    assert response.status_code == 404

def test_not_found(client):
    random_id = str(uuid.uuid4())
    response = client.get(f"/api/tasks/{random_id}")
    assert response.status_code == 404

def test_multiple_creates_and_updates(client):
    ids = []
    for i in range(5):
        r = client.post("/api/tasks/", json={"title": f"Task {i}"})
        ids.append(r.json()["id"])
    for task_id in ids:
        r = client.put(f"/api/tasks/{task_id}", json={"title": f"Updated {task_id}"})
        assert r.status_code == 200
        assert r.json()["title"].startswith("Updated")
