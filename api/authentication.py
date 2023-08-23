from tastypie.authentication import ApiKeyAuthentication


class CustomAuthentication(ApiKeyAuthentication):
    """
    Custom authentication class based on ApiKeyAuthentication.

    This class extends the functionality of ApiKeyAuthentication and overrides the
    'is_authenticated' method. It allows unauthenticated access for GET requests and
    delegates to the parent class for other request methods.

    Methods:
    - is_authenticated: Overrides the base method to allow unauthenticated access for GET requests.

    Parameters:
    - request: The HTTP request object.
    - **kwargs: Additional keyword arguments passed to the parent method.

    Returns:
    - True if the request is authenticated for GET requests, otherwise delegates to the parent
      method's return value.
    """

    def is_authenticated(self, request, **kwargs):
        """
        Check if the request is authenticated.

        This method overrides the base method to allow unauthenticated access for GET requests.

        Parameters:
        - request: The HTTP request object.
        - **kwargs: Additional keyword arguments passed to the parent method.

        Returns:
        - True if the request is authenticated for GET requests, otherwise delegates to the
          parent method's return value.
        """
        if request.method == 'GET':
            return True

        return super().is_authenticated(request, **kwargs)
