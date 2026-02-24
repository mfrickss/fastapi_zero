from attr import asdict
from tests.conftest import mock_db_time
from sqlalchemy import select

from fastapi_zero.models import User


def test_create_user(session):

    with mock_db_time(model=User) as time:
        new_user = User(
            username='alice', password='secret', email='test@test'
        )
        session.add(new_user)
        session.commit()

    user = session.scalar(select(User).where(User.username == 'alice'))

    assert asdict(user) == {
        'id': 1,
        'username': 'alice',
        'password': 'secret',
        'email': 'teste@test',
        'created_at': time
    }
