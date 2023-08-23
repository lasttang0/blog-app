from django.test import TestCase, RequestFactory
from tastypie.authentication import ApiKeyAuthentication
from api.authentication import CustomAuthentication


class CustomAuthenticationTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_is_authenticated_with_get_request(self):
        """
        Test whether 'is_authenticated' returns True for GET requests.
        """
        authentication = CustomAuthentication()
        request = self.factory.get('/api/v1/')
        self.assertTrue(authentication.is_authenticated(request))
