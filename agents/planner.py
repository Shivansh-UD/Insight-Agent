from groq import Groq
import os

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def generate_plan(topic):

    prompt = f"""
    You are a research planning assistant.
    Break the following topic into 5-7 structured research subtopics.

    Topic: {topic}

    Return only a clean numbered list.
    """

    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "user", "content": prompt}
        ],
        model="llama-3.1-8b-instant"
    )

    return chat_completion.choices[0].message.content