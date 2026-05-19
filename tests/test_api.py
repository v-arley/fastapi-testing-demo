def test_list_notes_returns_empty_list_when_no_notes_exist(client):
    # Arrange

    # Act
    response = client.get("/notes")

    # Assert
    assert response.status_code == 200
    assert response.json() == []


def test_create_note_returns_201_when_valid_payload(client):
    # Arrange
    payload = {
        "title": "Test note",
        "content": "This is a valid note",
        "color": "yellow"
    }

    # Act
    response = client.post("/notes", json=payload)

    # Assert
    assert response.status_code == 201
    data = response.json()

    assert data["id"] == 1
    assert data["title"] == payload["title"]
    assert data["content"] == payload["content"]
    assert data["color"] == payload["color"]


def test_create_note_returns_422_when_payload_is_invalid(client):
    # Arrange
    payload = {
        "title": "",
        "content": "This content is valid",
        "color": "yellow"
    }

    # Act
    response = client.post("/notes", json=payload)

    # Assert
    assert response.status_code == 422


def test_create_note_returns_422_when_color_is_invalid(client):
    # Arrange
    payload = {
        "title": "Invalid color note",
        "content": "This note has an invalid color",
        "color": "black"
    }

    # Act
    response = client.post("/notes", json=payload)

    # Assert
    assert response.status_code == 422
    assert response.json()["detail"] == "Invalid color"


def test_get_note_returns_404_when_note_does_not_exist(client):
    # Arrange
    note_id = 999

    # Act
    response = client.get(f"/notes/{note_id}")

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Note not found"


def test_get_note_returns_200_when_note_exists(client):
    # Arrange
    payload = {
        "title": "Existing note",
        "content": "This note exists",
        "color": "blue"
    }

    created_response = client.post("/notes", json=payload)
    note_id = created_response.json()["id"]

    # Act
    response = client.get(f"/notes/{note_id}")

    # Assert
    assert response.status_code == 200
    data = response.json()

    assert data["id"] == note_id
    assert data["title"] == payload["title"]
    assert data["content"] == payload["content"]
    assert data["color"] == payload["color"]


def test_delete_note_returns_204_when_note_exists(client):
    # Arrange
    payload = {
        "title": "Note to delete",
        "content": "This note will be deleted",
        "color": "red"
    }

    created_response = client.post("/notes", json=payload)
    note_id = created_response.json()["id"]

    # Act
    response = client.delete(f"/notes/{note_id}")

    # Assert
    assert response.status_code == 204


def test_delete_note_returns_404_when_note_does_not_exist(client):
    # Arrange
    note_id = 999

    # Act
    response = client.delete(f"/notes/{note_id}")

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Note not found"