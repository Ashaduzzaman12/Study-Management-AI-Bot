import streamlit as st
import os
import json
from abc import ABC, abstractmethod
from typing import Dict, Any
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
class BaseProvider(ABC):
    @abstractmethod
    def generate_response(self, prompt: str) -> str:
        """
        Generate a response from the AI model based on the prompt.
        :param prompt: The input prompt string.
        :return: The AI-generated response as a string.
        """
        pass
# OpenAI Provider 
class OpenAIProvider(BaseProvider):
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        self.model = "gpt-3.5-turbo"  # Can be configured via env if needed

    def generate_response(self, prompt: str) -> str:
        """
        Generate a response using OpenAI's API.
        """
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=1000,
                temperature=0.7
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            raise RuntimeError(f"OpenAI API error: {str(e)}")

# Flashcard Generator 
class FlashcardGenerator:
    def __init__(self, provider: BaseProvider):
        self.provider = provider

    def generate(self, text: str) -> Dict[str, Any]:
        
        prompt = f"""
        Generate 3-5 question-answer pairs (flashcards) from the following text. Each pair should be clear, accurate, and suitable for learning. Output in JSON format like: {{"flashcards": [{{"question": "Q", "answer": "A"}}]}}.

        Text: {text}
        """
        response = self.provider.generate_response(prompt)
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            return {"error": "Failed to parse response as JSON"}
# Quiz Generator 
class QuizGenerator:
   
    def __init__(self, provider: BaseProvider):
        self.provider = provider

    def generate(self, text: str) -> Dict[str, Any]:
        
        prompt = f"""
        Generate 3-5 multiple-choice questions from the following text. Each question should have 4 options, with one correct answer. Output in JSON format like: {{"quiz": [{{"question": "Q", "options": ["A", "B", "C", "D"], "correct_answer": "A"}}]}}.

        Text: {text}
        """
        response = self.provider.generate_response(prompt)
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            return {"error": "Failed to parse response as JSON"}

# Summarizer 
class Summarizer:
   
    def __init__(self, provider: BaseProvider):
        self.provider = provider

    def generate(self, text: str) -> Dict[str, Any]:
        
        prompt = f"""
        Provide a concise and informative summary of the following text, preserving key concepts. Output in JSON format like: {{"summary": "Summary text"}}.

        Text: {text}
        """
        response = self.provider.generate_response(prompt)
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            return {"error": "Failed to parse response as JSON"}

# Answer Evaluator 
class AnswerEvaluator:
    def __init__(self, provider: BaseProvider):
        self.provider = provider

    def evaluate(self, user_answer: str, correct_answer: str) -> Dict[str, Any]:
        
        prompt = f"""
        Evaluate the user's answer against the correct answer. Provide a score out of 10 and brief feedback. Output in JSON format like: {{"score": 8, "feedback": "Brief explanation"}}.

        User's Answer: {user_answer}
        Correct Answer: {correct_answer}
        """
        response = self.provider.generate_response(prompt)
        try:
            return json.loads(response)
        except json.JSONDecodeError:
            return {"error": "Failed to parse response as JSON"}
# Streamlit App
def main():
    # Initialize provider and features
    provider = OpenAIProvider()
    flashcard_gen = FlashcardGenerator(provider)
    quiz_gen = QuizGenerator(provider)
    summarizer = Summarizer(provider)
    evaluator = AnswerEvaluator(provider)

    st.title("Study Management AI")

    # Feature selection
    feature = st.selectbox("Select Feature", ["Flashcards", "Quiz", "Summarization", "Answer Evaluation"])

    # Input fields
    if feature in ["Flashcards", "Quiz", "Summarization"]:
        text_input = st.text_area("Enter study text or topic:")
        if st.button("Generate"):
            if text_input:
                if feature == "Flashcards":
                    result = flashcard_gen.generate(text_input)
                elif feature == "Quiz":
                    result = quiz_gen.generate(text_input)
                elif feature == "Summarization":
                    result = summarizer.generate(text_input)
                st.json(result)
            else:
                st.error("Please enter text.")
    elif feature == "Answer Evaluation":
        user_answer = st.text_area("User's Answer:")
        correct_answer = st.text_area("Correct Answer:")
        if st.button("Evaluate"):
            if user_answer and correct_answer:
                result = evaluator.evaluate(user_answer, correct_answer)
                st.json(result)
            else:
                st.error("Please enter both answers.")

if __name__ == "__main__":
    main()
