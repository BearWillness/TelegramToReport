# TelegramToReport

This Python program leverages OpenAI's GPT-3.5 Turbo model to assist with tasks related to message extraction, bullet point generation, and detailed report creation. The program is structured using Object-Oriented Programming (OOP) principles.

## Prerequisites

- Python 3.x
- OpenAI GPT-3.5 Turbo API Key

## Setup

1. Install the required dependencies:

   ```bash
   pip install beautifulsoup4 openai
  ```
```
2. Replace `'your_openai_api_key'` in the code with your actual OpenAI GPT API key.

## Usage

### 1. Message Extraction

Extract messages from an HTML file and store them in a text file:

  ```bash
  python main.py extract_messages messages.html extracted_messages.txt
```

### 2. Bullet Point Generation

Generate bullet points from extracted messages:

  ```bash
  python main.py generate_bullet_points extracted_messages.txt
```

### 3. Detailed Report Generation

Generate a detailed report on a given topic:

  ```bash
  python main.py generate_detailed_report items.txt detailed_report_output
```

## Class Structure

The program is organized into an `Assistant` class with methods for message extraction, bullet point generation, and detailed report creation. The class encapsulates the OpenAI API key and system message.

## Contributing

Feel free to contribute by opening issues or submitting pull requests.

