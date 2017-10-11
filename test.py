from models.user import User
from utils import log


def test():
    form = dict(
        username='whister',
        password='123',
        id='0',
    )
    u = User.new(form)
    log(u.json())


if __name__ == '__main__':
    test()