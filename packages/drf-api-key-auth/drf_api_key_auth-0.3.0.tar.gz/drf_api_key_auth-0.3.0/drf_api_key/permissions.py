from rest_framework.permissions import BasePermission
from rest_framework.settings import api_settings
from .models import APIKey
from .utils import get_api_key


class APIKeyPermission(BasePermission):
    """
    Custom permission class to check for the presence of an API key.
    
    Attributes:
        API_KEY_HEADER (str): The HTTP header used to pass the API key.
        KEY_IN_QUERY_PARAMS (bool): Flag to indicate if the key can also be passed in query params.
        model: The Django model class used for querying the API key, important if using subclassed models.
    """

    API_KEY_HEADER = getattr(api_settings, 'API_KEY_HEADER', "X_API_KEY")
    API_KEY_IN_QUERY_PARAMS = False
    model = APIKey
    
    def has_permission(self, request, view):
        """
        Check if the request contains a valid API key.
        """
        key = get_api_key(request=request, api_key_header=self.API_KEY_HEADER, key_in_query_params=self.API_KEY_IN_QUERY_PARAMS)
        return self.model.objects.filter(key=key).exists() if key else False
    
  
