from app import app

def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200  # Было 400 (ошибка), должно быть 200 (успех)
    assert response.data == b'Hello'