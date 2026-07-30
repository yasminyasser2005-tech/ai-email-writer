import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_reply(complaint_text, tone="professional and empathetic", company_name="Our Company"):
    system_prompt = f"""You are a customer service assistant for {company_name}.
Write a professional email reply to the customer complaint below.

Rules:
- Tone: {tone}
- Acknowledge the customer's specific issue, don't be generic
- Apologize sincerely without admitting legal fault
- Offer a clear next step or resolution
- Keep it concise: 3-5 short paragraphs
- Sign off as "Customer Support Team"
- Do not invent specific facts (refund amounts, dates, order numbers)
  that weren't in the original complaint
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Customer complaint:\n{complaint_text}"},
        ],
        temperature=0.5,
    )
    return response.choices[0].message.content