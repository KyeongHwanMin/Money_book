from accounts.models import User
from django.test import TestCase


# python manage.py test : 테스트 실행방법
# python manage.py test accounts.tests.Test.함수 : 개별 테스트


def create_user(name, email, password):
    return User.objects.create_user(name=name, email=email, password=password)


def login(user, password):
    return User.objects.login(user=user, password=password)


class Test(TestCase):
    def test_회원가입(self):
        response = self.client.post(
            '/accounts/register-user/',
            data={
                'email': 'tesdfst@test.com',
                'name': 'test',
                'password': '12345'
            }
        )
        print(response.json())
        assert response.status_code == 201

    def test_로그인(self):
        create_user(name='test', email='test111@test.com', password='12345')
        response = self.client.post(
            '/accounts/login/',
            data={
                'email': 'test111@test.com',
                'password': '12345'
            }
        )
        # print(response.json())
        assert response.status_code == 200

    def test_로그인_실패(self):
        create_user(name='test', email='test111@test.com', password='1234')
        response = self.client.post(
            '/accounts/login/',
            data={
                'email': 'test111@test.com',
                'password': '12345'
            }
        )
        print(response.json())
        assert response.status_code == 400

    def test_로그아웃(self):
        login(user='user', password='password')

        response = self.client.post(
            '/accounts/logout/',
        )
        print(response.json())
        assert response.status_code == 200
