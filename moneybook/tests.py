from accounts.models import User
from moneybook.models import Expense
from django.test import TestCase
from moneybook.serializers import ExpenseDefaultSerializer


def create_user(email):
    return User.objects.create_user(name='민경환', email=email, password='1234')


def create_expense(user, amount, memo='memo', is_deleted=False):
    return Expense.objects.create(user=user, amount=amount, memo=memo, is_deleted=is_deleted)


class ExpenseListTest(TestCase):
    url = '/expense/'

    def test_not_authenticated(self):
        response = self.client.get('/expense/')

        self.assertEqual(response.status_code, 403)

    def test_expense_list(self):
        user = create_user('test@test.com')
        expense = create_expense(user, amount=100)

        self.client.force_login(user)

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)

        actual = response.json()
        expected = {'count': 1, 'next': None, 'previous': None, 'results': [ExpenseDefaultSerializer(expense).data]}
        self.assertEqual(actual, expected)

    def test_deleted_expense_list(self):
        user = create_user('test@test.com')
        create_expense(user, amount=100, is_deleted=False)

        self.client.force_login(user)

        response = self.client.get(f'{self.url}?is_deleted=true')

        self.assertEqual(response.status_code, 200)

        actual = response.json()
        expected = {'count': 0, 'next': None, 'previous': None, 'results': []}
        self.assertEqual(actual, expected)


class ExpenseCreateTest(TestCase):
    url = '/expense/'

    def test_not_authenticated(self):
        response = self.client.post(self.url)

        self.assertEqual(response.status_code, 403)


class ExpenseRetrieveTest(TestCase):

    def get_url(self, expense):
        return f'/expense/{expense.id}/'

    def test_not_authenticated(self):
        user = create_user('test@test.com')
        expense = create_expense(user, amount=100, is_deleted=False)

        response = self.client.post(self.get_url(expense))

        self.assertEqual(response.status_code, 403)
