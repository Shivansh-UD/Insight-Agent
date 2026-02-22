from groq import Groq
import os

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def write_report(topic, context):

    prompt = f"""
    You are an expert research analyst.

    Before writing, analyze the research context and identify the 4–6 most important themes. 
    Organize the report around those themes.

    Using the provided research context, write a comprehensive, well-structured report.

    Requirements:
    - Clear title
    - Executive summary (short overview)
    - 4–6 well-defined sections with headings
    - Bullet points where helpful
    - Real-world examples
    - Clear explanations
    - Conclusion summarizing key insights
    - Professional and academic tone

    Topic:
    {topic}

    Research Context:
    {context}

    Make the report detailed but clear.
    """

    chat_completion = client.chat.completions.create(
    messages=[
        {"role": "system", "content": "You are a professional research analyst who writes structured academic reports."},
        {"role": "user", "content": prompt}
    ],
    model="llama-3.1-8b-instant"
    )

    return chat_completion.choices[0].message.content