from django.contrib.auth.models import User
from django.test import TestCase




def create_user(username, email, password):
    return User.objects.create_user(username=username, email=email, password=password)


class Test(TestCase):
    def test_회원가입(self):
        response = self.client.post(
            '/accounts/register/',
            data={
                'username': 'test',
                'email': 'test@test.com',
                'password': 12345
            }
        )

        assert response.status_code == 201
        assert User.objects.count() == 1

    def test_로그인_정상(self):
        create_user(username='abcd', email='abcd@test.com', password='1234')

        response = self.client.post(
            '/accounts/login/',
            data={
                'email': 'abcd@test.com',
                'password': '1234'
            }
        )

        print(response.json())
        assert response.status_code == 200

    def test_로그인_실패(self):
        create_user(username='abcd', email='abcd@test.com', password='1234')

        response = self.client.post(
            '/accounts/login/',
            data={
                'email': 'abcd',
                'password': '5678'
            }
        )

        print(response.json())
        assert response.status_code == 400
