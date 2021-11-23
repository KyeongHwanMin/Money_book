from django.contrib.auth.models import User
from django.test import TestCase

# python manage.py test : 테스트 실행방법
# python manage.py test moneybook.tests.Test.함수 : 개별 테스트
from moneybook.models import Expense

def create_user(username, email, password):
    return User.objects.create_user(username=username, email=email, password=password)

def create_Expense(user_id, amount, memo):
    return Expense.objects.create(user_id=user_id, amount=amount, memo=memo)


class Test(TestCase):
    def test_Expense(self):
        create_user(username='test', email='test111@test.com', password='12345')
        create_Expense(user_id=1, amount="100", memo="test")
        response = self.client.get(
            '/Expense/',
            Expense.objects.all()
        )
        print(response.json())
        assert response.status_code == 200
