# Hello World Agent - ADK Course Demo

<!-- ![License](https://img.shields.io/badge/License-MIT-blue.svg) -->
<!-- ![Python](https://img.shields.io/badge/Python-3.14-blue.svg) -->
<!-- ![ADK](https://img.shields.io/badge/Google-ADK-4285F4.svg) -->

## Description

This is an introductory demonstration project for the **Google Agent Development Kit (ADK)** course. It showcases the fundamentals of creating an AI agent with simple tool-calling capabilities. The agent can respond to queries about weather and time in different cities using mock data.

**Learning Objectives:**
- Understand basic ADK agent structure
- Implement simple function tools
- Configure agent models and instructions
- Run basic agent queries

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8+** (tested with Python 3.14)
- **pip** package manager
- **Google Cloud account** with GenAI API access
- **Git** for cloning the repository

## Installation & Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd adkdemos/hello-world
```

### 2. Create Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install google-adk
```

### 4. Configuration

**⚠️ IMPORTANT: Configure your API credentials**

1. Copy the example environment file:
   ```bash
   cp .env.example my_agent/.env
   ```

2. Edit `my_agent/.env` and add your Google API key:
   ```
   GOOGLE_GENAI_USE_VERTEXAI=0
   GOOGLE_API_KEY=your_actual_api_key_here
   ```

3. **Obtain your API key:**
   - Visit [Google AI Studio](https://aistudio.google.com/apikey)
   - Create a new API key
   - **Never commit this key to version control**

## Usage

### Running the Agent

```python
from my_agent.agent import root_agent

# Query the agent
response = root_agent.query("What's the weather in San Francisco?")
print(response.answer)
```

### Example Interactions

```python
# Get current time
response = root_agent.query("What time is it in New York?")
# Output: "The current time in New York is 10:30 AM"

# Get weather information
response = root_agent.query("Tell me about the weather in Tokyo")
# Output: "The weather in Tokyo is Sunny and 75°F"
```

### Interactive Testing

```bash
python -m my_agent
```

## Project Structure

```
hello-world/
├── my_agent/
│   ├── __init__.py          # Module initialization
│   ├── agent.py             # Main agent definition with tools
│   └── .env                 # API credentials (git-ignored)
├── .env.example             # Environment variable template
├── .gitignore               # Files to exclude from git
└── README.md                # This file
```

### Key Files

- **`agent.py`** - Defines the `root_agent` with two mock tools:
  - `get_current_time(city)` - Returns mock time data
  - `get_current_weather(city)` - Returns mock weather data
- **`.env`** - Stores environment variables (API keys)

## Security Note

**⚠️ This repository contains demo code for educational purposes.**

**Important Security Practices:**
- Always ensure **no secrets or API keys are committed** to version control
- Use the provided `.gitignore` to exclude sensitive files
- Store credentials in environment variables (`.env` file)
- **Rotate your API keys** if accidentally exposed
- In production, use secret management systems (Google Secret Manager, HashiCorp Vault, etc.)

**Before making this repository public:**
1. Verify `.env` is listed in `.gitignore`
2. Check git history for accidentally committed secrets: `git log --all --full-history -- "*/.env"`
3. If secrets were committed, use tools like `git-filter-repo` to rewrite history

## Learning Resources

- [Google ADK Documentation](https://cloud.google.com/adk)
- [Agent Development Best Practices](https://cloud.google.com/adk/docs/best-practices)
- [Tool Calling Guide](https://cloud.google.com/adk/docs/tools)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

**Course:** Google Agent Development Kit (ADK) - Beginner Module
**Created:** 2024
**Maintained by:** ADK Course Team
