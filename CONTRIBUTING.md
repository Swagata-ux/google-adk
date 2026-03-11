# Contributing to ADK Course Demo Projects

Thank you for your interest in contributing to the ADK Course Demo Projects!

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone <your-fork-url>`
3. Create a feature branch: `git checkout -b feature/your-feature-name`
4. Make your changes
5. Test your changes thoroughly
6. Commit with clear messages: `git commit -m "Add: feature description"`
7. Push to your fork: `git push origin feature/your-feature-name`
8. Open a Pull Request

## Development Setup

### Prerequisites
- Python 3.8 or higher
- Google Cloud account with GenAI API access
- Git

### Installation
```bash
# Clone the repository
git clone <repository-url>
cd google-adk

# Choose a project
cd hello-world  # or ticketpro

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env  # or helpdesk_agent/.env for ticketpro
# Edit .env and add your API key
```

## Code Standards

### Python Style
- Follow PEP 8 style guide
- Use type hints for function parameters and return values
- Write docstrings for all functions, classes, and modules
- Keep functions focused and concise

### Documentation
- Update README.md if adding new features
- Add inline comments for complex logic
- Include usage examples for new tools

### Testing
- Test all changes manually before submitting
- For ticketpro: Run `python verify_agent_flow.py`
- Ensure no regressions in existing functionality

## Security Guidelines

**Critical: Never commit sensitive information**

- Never commit API keys, tokens, or credentials
- Always use `.env` files for secrets (already in `.gitignore`)
- Review changes before committing: `git diff`
- If you accidentally commit secrets:
  1. Rotate the exposed credentials immediately
  2. Use `git-filter-repo` to remove from history
  3. Force push the cleaned history

## Project Structure

```
google-adk/
├── hello-world/          # Beginner project
│   ├── my_agent/        # Agent implementation
│   └── requirements.txt # Dependencies
├── ticketpro/           # Advanced project
│   ├── helpdesk_agent/  # Main agent
│   ├── tools/           # Tool implementations
│   ├── schemas/         # Data models
│   └── requirements.txt # Dependencies
└── .gitignore           # Git exclusions
```

## Pull Request Guidelines

### Before Submitting
- [ ] Code follows project style guidelines
- [ ] All tests pass
- [ ] Documentation is updated
- [ ] No sensitive information in commits
- [ ] Commit messages are clear and descriptive

### PR Description Should Include
- What changes were made and why
- How to test the changes
- Any breaking changes
- Related issues (if applicable)

## Reporting Issues

When reporting bugs or requesting features:

1. Check if the issue already exists
2. Use a clear, descriptive title
3. Provide detailed steps to reproduce (for bugs)
4. Include your environment details:
   - Python version
   - Operating system
   - ADK version
5. Add relevant code snippets or error messages

## Questions?

For questions about:
- **Google ADK**: See [official documentation](https://cloud.google.com/adk)
- **This project**: Open an issue with the `question` label
- **Course content**: Contact the course team

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for contributing to ADK Course Demo Projects!**
