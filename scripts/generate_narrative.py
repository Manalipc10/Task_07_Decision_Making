import os
from groq import Groq
from dotenv import load_dotenv
load_dotenv()
def generate_narrative(prompt_file, output_file="outputs/narrative_raw.txt"):
    with open(prompt_file, "r") as f:
        prompt = f.read()
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    GROQ_MODEL = os.getenv("GROQ_MODEL")
    client = Groq(api_key=GROQ_API_KEY)

    response = client.chat.completions.create(
        model=GROQ_MODEL,   # or another Groq-supported model
        messages=[
            {"role": "system", "content": "You are a sports analyst."},
            {"role": "user", "content": prompt},
        ],
    )

    narrative = response.choices[0].message.content

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(narrative)

    print(f"[INFO] Narrative saved to {output_file}")

if __name__ == "__main__":
    generate_narrative("prompts/narrative_prompt.txt")
