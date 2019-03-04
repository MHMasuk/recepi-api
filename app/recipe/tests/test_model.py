from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from .. import models
from ..serializers import TagSerializer


TAGS_URL = reverse('recipe:tag-list')


def sample_user(email='test@gmail.com', password='test2323'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)


class RecipeModelTest(TestCase):
    """Test case for Recipe model"""

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='MHmasuk'
        )

        self.assertEqual(str(tag), tag.name)


class PublicTagApiTests(TestCase):
    """Test the publiclly available api"""

    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        """Test that login is required for retrieving tags"""
        res = self.client.get(TAGS_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateTagApiTest(TestCase):
    """Test the authorized user tags API"""

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            'test@gmail.com',
            'password2323'
        )

        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_retrieve_tags(self):
        """Test retrieving tags"""
        models.Tag.objects.create(user=self.user, name='Mh')
        models.Tag.objects.create(user=self.user, name='Hossain')

        res = self.client.get(TAGS_URL)

        tags = models.Tag.objects.all().order_by('-name')
        serializer = TagSerializer(tags, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_tags_limited_to_user(self):
        """Test that tags are returned are for the authenticated user"""
        user2 = get_user_model().objects.create_user(
            'test2@gmail.com',
            'password3434'
        )

        models.Tag.objects.create(user=user2, name='HOss')
        tag = models.Tag.objects.create(user=self.user, name='Food')

        res = self.client.get(TAGS_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]['name'], tag.name)
