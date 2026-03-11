# Quick Start Guide

Get up and running with Google ADK demos in 5 minutes!

## 🚀 Fast Track Setup

### 1. Clone & Navigate
```bash
git clone <repository-url>
cd google-adk
```

### 2. Choose Your Path

#### 🟢 Beginner: Hello World
```bash
cd hello-world
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example my_agent/.env
# Edit my_agent/.env and add your API key
```

#### 🔵 Advanced: TicketPro
```bash
cd ticketpro
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example helpdesk_agent/.env
# Edit helpdesk_agent/.env and add your API key
```

### 3. Get Your API Key
1. Visit [Google AI Studio](https://aistudio.google.com/apikey)
2. Create a new API key
3. Add it to your `.env` file:
   ```
   GOOGLE_API_KEY=your_actual_api_key_here
   ```

### 4. Test It!

#### Hello World
```python
from my_agent.agent import root_agent

response = root_agent.query("What's the weather in Tokyo?")
print(response.answer)
```

#### TicketPro
```bash
python verify_agent_flow.py
```

## 📖 What's Next?

- Read the [full README](README.md) for detailed information
- Check [CONTRIBUTING.md](CONTRIBUTING.md) to contribute
- See [IMPROVEMENTS.md](IMPROVEMENTS.md) for recent changes
- Review [CHANGELOG.md](CHANGELOG.md) for version history

## 🆘 Common Issues

### Import Errors
```bash
pip install google-adk pydantic
```

### API Key Not Working
- Verify the key is correct in `.env`
- Check you're in the right directory
- Ensure `.env` file is in the correct location

### Virtual Environment Issues
```bash
deactivate  # Exit current venv
rm -rf .venv  # Remove old venv
python3 -m venv .venv  # Create new venv
source .venv/bin/activate  # Activate
pip install -r requirements.txt  # Reinstall
```

## 💡 Pro Tips

- Use `make install` to install all dependencies at once
- Use `make test` to run verification tests
- Use `make clean` to remove cache files
- Check `.env.example` for configuration options

## 🔒 Security Reminder

**Never commit your `.env` file or API keys to Git!**

The `.gitignore` is already configured to protect you, but always double-check before pushing.

---

**Ready to build agents? Let's go! 🚀**
