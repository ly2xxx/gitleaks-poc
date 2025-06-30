"""
Configuration file with more secrets for gitleaks to detect
"""

import os

# Database configurations
DATABASE_CONFIG = {
    'host': 'prod-db.example.com',
    'username': 'admin',
    'password': 'MyS3cr3tP@ssw0rd!',
    'database': 'production_db',
    'port': 5432
}

# API Keys and Tokens
API_KEYS = {
    'openai': 'sk-1234567890abcdef1234567890abcdef1234567890abcdef12',
    'anthropic': 'sk-ant-api01-1234567890abcdef1234567890abcdef1234567890abcdef',
    'google_maps': 'AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI',
    'sendgrid': 'SG.1234567890abcdef.1234567890abcdef1234567890abcdef12',
}

# OAuth Credentials
OAUTH_CONFIG = {
    'google': {
        'client_id': '1234567890-abcdefghijklmnopqrstuvwxyz123456.apps.googleusercontent.com',
        'client_secret': 'GOCSPX-1234567890abcdef1234567890abcdef',
    },
    'facebook': {
        'app_id': '1234567890123456',
        'app_secret': '1234567890abcdef1234567890abcdef',
    },
    'twitter': {
        'consumer_key': 'abcdefghijklmnopqrstuvwx',
        'consumer_secret': '1234567890abcdef1234567890abcdef1234567890abcdef12',
        'access_token': '1234567890-abcdefghijklmnopqrstuvwxyz1234567890abcdef',
        'access_token_secret': '1234567890abcdef1234567890abcdef1234567890',
    }
}

# Encryption keys
ENCRYPTION_KEY = b'1234567890abcdef1234567890abcdef'
FERNET_KEY = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJK='

# Redis configuration
REDIS_URL = 'redis://:supersecretredispassword@redis.example.com:6379/0'

# MongoDB connection
MONGO_URI = 'mongodb://admin:mongosecretpass@mongo.example.com:27017/mydb'

# Webhook URLs
WEBHOOKS = {
    'discord': 'https://discord.com/api/webhooks/123456789012345678/abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    'teams': 'https://outlook.office.com/webhook/a1b2c3d4-e5f6-7890-abcd-ef1234567890@a1b2c3d4-e5f6-7890-abcd-ef1234567890/IncomingWebhook/abcdef1234567890/a1b2c3d4-e5f6-7890-abcd-ef1234567890',
}

# Email configuration
EMAIL_CONFIG = {
    'smtp_server': 'smtp.gmail.com',
    'smtp_port': 587,
    'username': 'myapp@example.com',
    'password': 'myemailpassword123',
    'use_tls': True
}

# Cloud provider credentials
CLOUD_CREDENTIALS = {
    'aws': {
        'access_key_id': 'AKIAI1234567890ABCDEF',
        'secret_access_key': '1234567890abcdef1234567890abcdef1234567890',
        'region': 'us-west-2'
    },
    'azure': {
        'subscription_id': '12345678-1234-1234-1234-123456789012',
        'client_id': '12345678-1234-1234-1234-123456789012',
        'client_secret': '1234567890abcdef1234567890abcdef',
        'tenant_id': '12345678-1234-1234-1234-123456789012'
    },
    'gcp': {
        'project_id': 'my-gcp-project-123456',
        'private_key_id': '1234567890abcdef1234567890abcdef12345678',
        'private_key': '-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC1234567890\n-----END PRIVATE KEY-----\n',
        'client_email': 'service-account@my-gcp-project-123456.iam.gserviceaccount.com',
        'client_id': '123456789012345678901',
    }
}

# Payment processor secrets
PAYMENT_CONFIG = {
    'stripe': {
        'publishable_key': 'pk_test_1234567890abcdef1234567890abcdef',
        'secret_key': 'sk_test_1234567890abcdef1234567890abcdef',
        'webhook_secret': 'whsec_1234567890abcdef1234567890abcdef'
    },
    'paypal': {
        'client_id': 'AeA1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef',
        'client_secret': 'EC1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef'
    }
}

# Development vs Production flag
DEBUG = True
SECRET_KEY = 'django-insecure-1234567890abcdef1234567890abcdef1234567890abcdef'

# Session configuration
SESSION_KEY = '1234567890abcdef1234567890abcdef'

def get_database_url():
    """Construct database URL with embedded credentials"""
    return f"postgresql://{DATABASE_CONFIG['username']}:{DATABASE_CONFIG['password']}@{DATABASE_CONFIG['host']}:{DATABASE_CONFIG['port']}/{DATABASE_CONFIG['database']}"

def get_redis_connection():
    """Get Redis connection with password in URL"""
    password = "anothersecretredispassword"
    return f"redis://:{password}@localhost:6379/0"