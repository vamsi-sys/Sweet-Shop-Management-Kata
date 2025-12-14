import uuid


def auth_header(client):
    email = f"{uuid.uuid4()}@test.com"

    client.post("/auth/register", json={
        "email": email,
        "password": "pass123"
    })

    login = client.post("/auth/login", json={
        "email": email,
        "password": "pass123"
    })

    token = login.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}


def test_purchase_reduces_quantity(client):
    headers = auth_header(client)

    sweet = client.post(
        "/sweets",
        json={
            "name": "Ladoo",
            "category": "Indian",
            "price": 10.0,
            "quantity": 2
        },
        headers=headers
    )

    assert sweet.status_code == 200
    sweet_id = sweet.json()["id"]

    purchase = client.post(
        f"/sweets/{sweet_id}/purchase",
        headers=headers
    )

    assert purchase.status_code == 200
    assert purchase.json()["quantity"] == 1


def test_purchase_out_of_stock(client):
    headers = auth_header(client)

    sweet = client.post(
        "/sweets",
        json={
            "name": "Barfi",
            "category": "Indian",
            "price": 15.0,
            "quantity": 0
        },
        headers=headers
    )

    assert sweet.status_code == 200
    sweet_id = sweet.json()["id"]

    purchase = client.post(
        f"/sweets/{sweet_id}/purchase",
        headers=headers
    )

    assert purchase.status_code == 400
