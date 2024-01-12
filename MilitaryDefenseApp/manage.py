#!/usr/bin/env python
import os
import sys
from django.conf import settings

# Add your middleware class here
class XFrameOptionsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response['X-Frame-Options'] = 'ALLOWALL'
        return response

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MilitaryDefenseApp.settings")

    # Add your middleware class to the MIDDLEWARE setting
    sys.path.insert(0, os.path.dirname(__file__))  # Add the current directory to the Python path
    settings.MIDDLEWARE.insert(0, 'manage.XFrameOptionsMiddleware')  # Use a relative import
    # other middleware entries

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    execute_from_command_line(sys.argv)
