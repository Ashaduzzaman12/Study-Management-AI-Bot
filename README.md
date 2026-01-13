# Study-Management-AI-Bot

This repository contains a standalone AI Engine for generating study content, including flashcards, quizzes, summaries, and answer evaluation. It's built with modularity in mind, allowing easy extension and integration with different AI providers.

## Features

1. **Flashcard Generation**: Generates question-answer pairs from input text or topics.
2. **Quiz Generation**: Creates multiple-choice questions with options and correct answers.
3. **Notes Summarization**: Produces concise summaries from long texts.
4. **Answer Evaluation**  Evaluates user answers against correct ones, providing scores and feedback.

## Architecture

- **Modular Design**: Separate classes for AI providers, features, and prompts.
- **Provider Independence**: Easily switch between AI models (e.g., OpenAI, others).
- **Configuration**: Uses environment variables for API keys and settings.
- **Structured Outputs**: All outputs are in JSON format for consistency.
