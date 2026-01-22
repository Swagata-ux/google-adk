# TicketPro - IT Helpdesk Agent - ADK Course Demo

<!-- ![License](https://img.shields.io/badge/License-MIT-blue.svg) -->
<!-- ![Python](https://img.shields.io/badge/Python-3.14-blue.svg) -->
<!-- ![ADK](https://img.shields.io/badge/Google-ADK-4285F4.svg) -->

## Description

**TicketPro** is an advanced demonstration project for the **Google Agent Development Kit (ADK)** course. It implements a sophisticated IT helpdesk agent that handles common IT support scenarios through multi-turn conversations, tool orchestration, and intelligent decision-making.

**Learning Objectives:**
- Build complex multi-tool agents with sophisticated workflows
- Implement structured data models with Pydantic
- Design conversational flows with context management
- Create and run evaluation test suites
- Handle errors gracefully in agent tools
- Follow best practices for agent instructions and prompt engineering

**Key Features:**
- **User Account Management** - Look up users and check account status
- **Service Status Monitoring** - Check operational status of IT services (email, VPN, GitLab, Wi-Fi)
- **Ticket Creation** - Generate structured helpdesk tickets with proper approval flows
- **Multi-Turn Conversations** - Context-aware dialogue across multiple exchanges
- **Evaluation Framework** - Automated testing with ADK evaluation tools

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
cd adkdemos/ticketpro
```

### 2. Create Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install google-adk pydantic
```

### 4. Configuration

**⚠️ IMPORTANT: Configure your API credentials**

1. Copy the example environment file:
   ```bash
   cp .env.example helpdesk_agent/.env
   ```

2. Edit `helpdesk_agent/.env` and add your Google API key:
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
from helpdesk_agent.agent import root_agent

# Query the helpdesk agent
response = root_agent.query("My email is not working. My address is alice@example.com")
print(response.answer)
```

### Example Interactions

```python
# Locked Account Scenario
response = root_agent.query(
    "My email says my account is locked. My email is carol@example.com"
)
# Agent will:
# 1. Call lookup_user tool
# 2. Detect locked status
# 3. Ask if user wants to create a ticket

# VPN Outage Scenario
response = root_agent.query(
    "My whole team can't use VPN this morning. We're all blocked."
)
# Agent will:
# 1. Call check_service_status tool
# 2. Report degraded/outage status
# 3. Suggest creating a ticket
```

### Manual Testing

Run the verification script to test agent behavior:

```bash
python verify_agent_flow.py
```

This tests:
- Locked account detection (user: carol@example.com)
- VPN outage handling (degraded service)
- Proper "ask before creating ticket" flow

### Running Evaluations

Run the automated evaluation suite:

```bash
cd helpdesk_agent
adk eval run helpdesk_core_flows.evalset.json
```

View evaluation results:
```bash
ls .adk/eval_history/
```

### Inspecting the Agent

```bash
python inspect_agent.py
```

## Project Structure

```
ticketpro/
├── helpdesk_agent/           # Main agent package
│   ├── agent.py              # Agent definition with instructions
│   ├── __init__.py           # Module initialization
│   ├── .env                  # API credentials (git-ignored)
│   ├── helpdesk_core_flows.evalset.json  # Evaluation test cases
│   ├── evals/                # Evaluation configurations
│   └── .adk/                 # ADK evaluation artifacts (git-ignored)
│       └── eval_history/     # Test run results
├── tools/                    # Tool implementations
│   ├── __init__.py
│   └── helpdesk_tools.py     # User lookup, service status, ticket creation
├── schemas/                  # Data models
│   ├── __init__.py
│   └── ticket.py             # Pydantic Ticket model
├── inspect_agent.py          # Agent introspection utility
├── verify_agent_flow.py      # Manual flow testing script
├── .env.example              # Environment variable template
├── .gitignore                # Files to exclude from git
└── README.md                 # This file
```

### Key Components

#### **Agent Definition** (`helpdesk_agent/agent.py`)
- Comprehensive 114-line instruction prompt with decision trees
- Tool orchestration logic
- Multi-turn conversation handling

#### **Tools** (`tools/helpdesk_tools.py`)
- **`lookup_user_impl(email)`** - Queries fake user directory
- **`check_service_status_impl(service_name)`** - Checks service health
- **`create_ticket_impl(args)`** - Creates structured IT tickets

#### **Data Models** (`schemas/ticket.py`)
- **`Ticket`** - Pydantic model with fields:
  - `ticket_id`, `summary`, `service`, `user_email`
  - `severity` (low/medium/high)
  - `status` (open/in_progress/resolved)
  - `department`, `created_at`

#### **Mock Data** (`tools/helpdesk_tools.py`)
```python
# Fake user directory (for testing)
alice@example.com   - Active user (Engineering)
bob@example.com     - Active user (Finance)
carol@example.com   - Locked account (HR)

# Fake service status
email    - operational
vpn      - degraded
gitlab   - outage
wifi     - operational
```

## Agent Behavior

### Troubleshooting Flow

The agent follows this decision tree:

1. **Clarify the Problem** - Ask about affected service and symptoms
2. **Gather Details** - Request user email if account-specific
3. **Use Tools Strategically**:
   - `lookup_user` for account-specific issues
   - `check_service_status` for service health checks
4. **Ticket Creation Approval**:
   - **ALWAYS ask before creating tickets**
   - Only create after explicit user confirmation
5. **Provide Next Steps** - Give numbered troubleshooting steps

### Error Handling

All tools return structured responses:
```json
{
  "status": "success" | "error",
  "error_message": "explanation if error",
  // ... tool-specific fields
}
```

The agent handles:
- Unknown users gracefully
- Invalid service names with suggestions
- Tool exceptions without crashing

## Testing & Evaluation

### Test Cases Included

1. **Locked Account Detection** (`casee4c486`)
   - Input: User reports locked account
   - Expected: Agent calls `lookup_user`, confirms lock, asks about ticket

2. **VPN Outage Handling** (`casef6b2f7`)
   - Input: Team-wide VPN issues
   - Expected: Agent calls `check_service_status`, reports degradation

### Evaluation Metrics

- Tool call accuracy
- Response quality
- Adherence to "ask before ticket" policy

## Security Note

**⚠️ This repository contains demo code for educational purposes.**

**Important Security Practices:**
- Always ensure **no secrets or API keys are committed** to version control
- Use the provided `.gitignore` to exclude `.env` files
- Store credentials in environment variables
- **Rotate your API keys** if accidentally exposed
- Mock data (user directory, service status) is for **demo purposes only**
- In production:
  - Use real authentication systems
  - Implement proper authorization checks
  - Encrypt sensitive data at rest and in transit
  - Use secret management systems (Google Secret Manager, etc.)

**Before making this repository public:**
1. Verify `.env` is listed in `.gitignore`
2. Check git history: `git log --all --full-history -- "*/.env"`
3. Remove any committed secrets with `git-filter-repo`
4. Rotate all exposed API keys immediately

## Advanced Topics Demonstrated

- **Pydantic Validation** - Type-safe data models with `BaseModel`
- **Type Hints** - Extensive use of `Dict`, `Literal`, `Optional`
- **Error Recovery** - Try/except blocks with user-friendly messages
- **Prompt Engineering** - 114-line structured instruction set
- **Tool Design Patterns** - Consistent response structures
- **Conversation Memory** - ADK automatic history management
- **Evaluation-Driven Development** - Test cases in JSON format

## Learning Resources

- [Google ADK Documentation](https://cloud.google.com/adk)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Agent Tool Design Best Practices](https://cloud.google.com/adk/docs/tools)
- [Evaluation Framework Guide](https://cloud.google.com/adk/docs/evaluation)

## Troubleshooting

### Common Issues

**ImportError: No module named 'google.adk'**
```bash
pip install google-adk
```

**API Key errors**
- Verify `.env` file exists in `helpdesk_agent/`
- Check API key is valid in Google Cloud Console
- Ensure `GOOGLE_API_KEY` environment variable is set

**Tool execution failures**
- Check tool function signatures match `FunctionTool` expectations
- Verify Pydantic models are properly defined
- Review agent logs for detailed error messages

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

**Course:** Google Agent Development Kit (ADK) - Advanced Module
**Created:** 2024
**Maintained by:** ADK Course Team
**Demo Purpose:** Educational use only - not for production deployment
