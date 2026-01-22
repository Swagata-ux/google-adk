# ADK Course Demo Projects

A collection of demonstration projects for our Kodekloud course on the **Google Agent Development Kit (ADK)**. 

These projects showcase agent development patterns from basic to advanced implementations.

## Projects

### 1. [hello-world](./hello-world/)
**Beginner Level** - Introduction to ADK agent basics

A minimal "Hello World" agent demonstrating:
- Basic agent structure
- Simple function tools
- Model configuration
- Basic queries

Perfect for getting started with ADK development.

### 2. [ticketpro](./ticketpro/)
**Advanced Level** - IT Helpdesk Agent

A sophisticated helpdesk agent showcasing:
- Multi-tool orchestration
- Structured data models (Pydantic)
- Multi-turn conversations
- Evaluation testing
- Error handling patterns
- Complex agent instructions

Demonstrates production-ready patterns for real-world applications.

## Quick Start

### Prerequisites

- Python 3.8 or higher
- Google Cloud account with GenAI API access
- Git

### Setup

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd adkdemos
   ```

2. **Choose a project:**
   ```bash
   # For beginners
   cd hello-world

   # For advanced users
   cd ticketpro
   ```

3. **Follow the project-specific README** for detailed setup instructions

## Repository Structure

```
adkdemos/
├── hello-world/              # Beginner: Basic agent demo
│   ├── my_agent/            # Agent implementation
│   ├── .env.example         # Environment template
│   └── README.md            # Project documentation
├── ticketpro/               # Advanced: Helpdesk agent
│   ├── helpdesk_agent/      # Main agent package
│   ├── tools/               # Tool implementations
│   ├── schemas/             # Data models
│   ├── .env.example         # Environment template
│   └── README.md            # Project documentation
├── .gitignore               # Git exclusions
├── LICENSE                  # MIT License
└── README.md                # This file
```

## Security

**⚠️ Important:** These are educational demo projects.

- **Never commit API keys** to version control
- Use `.env.example` as a template and create your own `.env` files
- The `.gitignore` is configured to protect sensitive files
- Always rotate API keys if accidentally exposed

See individual project READMEs for detailed security practices.

## Learning Path

**Recommended Order:**

1. **Start with hello-world** to understand:
   - Basic agent creation
   - Tool definition
   - Simple queries

2. **Progress to ticketpro** to learn:
   - Complex agent instructions
   - Multi-tool coordination
   - Data validation
   - Testing and evaluation

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Resources

- [Google ADK Documentation](https://cloud.google.com/adk)
- [ADK API Reference](https://cloud.google.com/adk/docs/reference)
- [Agent Development Best Practices](https://cloud.google.com/adk/docs/best-practices)

## Support

These are educational demonstration projects. For production use:
- Review Google ADK production guidelines
- Implement proper secret management
- Add comprehensive error handling
- Set up monitoring and logging

---

**Course:** Google Agent Development Kit (ADK)
**Purpose:** Educational demonstrations
**Maintained by:** ADK Course Team
