from groq import Groq
import os

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def write_report(topic, plan):

    prompt = f"""
    You are a professional research analyst.

    Write a detailed and structured research report on:

    Topic: {topic}

    Use the following research findings:
    {plan}

    Requirements:
    - Use clear headings
    - Explain each section in detail
    - Include real-world examples
    - End with a strong conclusion
    """

    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "user", "content": prompt}
        ],
        model="llama-3.1-8b-instant"
    )

    return chat_completion.choices[0].message.content