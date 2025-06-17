from fastapi_zero.models import User


def test_create_user():
    user = User(username='testuser', email='test@test.com', password='secret')

    assert user.username == 'testuser'
    assert user.email == 'test@test.com'
