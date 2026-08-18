import os
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file
from groq import Groq
client = Groq(
            api_key=os.environ.get("GROQ_API_KEY"),
        )

clubs = ["Go home after collage", "Sports", "Education", "Geography", "Space Reasearch", "Daily News"]
clubs_string = ', '.join(clubs)
System_prompt=  f"""You are an expert, patient, and engaging collage club guider based on students interests.
Core Guidelines:
1. Gather student's interest (hobbies, goals) and keep it in the memory
2. From the student's interests and from club list, recommend a collage club by name with a one-line reason.
Available Clubs: 
{clubs_string}
"""

history = [
    {"role": "system", "content": System_prompt},
]

while True:
    input_text = input("Enter your prompt (or type 'exit' to quit): ")
    if input_text.lower() == 'exit':
        break
    if input_text.lower() == 'show':
        print("\nThis is the History: ")
        print(history)
        continue
    
    history.append({"role": "user", "content": input_text})    
    chat_completion = client.chat.completions.create(
        messages=history,
        model="openai/gpt-oss-20b",
    )
    output_text = chat_completion.choices[0].message.content
    history.append({"role": "assistant", "content": output_text})
    print(output_text)