# CampusFlow AI Ticket Assistant

## About the Project
CampusFlow is a Python command-line application that allows students to create support tickets for campus-related problems.

## Features
- Create support tickets.
- Generate a unique ID for each ticket.
- Save tickets in a JSON file.
- Request AI troubleshooting suggestions.

## Requirements
- Python 3
- The `openai` package
- The `python-dotenv` package

## How to Run
1. Open a terminal in the project folder.
2. Activate the virtual environment:

   `source .venv/bin/activate`

3. Install dependencies if needed:

   `python3 -m pip install openai python-dotenv`

4. Run the application:

   `python3 tickets.py`

## AI Configuration
The application uses OpenRouter for AI suggestions. A valid API key must be configured locally in a `.env` file. Never upload API keys to GitHub.

## Project Files
- `tickets.py` — main ticket application.
- `ai_helper.py` — AI integration.
- `tickets.json` — saved tickets.
- `.gitignore` — excludes files that should not be committed.