#!/usr/bin/env python3
"""
Gitleaks Demo Application
A simple Streamlit app with intentionally embedded secrets for demonstration purposes.
"""

import streamlit as st
import pandas as pd
import requests
import sqlite3
import os
from datetime import datetime

# SECURITY ISSUE: Hardcoded API keys (these are fake for demo purposes)
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
STRIPE_SECRET_KEY = "sk_test_51H7JjqHnLJRGQKhJrKKuYrQX4qLNGLGBBNGJKnLJRGQ"
GITHUB_TOKEN = "ghp_1234567890abcdef1234567890abcdef12345678"

# Database connection with hardcoded password
DB_CONNECTION_STRING = "postgresql://admin:supersecretpassword123@localhost:5432/myapp"

# Slack webhook URL
SLACK_WEBHOOK = "https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX"

# JWT secret
JWT_SECRET = "my-super-secret-jwt-key-that-should-not-be-in-code"

class DatabaseManager:
    def __init__(self):
        # Another hardcoded credential
        self.api_key = "aaaabbbbccccdddd1111222233334444"
        self.connection = None
    
    def connect(self):
        # Simulated database connection
        password = "admin123"  # SECURITY ISSUE: Hardcoded password
        username = "dbuser"
        host = "production-db.company.com"
        
        st.write(f"Connecting to database at {host} with user {username}")
        return True

def send_notification(message):
    """Send notification to Slack"""
    webhook_url = "https://hooks.slack.com/services/T12345/B12345/abcdef123456789"
    
    payload = {
        "text": message,
        "username": "demo-bot"
    }
    
    # This would normally make a real request
    st.write(f"Would send notification: {message}")

def main():
    st.title("🔍 Gitleaks Demo Application")
    st.write("This application contains various types of secrets that gitleaks should detect.")
    
    # Create tabs for different features
    tab1, tab2, tab3, tab4 = st.tabs(["Dashboard", "API Testing", "Database", "Configuration"])
    
    with tab1:
        st.header("Application Dashboard")
        st.write("Welcome to the demo application!")
        
        # Display some fake metrics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Active Users", "1,234")
        with col2:
            st.metric("API Calls", "56,789")
        with col3:
            st.metric("Errors", "12")
        
        # Show current time
        st.write(f"Current time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    with tab2:
        st.header("API Testing")
        
        # AWS S3 simulation
        if st.button("Test AWS S3 Connection"):
            # Using the hardcoded credentials
            st.write(f"Testing AWS connection with key: {AWS_ACCESS_KEY_ID[:10]}...")
            st.success("✅ AWS S3 connection test completed!")
        
        # Stripe payment simulation
        if st.button("Test Stripe Payment"):
            st.write(f"Using Stripe key: {STRIPE_SECRET_KEY[:15]}...")
            st.success("✅ Stripe payment test completed!")
        
        # GitHub API simulation
        if st.button("Test GitHub API"):
            st.write(f"Using GitHub token: {GITHUB_TOKEN[:15]}...")
            st.success("✅ GitHub API test completed!")
    
    with tab3:
        st.header("Database Operations")
        
        db_manager = DatabaseManager()
        
        if st.button("Connect to Database"):
            if db_manager.connect():
                st.success("✅ Database connected successfully!")
        
        # Show connection string (partially masked)
        st.write(f"Connection: {DB_CONNECTION_STRING.split('@')[1] if '@' in DB_CONNECTION_STRING else 'localhost'}")
        
        # Simulate some database operations
        if st.button("Run Query"):
            st.code("""
            SELECT * FROM users 
            WHERE api_key = 'aaaabbbbccccdddd1111222233334444'
            LIMIT 10;
            """)
            st.write("Query executed successfully!")
    
    with tab4:
        st.header("Configuration")
        
        st.subheader("Environment Variables")
        
        # Display some fake environment info
        env_vars = {
            "APP_ENV": "development",
            "DEBUG": "true",
            "JWT_SECRET": JWT_SECRET[:10] + "...",
            "API_KEY": db_manager.api_key[:8] + "...",
        }
        
        for key, value in env_vars.items():
            st.write(f"**{key}**: `{value}`")
        
        if st.button("Send Test Notification"):
            send_notification("Test notification from Gitleaks demo app!")
        
        st.subheader("Application Info")
        st.json({
            "version": "1.0.0",
            "build": "demo-build-123",
            "environment": "development"
        })

if __name__ == "__main__":
    # More hardcoded secrets in different formats
    MAILGUN_API_KEY = "key-1234567890abcdef1234567890abcdef"
    TWILIO_AUTH_TOKEN = "AC1234567890abcdef1234567890abcdef12"
    
    # Private key (fake RSA private key for demo)
    PRIVATE_KEY = """-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA1234567890abcdef1234567890abcdef1234567890abcdef
1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef
1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef
-----END RSA PRIVATE KEY-----"""
    
    main()