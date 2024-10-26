# IS601-midterm

## Introduction Video
[![Project Overview Video]](https://youtu.be/PRXJG9NbGaA)

## Table of Contents
- [Project Overview](#project-overview)
- [Setup Instructions](#setup-instructions)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Architectural Decisions](#architectural-decisions)
  - [Design Patterns](#design-patterns)
  - [Logging Strategy](#logging-strategy)
  - [Configuration with dotenv](#configuration-with-dotenv)
---

## Project Overview
*Thie project designed to underscore the importance of professional software development practices, the application integrates clean, maintainable code, the application of design patterns, comprehensive logging, dynamic configuration via environment variables, sophisticated data handling with Pandas, and a command-line interface (REPL) for real-time user interaction.*

## Setup Instructions

### Prerequisites
- **Python 3.8+**
- **pip** for managing Python packages
- **Git** for version control
- **Virtual Environment** (recommended) to isolate dependencies

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/jincheng411/IS601-midterm.gist
2. Set up and activate a virtual environment:
    ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. Install dependencies:
    ```bash
   pip install -r requirements.txt
    
## Architectural Decisions
### Design Patterns
*This project adopts several design patterns to enhance modularity, maintainability, and scalability.*

1. Command Pattern:

*Implementation: Each command is encapsulated in its own class, inheriting from a Command interface with an execute method. Commands are registered and managed by a CommandHandler class, which maps command strings to their respective classes.
Impact: By isolating commands into separate classes, adding new commands becomes straightforward without modifying existing code, enhancing extensibility.*

For details on the `command pattern` implementation, see [command pattern in `__init__.py`](https://github.com/jincheng411/IS601-midterm/blob/master/app/commands/__init__.py).

2. lugin Pattern:

*Implementation: Commands are dynamically loaded as plugins using importlib and pkgutil. Each plugin can be registered automatically in load_plugins, making it easy to integrate additional functionality.
Impact: This allows for a modular approach where new features can be added as plugins rather than hardcoded in the application, encouraging separation of concerns.*

3. Factory Pattern:

*Implementation: A CalculationFactory could be introduced to instantiate Calculation objects based on different operations (e.g., addition, subtraction).
Impact: This makes the code more scalable, as new calculation types can be added by updating the factory without changing the rest of the codebase.*

## Logging Strategy
*The logging strategy is designed for flexible, level-based logging that can be configured via environment variables, with separate configurations for development and production.*

1. Configuration:

Environment-Driven: Log levels (DEBUG, INFO, WARNING, ERROR, CRITICAL) are configured through environment variables. This enables different logging verbosity between development and production environments.
Output Destination: Logs can be directed to both console and file, with the file path defined by the LOG_FILE_PATH variable.

2. Implementation:

Log Levels:
*INFO: General operational messages, e.g., “Command executed successfully.”*
*WARNING: Issues that don’t stop the application but may need attention, e.g., “Deprecated command used.”*
*ERROR: Operational failures, e.g., “Failed to load plugin.”*
*Rotation and Retention (if applicable): In production, a log rotation strategy may be implemented to manage log sizes.*
3. Impact:
*Effective monitoring through differentiated logging levels helps in quickly identifying critical issues without cluttering logs with general operational information. Configurable log levels ensure flexibility in troubleshooting and tracking during development and production.*

## Using the REPL
The application includes a REPL (Read-Eval-Print Loop) interface, which allows you to interact with it in real-time. This REPL is especially useful for testing commands and experimenting with the app's functionality.

Start the REPL:
    ```
    
    python main.py
Available Commands: When prompted, enter any available command (see below) and press Enter.
    ```
    
    -----------Menu:-----------
    add <num1> <num2>
    subtract <num1> <num2>
    multiply <num1> <num2>
    divide <num1> <num2>
    loadHistory
    deleteHistory <line number>
    clearHistory
Exit the REPL: Type exit to terminate the REPL session.
This interactive shell provides immediate feedback, helping with command validation and troubleshooting.

## configuration-with-dotenv
Configuration with dotenv
This application uses python-dotenv to manage environment variables. You can define environment variables in a .env file to configure the application.

Create a .env file:

    ```
    LOG_LEVEL=INFO
    LOG_FILE=log/app.log
    CSV_FILE_PATH="./calculations.csv"

The application will automatically load the environment variables from this .env file, allowing you to configure settings like logging paths and database URLs without hardcoding them in the code.

GitHub Actions Environment Variables:

Store any sensitive information, like API keys or passwords, in GitHub Actions Secrets.
Define non-sensitive variables directly in the .env file or the GitHub Actions workflow file for ease of configuration in CI/CD.




