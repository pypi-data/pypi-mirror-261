from rest_framework.throttling import SimpleRateThrottle
from rest_framework.settings import api_settings
from . import models
import datetime
from rest_framework.request import Request
from .utils import get_api_key


class APIKeyThrottle(SimpleRateThrottle):
    """
    Throttle class to limit API requests based on API keys.

    Attributes:
        API_KEY_HEADER (str): The HTTP header used to pass the API key.
        scope_long (str): The rate of requests allowed per month.
        model: The Django model class used for querying the API key.
    """
    API_KEY_HEADER = getattr(api_settings, 'API_KEY_HEADER', "X_API_KEY")
    API_KEY_IN_QUERY_PARAMS = False
    scope_long = SimpleRateThrottle.THROTTLE_RATES.get('scope_long')
    model = models.APIKey

    if scope_long and not (model and hasattr(model, "key")):
        raise NotImplementedError("API_KEY model must have a 'key' attribute.")
    
    def get_cache_key(self, request: Request, view):
        """
        Retrieve the cache key for the request.

        Args:
            request: The incoming HTTP request.
            view: The Django view being accessed.

        Returns:
            str: A unique cache key for the request.
        """
        return self.cache_format % {
            'scope': self.scope,
            'ident': get_api_key(request=request, api_key_header=self.API_KEY_HEADER, key_in_query_params=self.API_KEY_IN_QUERY_PARAMS)
        }
    
    def allow_request(self, request: Request, view) -> bool:
        """
        Determine if the request should be allowed based on throttle limits.
        """
        if not super().allow_request(request, view):
            return False

        if self.scope_long:
            key = get_api_key(request=request, api_key_header=self.API_KEY_HEADER, key_in_query_params=self.API_KEY_IN_QUERY_PARAMS)
            filter_kwargs = {'created_at__gte': datetime.datetime.now() - datetime.timedelta(days=30)}
            key_obj = self.model.objects.filter(key=key).first()
            if key_obj and key_obj.requests.filter(**filter_kwargs).count() >= self.get_scope_long_rate(request):
                return False
                
            models.Request.objects.create(api_key=key_obj) # Create a request mapped to the key obj

        return True
    
    def get_scope_long_rate(self, request: Request) -> int:
        """
        Retrieve the request rate limit for a long scope.

        Args:
            request: The incoming HTTP request.

        Returns:
            int: The number of requests allowed per month.

        Raises:
            ValueError: If 'scope_long' is not an integer.
        """
        if self.scope_long:
            try:
                return int(self.scope_long)
            except ValueError:
                raise ValueError("scope_long must be an integer.")
