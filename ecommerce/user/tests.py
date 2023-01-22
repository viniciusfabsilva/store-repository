from django.test import TestCase
from .models import User
from datetime import date
from rest_framework.test import APITestCase
from .serializers import UserSerializer


class UserTestCase(TestCase):
    def test_create_user(self):
        user = User.objects.create(
            email="user@example.com",
            password="password123",
            first_name="User",
            birth_date="2000-01-01"
        )
        self.assertEqual(user.email, "user@example.com")
        self.assertEqual(user.first_name, "User")
        self.assertEqual(user.birth_date, "2000-01-01")


class UserSerializerTestCase(APITestCase):
    def test_serialize_user(self):
        user = User.objects.create(
            email="user@example.com",
            password="password123",
            first_name="User",
            birth_date="2000-01-01"
        )
        serializer = UserSerializer(user)
        self.assertEqual(serializer.data['email'], "user@example.com")
        self.assertEqual(serializer.data['first_name'], "User")
        self.assertEqual(serializer.data['birth_date'], "2000-01-01")
