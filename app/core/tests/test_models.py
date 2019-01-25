from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user(email='dj@dj.com', password='12345django'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating new user with email is successful"""
        email = 'sindbad@morehod.com'
        password = 'thisistest555'
        user = get_user_model().objects.create_user(email, password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for new user is normalized"""
        email = 'test@MOREHOD.COM'
        user = get_user_model().objects.create_user(email, 'test12345')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('@GOOD.com', 'test1234567')

    def test_create_super_user(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@MOREHOD.COM',
            'testtest123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )

        self.assertEqual(str(tag), tag.name)

    def test_ingredient_str(self):
        """Test ingredient string representation"""
        ingredient = models.Ingredient.objects.create(
            name='Grape',
            user=sample_user()
        )

        self.assertEqual(str(ingredient), ingredient.name)

    def test_recipe_str(self):
        """Tset recipe string representation"""
        recipe = models.Recipe.objects.create(
            user=sample_user(),
            title='Best recipe',
            time_minutes=5,
            price=5.00,
        )

        self.assertEqual(str(recipe), recipe.title)
