def test_register_and_login(client):
    register = client.post("/auth/register", json={
        "email": "auth@test.com",
        "password": "password123"
    })
    assert register.status_code == 200
