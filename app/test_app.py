from app import app, clasificar


def test_home_returns_ok():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"


def test_disk_returns_expected_fields():
    client = app.test_client()
    response = client.get("/disk")
    assert response.status_code == 200
    data = response.get_json()
    for field in ("total_gb", "used_gb", "usage_percent", "level"):
        assert field in data


def test_clasificar_levels():
    assert clasificar(50) == "normal"
    assert clasificar(80) == "WARNING"
    assert clasificar(90) == "CRITICAL"
