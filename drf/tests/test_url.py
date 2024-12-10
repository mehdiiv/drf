from django.test import SimpleTestCase
from django.urls import reverse, resolve
from drf.views import UserViewSet

class UrlTest(SimpleTestCase):
    def test_users_drfs_url(self):
        url = reverse('user-list')
        self.assertEqual(resolve(url).func.cls, UserViewSet)
