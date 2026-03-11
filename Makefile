.PHONY: help install install-hello install-ticket test clean lint format

help:
	@echo "Available commands:"
	@echo "  make install        - Install all project dependencies"
	@echo "  make install-hello  - Install hello-world dependencies"
	@echo "  make install-ticket - Install ticketpro dependencies"
	@echo "  make test           - Run all tests"
	@echo "  make clean          - Remove cache and build files"
	@echo "  make lint           - Run code linting"
	@echo "  make format         - Format code with black"

install:
	pip install -r hello-world/requirements.txt
	pip install -r ticketpro/requirements.txt

install-hello:
	cd hello-world && pip install -r requirements.txt

install-ticket:
	cd ticketpro && pip install -r requirements.txt

test:
	cd ticketpro && python verify_agent_flow.py

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type d -name ".adk" -exec rm -rf {} +
	find . -type d -name "*.egg-info" -exec rm -rf {} +

lint:
	@echo "Install flake8 first: pip install flake8"
	flake8 hello-world/my_agent ticketpro --max-line-length=100 --exclude=.venv,__pycache__

format:
	@echo "Install black first: pip install black"
	black hello-world/my_agent ticketpro --line-length=100
