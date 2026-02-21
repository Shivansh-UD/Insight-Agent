from groq import Groq
import os

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def search_topic(subtopic):

    prompt = f"""
    Provide factual, concise research findings on:

    {subtopic}

    Include:
    - Key statistics
    - Real-world examples
    - Current trends
    """

    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "user", "content": prompt}
        ],
        model="llama-3.1-8b-instant"
    )

    return chat_completion.choices[0].message.content

'''
WE ARE TEMPORARLY USING THE RESEARCH TO BE DONE BY THE LLM HERE BUT LATER IN THE FUTURE WE CAN USE THINGS LIKE API FROM GOOGLE 
OR OTHER BROWSERS.
'''