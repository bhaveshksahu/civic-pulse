import os
from groq import Groq

CATEGORIES = [
    "Environment & Conservation",
    "Elder Care",
    "Child Welfare",
    "Healthcare",
    "Women Safety",
    "Education & Youth Development",
    "Human Rights & Advocacy",
    "Animal Welfare",
    "Poverty & Basic Needs"
]

def classify_issue(problem_text):
    # This securely pulls the key from your .env file instead of hardcoding it
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{
            "role": "user",
            "content": f"""You are an NGO routing assistant for India. Classify this community problem into EXACTLY ONE category:
{chr(10).join(CATEGORIES)}

Problem: "{problem_text}"

Reply with ONLY the category name. Nothing else."""
        }]
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    test = "There is garbage piled up near the park for 2 weeks, it smells terrible"
    print(classify_issue(test))