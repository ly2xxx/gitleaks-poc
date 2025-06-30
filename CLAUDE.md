# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

### Running the application
- `streamlit run app.py` - Start the Streamlit web application
- Debug configuration exists in `.vscode/launch.json` for running with debugger

### Dependencies
- Install dependencies: `pip install -r requirements.txt`
- Main dependencies: streamlit, pandas, requests

### Gitleaks Secret Scanning
- Linux/macOS: `./gitleaks detect --source . --verbose`
- Windows: `.\gitleaks.exe detect --source . --verbose`
- Generate JSON report: `./gitleaks detect --source . --report-format json --report-path gitleaks-report.json`
- Generate CSV report: `./gitleaks detect --source . --report-format csv --report-path report.csv`

## Architecture Overview

This is a **Gitleaks demonstration repository** designed to showcase secret detection capabilities. The project contains intentionally embedded fake secrets for educational and testing purposes.

### Core Components

**Demo Application (`app.py`)**:
- Single-file Streamlit app demonstrating various secret exposure patterns
- Contains hardcoded API keys, database credentials, JWT secrets, and webhook URLs
- Four-tab interface: Dashboard, API Testing, Database Operations, Configuration
- Uses fake secrets that follow real-world patterns (AWS keys start with AKIA, etc.)

**Configuration Files**:
- `config.py` - Comprehensive configuration file with various secret types
- `.env.example` - Environment file with common secret patterns
- Both files contain intentionally exposed credentials for demo purposes

**Secret Detection Setup**:
- Gitleaks binaries included for Linux (`gitleaks`) and Windows (`gitleaks.exe`)
- Pre-generated reports available as examples
- Repository contains 30+ different types of secrets across multiple files

### Key Technical Details

- All secrets are **fake and safe for demonstration**
- Secrets follow realistic patterns to trigger Gitleaks detection rules
- Application simulates real-world scenarios where secrets are accidentally committed
- No actual external connections are made; all operations are simulated
- Designed for security training, CI/CD testing, and Gitleaks rule development

### Secret Categories Included
- Cloud provider credentials (AWS, Azure, GCP)
- Payment processor keys (Stripe, PayPal)
- Communication APIs (Slack, Discord, Teams webhooks)
- Database connection strings with embedded passwords
- OAuth credentials and API tokens
- Encryption keys and JWT secrets

### Platform Considerations
- Windows users must use `.\gitleaks.exe` (PowerShell security requirement)
- Linux/macOS users can use `./gitleaks`
- Virtual environment recommended for Python dependencies
- Repository works on all major platforms with appropriate binary