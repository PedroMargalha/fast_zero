def test_get_token(client, user):
    response = client.post(
        '/auth/token',
        data={'username': user.email, 'password': user.clean_password},
    )
    token = response.json()

    assert response.status_code == 200
    assert 'access_token' in token
    assert 'token_type' in token


def test_get_token_incorrect_email(client, user):
    response = client.post(
        '/auth/token',
        data={'username': 'test@test.com', 'password': user.clean_password},
    )
    assert response.status_code == 400
    response.json() == {'detail': 'Incorrect email or password'}


def test_get_token_incorrect_password(client, user):
    response = client.post(
        '/auth/token',
        data={'username': user.email, 'password': '1234'},
    )
    assert response.status_code == 400
    response.json() == {'detail': 'Incorrect email or password'}
