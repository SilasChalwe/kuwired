import os
from django.core.wsgi import get_wsgi_application

# Set the default settings module for the 'DJANGO_SETTINGS_MODULE' environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Kuwired_project.settings')  # Ensure this matches your project structure

# Create the WSGI application callable
application = get_wsgi_application()

