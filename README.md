# Mac AI Voice Assistant with OpenAI Integration

This repository contains the source code for a voice assistant program called "Mac AI". The program is built using Python and leverages various libraries and APIs for speech recognition, natural language processing, web automation, and integration with the OpenAI API.

## Features

- Voice Recognition: Utilizes the `speech_recognition` library to convert speech input into text commands.
- OpenAI Integration: Integrates with the OpenAI API to generate AI responses based on user queries and prompts.
- Web Automation: Opens websites based on user commands using the `webbrowser` module.
- Time Announcement: Provides the current time upon user request using the `datetime` module.
- Application Launch: Opens specified applications like FaceTime and Passky using system commands.
- Chatting Capability: Engages in a conversation with the user, responding to general queries and maintaining a conversation history.

## Dependencies

- `speech_recognition`: Library for speech recognition.
- `openai`: Python client for the OpenAI API.
- `webbrowser`: Module for web browser automation.
- `datetime`: Module for working with dates and times.

## Usage

1. Install the required dependencies using `pip` or your preferred package manager.
2. Obtain an API key from OpenAI and add it to the `config.py` file.
3. Run the `main.py` script to start the Mac AI voice assistant.
4. Speak commands and interact with the assistant using voice input.
5. The assistant can open websites, announce the time, launch applications, engage in conversation, and more.
6. Additionally, you can use the OpenAI integration to generate AI responses for specific prompts by calling the appropriate functions.

## Code Examples

The repository includes code examples that demonstrate different functionalities:

1. `main.py`: The main script that runs the Mac AI voice assistant with speech recognition and various features.
2. `openai_integration.py`: A code snippet that showcases how to integrate with the OpenAI API to generate AI responses for specific prompts.
