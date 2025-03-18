import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.environ['GEMINI_API_KEY'])

model = genai.GenerativeModel(model_name="gemini-2.0-flash")

# Continuously get input from the user
while True:
    user_input = input("Enter your question (or 'quit' to exit): ")
    if user_input.lower() == 'quit':
        print("Thank you for using the chatbot!")
        break
    response = model.generate_content(user_input)
    print("\nResponse:",response.text)