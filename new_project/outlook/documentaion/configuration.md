# Configuration

This document provides information on how to configure the project for specific settings, environmental variables, and other customization options.

## Project Settings

Key project settings and configurations are typically found in the `settings.py` file of your Django project. You may need to modify the following settings based on your project's requirements:

```python
# outlook/settings.py

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  # Choose the appropriate database engine
        'NAME': 'mydatabase',
        'USER': 'myuser',
        'PASSWORD': 'mypassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Security settings
SECRET_KEY = 'your-secret-key'  #generated from Azure App Registration

# Outlook OAuth configuration
SOCIAL_AUTH_MICROSOFT_OAUTH2_KEY = 'Your-Outlook-App-ID'
SOCIAL_AUTH_MICROSOFT_OAUTH2_SECRET = 'Your-Outlook-App-Secret'


# Environment Variables

Sensitive information, such as secret keys, API tokens, or database credentials, should be stored as environment variables to enhance security. You can set environment variables in your development environment or on your production server.

Example of setting environment variables:

export SECRET_KEY="your-secret-key"
export DATABASE_URL="postgres://myuser:mypassword@localhost:5432/mydatabase"
export OUTLOOK_OAUTH_APP_ID="Your-Outlook-App-ID"
export OUTLOOK_OAUTH_APP_SECRET="Your-Outlook-App-Secret"

In your project, you can access environment variables using Python's os module:

#  settings.py
import os

SECRET_KEY = os.environ.get("SECRET_KEY")
DATABASE_URL = os.environ.get("DATABASE_URL")
OUTLOOK_OAUTH_APP_ID = os.environ.get("OUTLOOK_OAUTH_APP_ID")
OUTLOOK_OAUTH_APP_SECRET = os.environ.get("OUTLOOK_OAUTH_APP_SECRET")

**Note**
Provide any troubleshooting tips or common issues that users might encounter during the installation process.

For more detailed information, refer to the [official documentation](link_to_more_detailed_installation_guide).

## Cnclusion 

This `configuration.md` document provides guidance on configuring your project, including modifying project settings in `settings.py`, setting environment variables, and addressing any additional configuration requirements. Users and developers can refer to this document to customize the project according to their needs.
