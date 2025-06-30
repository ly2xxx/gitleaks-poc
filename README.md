# 🔍 Gitleaks Demo Application

A demonstration application showcasing **Gitleaks** - a SAST (Static Application Security Testing) tool that detects secrets, passwords, and sensitive information in git repositories.

This project contains a simple Streamlit web application with **intentionally embedded fake secrets** to demonstrate how Gitleaks can identify various types of sensitive data in source code.

## 🎯 Purpose

This demo helps developers and security teams:
- Learn how to use Gitleaks for secret detection
- Understand different types of secrets that Gitleaks can identify
- Practice integrating secret scanning into CI/CD pipelines
- See real examples of how secrets are accidentally committed to repositories

⚠️ **Important**: All secrets in this repository are **fake and for demo purposes only**. They should never be used in production systems.

## 🚀 Quick Start

### Prerequisites

- Python 3.8+ 
- Git
- Linux/macOS (Windows users can use WSL)

### Step 1: Clone the Repository

```bash
git clone <your-repo-url>
cd gitleaks-poc
```

### Step 2: Install Python Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Download and Install Gitleaks

The repository includes a pre-downloaded gitleaks binary, but you can also download the latest version:

```bash
# Download latest gitleaks (Linux x64)
curl -s https://api.github.com/repos/gitleaks/gitleaks/releases/latest | \
  grep "browser_download_url.*linux_x64.tar.gz" | \
  cut -d '"' -f 4 | \
  wget -qi -

# Extract the binary
tar -xzf gitleaks_*.tar.gz

# Make it executable
chmod +x gitleaks

# Test installation
./gitleaks version
```

### Step 4: Run the Demo Application

```bash
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`.

### Step 5: Scan for Secrets with Gitleaks

```bash
# Basic scan of the current repository
./gitleaks detect --source . --verbose

# Generate a detailed report
./gitleaks detect --source . --report-format json --report-path gitleaks-report.json

# Scan specific files
./gitleaks detect --source . --verbose --log-opts="--all -- app.py config.py"
```

## 📊 Expected Results

When you run Gitleaks on this repository, you should see approximately **30+ detected secrets** including:

- **API Keys**: AWS, Stripe, SendGrid, OpenAI, etc.
- **Database Passwords**: PostgreSQL, MongoDB, Redis
- **OAuth Credentials**: Google, Facebook, Twitter
- **Webhook URLs**: Slack, Discord, Teams
- **JWT Secrets and Encryption Keys**
- **Private Keys and Certificates**
- **GitHub Personal Access Tokens**

### Sample Detection Output

```
Finding:     AWS_ACCESS_KEY_ID="AKIAIOSFODNN7EXAMPLE"
Secret:      AKIAIOSFODNN7EXAMPLE
RuleID:      aws-access-token
File:        app.py
Line:        12
```

## 🛠️ Available Gitleaks Commands

### Basic Detection
```bash
# Scan current directory
./gitleaks detect --source .

# Scan with verbose output
./gitleaks detect --source . --verbose

# Scan specific commit range
./gitleaks detect --source . --log-opts="--since='2024-01-01'"
```

### Generate Reports
```bash
# JSON report
./gitleaks detect --source . --report-format json --report-path report.json

# CSV report  
./gitleaks detect --source . --report-format csv --report-path report.csv

# SARIF report (for GitHub Security tab)
./gitleaks detect --source . --report-format sarif --report-path report.sarif
```

### Configuration
```bash
# Use custom configuration
./gitleaks detect --source . --config-path custom-gitleaks.toml

# Generate default config file
./gitleaks generate config
```

## 📁 Project Structure

```
gitleaks-poc/
├── app.py              # Main Streamlit application with embedded secrets
├── config.py           # Configuration file with various API keys and credentials
├── .env.example        # Environment file example with secrets
├── requirements.txt    # Python dependencies
├── gitleaks           # Gitleaks binary
├── README.md          # This file
└── reports/           # Generated scan reports (created after running scans)
```

## 🧪 Demo Application Features

The Streamlit application includes:

1. **Dashboard**: Overview with fake metrics
2. **API Testing**: Simulated connections to AWS, Stripe, GitHub
3. **Database Operations**: Mock database operations with hardcoded credentials
4. **Configuration**: Display of environment variables and settings

### Types of Secrets Included

- **Cloud Provider Keys**: AWS Access Keys, Azure Client Secrets, GCP Service Account Keys
- **Payment Processors**: Stripe Keys, PayPal Client Secrets
- **Communication APIs**: Slack Webhooks, Discord Webhooks, Twilio Tokens
- **Development Tools**: GitHub Tokens, API Keys
- **Database Credentials**: Connection strings with embedded passwords
- **Encryption Keys**: JWT secrets, Fernet keys, session keys

## 🔧 Customizing the Demo

### Adding New Secret Types

1. Edit `app.py` or `config.py` to add new fake secrets
2. Ensure they follow realistic patterns (e.g., AWS keys start with `AKIA`)
3. Commit the changes: `git add . && git commit -m "Add new secrets"`
4. Run Gitleaks scan to verify detection

### Creating Custom Gitleaks Rules

```bash
# Generate a base configuration
./gitleaks generate config

# Edit the generated .gitleaks.toml file to add custom rules
# Example custom rule for your organization's API keys:
[[rules]]
id = "company-api-key"
description = "Company API Key"
regex = '''(?i)company[_-]?api[_-]?key['":\s=]*[a-f0-9]{32}'''
keywords = ["company_api_key", "company-api-key"]
```

## 🚨 Integration Examples

### GitHub Actions

Create `.github/workflows/gitleaks.yml`:

```yaml
name: gitleaks
on: [push, pull_request]
jobs:
  scan:
    name: gitleaks
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0
      - uses: gitleaks/gitleaks-action@v2
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

### Pre-commit Hook

```bash
# Install pre-commit
pip install pre-commit

# Create .pre-commit-config.yaml
cat > .pre-commit-config.yaml << EOF
repos:
  - repo: https://github.com/gitleaks/gitleaks
    rev: v8.18.0
    hooks:
      - id: gitleaks
EOF

# Install the hook
pre-commit install
```

### CI/CD Pipeline Integration

```bash
# In your CI/CD pipeline
./gitleaks detect --source . --exit-code 1
```

## 📚 Learning Resources

- [Gitleaks Official Documentation](https://github.com/gitleaks/gitleaks)
- [OWASP Secret Management Guide](https://owasp.org/www-community/controls/SecretManagement)
- [GitHub Secret Scanning](https://docs.github.com/en/code-security/secret-scanning)

## 🛡️ Best Practices

1. **Never commit real secrets** - Use environment variables or secret management systems
2. **Scan regularly** - Integrate Gitleaks into your CI/CD pipeline
3. **Use .gitignore** - Prevent sensitive files from being committed
4. **Rotate exposed secrets** - If secrets are accidentally committed, rotate them immediately
5. **Educate your team** - Regular training on secure coding practices

## 🔍 Troubleshooting

### Gitleaks Not Finding Secrets
- Ensure files are committed to git (Gitleaks scans git history)
- Check if secrets match known patterns in the default ruleset
- Try verbose mode: `./gitleaks detect --source . --verbose`

### Performance Issues
- For large repositories, use `--max-target-megabytes` to limit scan size
- Scan specific paths: `./gitleaks detect --source ./src`

### False Positives
- Create a `.gitleaksignore` file to exclude specific findings
- Customize rules in `.gitleaks.toml` configuration

## 📝 License

This project is for educational and demonstration purposes. See LICENSE file for details.

---

**⚠️ Disclaimer**: This repository contains fake secrets for demonstration purposes only. Never use these credentials in production systems. Always follow security best practices when handling real sensitive data.