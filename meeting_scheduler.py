import openai
import os
from dotenv import load_dotenv

# Load the API key from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def schedule_meetings(details):
    prompt = f"Generate a detailed meeting schedule for the week based on the following details:\n{details}"
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert meeting scheduler."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=200
    )
    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    details = input("Enter meeting details (e.g., topics, available time slots): ")
    schedule = schedule_meetings(details)
    print("\nGenerated Meeting Schedule:\n", schedule)
