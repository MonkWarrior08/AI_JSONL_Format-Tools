## Overview

Welcome to the GPT-4 Prompt Template Tool! This is a GUI application designed using PyQt5 that helps you construct structured JSON format prompts with alternating roles for use in GPT-4 AI interactions. 

The tool enables users to quickly format prompts into a JSON structure that can be used for interactions with language models like GPT-4, allowing for a well-defined conversation flow between the system, user, and assistant.

## Features

- **Scrollable Interface**: Allows you to easily create and navigate through a sequence of messages.
- **Dynamic Text Boxes**: Begin with a default sequence of roles (system, user, assistant), and add new user or assistant prompts as needed.
- **Live JSON Formatting**: Updates and displays the JSON-formatted prompt as you type, enabling real-time visualization of your structured data.
- **Copy Functionality**: Copy the formatted JSON data to your clipboard with a simple click for easy integration into your projects.

## Requirements

- Python 3.x
- PyQt5

## Installation

1. Install Python 3.x from [Python's official website](https://www.python.org/).
2. Install PyQt5 using pip:

   ```bash
   pip install PyQt5
   ```
3. Clone this repository:

   ```bash
   git clone https://github.com/MonkWarrior08/Format_Tools.git
   cd Format_Tools
   ```
## Usage
Run the application:
```bash
python gpt4_prompt_template_tool.py
```
- The window will display with default roles [system, user, assistant] prompts. Enter your desired messages in each text box.
- Click the Add button to append new user or assistant prompts.
- The JSON format will dynamically update as you type your messages.
- Click Copy Format to copy the JSON structure to your clipboard.
