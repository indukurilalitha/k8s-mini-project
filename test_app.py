from app import app

def test_home_route():
    tester = app.test_client()
    response = tester.get("/")
    assert response.status_code == 200
    assert b"Hello, Kubernetes!" in response.data

def test_health_route():
    tester = app.test_client()
    response = tester.get("/health")
    assert response.status_code == 200
    assert b"status" in response.data
