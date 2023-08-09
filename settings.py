INSTALLED_APPS = [
    # ...
    'rest_framework',
    'api',  # Your app name
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
}

JWT_AUTH = {
    'JWT_SECRET_KEY': 'your-secret-key',  # Replace with your actual secret key
    'JWT_ALGORITHM': 'HS256',
}
