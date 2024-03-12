# drf_api_key_auth

`drf_api_key_auth` is a Django REST Framework library designed for creating, managing, and securing API keys. It provides easy-to-use models, permissions, and throttling classes to manage API access effectively.

## Installation

Install  `drf_api_key_auth` using pip:

```bash
pip install drf_api_key_auth
```

Configuration
After installation, you need to add drf_apikey to your INSTALLED_APPS in the Django settings.

```bash
INSTALLED_APPS = (
    ...
    'drf_apikey',
    ...
)
```

Next, set up the Django REST framework permissions in your Django settings:
```bash
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'drf_apikey.permissions.APIKeyPermission',
    ),
    'DEFAULT_THROTTLE_CLASSES': (
        'drf_apikey.throttling.APIKeyThrottle',
    ),
    'DEFAULT_THROTTLE_RATES': {
        'scope_long': '1000'    # Relates to monthly limits, should just be integer
    }
}
```

## Example Request
Here's a basic example of making a request to a Django REST Framework view that is protected with drf_apikey permissions:

```bash
import requests

response = requests.get(
    url="http://0.0.0.0:8000/api/your_endpoint",
    headers={
        "X_API_KEY": "fd8b4a98c8f53035aeab410258430e2d86079c93",
    },
)

print(response.json())
```

in this example above, replace "http://0.0.0.0:8000/api/your_endpoint" with the actual endpoint you wish to access, and "fd8b4a98c8f53035aeab410258430e2d86079c93" with a valid API key.


## Contributing
Contributions are welcome. Please read the contributing guide for more information.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
