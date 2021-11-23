from django.contrib.auth.models import User
from django.test import TestCase


# python manage.py test : 테스트 실행방법
# python manage.py test accounts.tests.Test.함수 : 개별 테스트


def create_user(username, email, password):
    return User.objects.create_user(username=username, email=email, password=password)


class Test(TestCase):
    def test_회원가입(self):
        response = self.client.post(
            '/accounts/register-user/',
            data={
                'email': 'tesdfst@test.com',
                'password': '12345'
            }
        )
        print(response.json())
        assert response.status_code == 201

    def test_로그인(self):
        create_user(username='test', email='test111@test.com', password='12345')
        response = self.client.post(
            '/accounts/login/',
            data={

                'email': 'test111@test.com',
                'password': '12345'
            }
        )
        print(response.json())
        assert response.status_code == 200

    def test_로그인_실패(self):
        create_user(username='test111@test.com', password='1234')
        response = self.client.post(
            '/accounts/login/',
            data={
                'username': 'test111@test.com',
                'password': '12345'
            }
        )
        print(response.json())
        assert response.status_code == 400


