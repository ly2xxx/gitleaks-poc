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
- Linux/macOS/Windows

### Step 1: Clone the Repository

```bash
git clone <your-repo-url>
cd gitleaks-poc
```

### Step 2: Install Python Dependencies

```bash
# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Step 3: Download and Install Gitleaks

The repository includes a pre-downloaded gitleaks binary for Linux, but you need to download the appropriate version for your operating system:

#### For Linux/macOS:
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

#### For Windows:
```powershell
# Option 1: Download using PowerShell
Invoke-WebRequest -Uri "https://github.com/gitleaks/gitleaks/releases/download/v8.27.2/gitleaks_8.27.2_windows_x64.zip" -OutFile "gitleaks_windows.zip"

# Extract the ZIP file
Expand-Archive -Path "gitleaks_windows.zip" -DestinationPath "." -Force

# Test the executable
.\gitleaks.exe version
```

```powershell
# Option 2: Using Chocolatey (if installed)
choco install gitleaks

# Option 3: Using Scoop (if installed)
scoop install gitleaks
```

**Note for Windows users**: You must use `.\gitleaks.exe` (not just `gitleaks`) to run the binary from the current directory. PowerShell doesn't execute programs from the current directory by default for security reasons.

### Step 4: Run the Demo Application

```bash
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`.

### Step 5: Scan for Secrets with Gitleaks

#### Linux/macOS:
```bash
# Basic scan of the current repository
./gitleaks detect --source . --verbose

# Generate a detailed report
./gitleaks detect --source . --report-format json --report-path gitleaks-report.json

# Scan specific files
./gitleaks detect --source . --verbose --log-opts="--all -- app.py config.py"
```

#### Windows:
```powershell
# Basic scan of the current repository
.\gitleaks.exe detect --source . --verbose

# Generate a detailed report
.\gitleaks.exe detect --source . --report-format json --report-path gitleaks-report.json

# Scan specific files
.\gitleaks.exe detect --source . --verbose --log-opts="--all -- app.py config.py"
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

#### Linux/macOS:
```bash
# Scan current directory
./gitleaks detect --source .

# Scan with verbose output
./gitleaks detect --source . --verbose

# Scan specific commit range
./gitleaks detect --source . --log-opts="--since='2024-01-01'"
```

#### Windows:
```powershell
# Scan current directory
.\gitleaks.exe detect --source .

# Scan with verbose output
.\gitleaks.exe detect --source . --verbose

# Scan specific commit range
.\gitleaks.exe detect --source . --log-opts="--since='2024-01-01'"
```

### Generate Reports

#### Linux/macOS:
```bash
# JSON report
./gitleaks detect --source . --report-format json --report-path report.json

# CSV report  
./gitleaks detect --source . --report-format csv --report-path report.csv

# SARIF report (for GitHub Security tab)
./gitleaks detect --source . --report-format sarif --report-path report.sarif
```

#### Windows:
```powershell
# JSON report
.\gitleaks.exe detect --source . --report-format json --report-path report.json

# CSV report  
.\gitleaks.exe detect --source . --report-format csv --report-path report.csv

# SARIF report (for GitHub Security tab)
.\gitleaks.exe detect --source . --report-format sarif --report-path report.sarif
```

### Configuration
```bash
# Use custom configuration (Linux/macOS)
./gitleaks detect --source . --config-path custom-gitleaks.toml

# Generate default config file (Linux/macOS)
./gitleaks generate config
```

```powershell
# Use custom configuration (Windows)
.\gitleaks.exe detect --source . --config-path custom-gitleaks.toml

# Generate default config file (Windows)
.\gitleaks.exe generate config
```

## 📈 Historical Commit Scanning

Use these commands to scan specific commit ranges, dates, or authors in your git history:

### Scan Specific Commit Range

#### Linux/macOS:
```bash
# Scan commits between two specific commits
./gitleaks detect --source . --log-opts="commit1..commit2"

# Scan last N commits
./gitleaks detect --source . --log-opts="-10"

# Scan commits since a specific date
./gitleaks detect --source . --log-opts="--since='2024-01-01'"

# Scan commits by author
./gitleaks detect --source . --log-opts="--author='username'"

# Scan commits from last week
./gitleaks detect --source . --log-opts="--since='1 week ago'"
```

#### Windows:
```powershell
# Scan commits between two specific commits
.\gitleaks.exe detect --source . --log-opts="commit1..commit2"

# Scan last N commits
.\gitleaks.exe detect --source . --log-opts="-10"

# Scan commits since a specific date
.\gitleaks.exe detect --source . --log-opts="--since='2024-01-01'"

# Scan commits by author
.\gitleaks.exe detect --source . --log-opts="--author='username'"

# Scan commits from last week
.\gitleaks.exe detect --source . --log-opts="--since='1 week ago'"
```

### Scan Branch Differences

#### Linux/macOS:
```bash
# Scan commits that are in feature-branch but not in main
./gitleaks detect --source . --log-opts="main..feature-branch"

# Scan uncommitted changes (staged and unstaged)
./gitleaks detect --source . --log-opts="--cached"

# Scan specific file history
./gitleaks detect --source . --log-opts="-- path/to/file.py"

# Scan merge commits only
./gitleaks detect --source . --log-opts="--merges"
```

#### Windows:
```powershell
# Scan commits that are in feature-branch but not in main
.\gitleaks.exe detect --source . --log-opts="main..feature-branch"

# Scan uncommitted changes (staged and unstaged)
.\gitleaks.exe detect --source . --log-opts="--cached"

# Scan specific file history
.\gitleaks.exe detect --source . --log-opts="-- path/to/file.py"

# Scan merge commits only
.\gitleaks.exe detect --source . --log-opts="--merges"
```

### Historical Scanning with Custom Configuration

#### Linux/macOS:
```bash
# Use custom config for historical scan
./gitleaks detect --config .gitleaks.toml --source . --log-opts="-20"

# Generate report for specific commit range
./gitleaks detect --config .gitleaks.toml --source . --log-opts="--since='2024-01-01'" --report-format json --report-path historical-report.json
```

#### Windows:
```powershell
# Use custom config for historical scan
.\gitleaks.exe detect --config .gitleaks.toml --source . --log-opts="-20"

# Generate report for specific commit range
.\gitleaks.exe detect --config .gitleaks.toml --source . --log-opts="--since='2024-01-01'" --report-format json --report-path historical-report.json
```

**Note**: The `--log-opts` parameter accepts any valid `git log` options, making it very flexible for targeting specific commit ranges or filtering criteria.

## 🔍 Current Codebase Scanning

Use the `protect` command to scan only the current working directory files (not git history):

### Basic Current File Scanning

#### Linux/macOS:
```bash
# Basic scan of current files
./gitleaks protect --source .

# Verbose output
./gitleaks protect --source . --verbose

# Scan specific directory
./gitleaks protect --source ./src

# With custom configuration
./gitleaks protect --config .gitleaks.toml --source .
```

#### Windows:
```powershell
# Basic scan of current files
.\gitleaks.exe protect --source .

# Verbose output
.\gitleaks.exe protect --source . --verbose

# Scan specific directory
.\gitleaks.exe protect --source ./src

# With custom configuration
.\gitleaks.exe protect --config .gitleaks.toml --source .
```

### Generate Reports for Current Files

#### Linux/macOS:
```bash
# Generate JSON report for current files
./gitleaks protect --source . --report-format json --report-path current-scan.json

# Generate CSV report for current files
./gitleaks protect --source . --report-format csv --report-path current-scan.csv

# Generate SARIF report for current files
./gitleaks protect --source . --report-format sarif --report-path current-scan.sarif
```

#### Windows:
```powershell
# Generate JSON report for current files
.\gitleaks.exe protect --source . --report-format json --report-path current-scan.json

# Generate CSV report for current files
.\gitleaks.exe protect --source . --report-format csv --report-path current-scan.csv

# Generate SARIF report for current files
.\gitleaks.exe protect --source . --report-format sarif --report-path current-scan.sarif
```

### CI/CD Integration

#### Linux/macOS:
```bash
# Exit with non-zero code if leaks found (useful for CI)
./gitleaks protect --source . --exit-code 1

# Scan and fail pipeline if secrets detected
./gitleaks protect --source . --verbose --exit-code 1
```

#### Windows:
```powershell
# Exit with non-zero code if leaks found (useful for CI)
.\gitleaks.exe protect --source . --exit-code 1

# Scan and fail pipeline if secrets detected
.\gitleaks.exe protect --source . --verbose --exit-code 1
```

### Key Differences Between Commands

**`gitleaks detect`** - Scans Git commit history (default behavior)
- Examines all commits in the repository
- Looks at historical changes and committed files
- Used for: Finding secrets that were previously committed

**`gitleaks protect`** - Scans current working directory files
- Examines only the current state of files
- Ignores Git history completely
- Used for: Pre-commit hooks, CI/CD pipelines, current code scanning
- Faster for large repositories as it doesn't process Git history

## 📁 Project Structure

```
gitleaks-poc/
├── app.py              # Main Streamlit application with embedded secrets
├── config.py           # Configuration file with various API keys and credentials
├── .env.example        # Environment file example with secrets
├── requirements.txt    # Python dependencies
├── gitleaks           # Gitleaks binary (Linux)
├── gitleaks.exe       # Gitleaks binary (Windows, after download)
├── chat.html          # Conversation history export
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
./gitleaks generate config      # Linux/macOS
.\gitleaks.exe generate config  # Windows

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
./gitleaks detect --source . --exit-code 1      # Linux/macOS
.\gitleaks.exe detect --source . --exit-code 1  # Windows
```

## 🐛 Common Issues & Solutions

### Windows PowerShell Issues

**Problem**: `gitleaks : The term 'gitleaks' is not recognized...`

**Solution**: Use `.\gitleaks.exe` instead of just `gitleaks`. PowerShell requires the `.\` prefix to execute binaries from the current directory.

**Problem**: Gitleaks opens a dialog asking which application to use

**Solution**: You downloaded the Linux binary instead of Windows. Download the Windows version using the PowerShell commands above.

### Permission Issues (Linux/macOS)

**Problem**: `Permission denied` when running `./gitleaks`

**Solution**: Make the binary executable:
```bash
chmod +x gitleaks
```

### Virtual Environment Issues

**Problem**: Module not found errors when running Streamlit

**Solution**: Ensure you're in the virtual environment:
```bash
# Windows
venv\Scripts\activate

# Linux/macOS  
source venv/bin/activate
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