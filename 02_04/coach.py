import os
from openai import OpenAI

# ---- Configuration ----
# Use a fine-grained PAT with models:read scope in GitHub Codespaces
token = os.environ["GITHUB_TOKEN"]
if not token:
    raise SystemExit("Error: Missing API key. Set GITHUB_TOKEN.")

endpoint = "https://models.github.ai/inference" 
model_name = "openai/o4-mini"

# ---- Client ----
client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

# ---- Request ----
try:
    response = client.chat.completions.create(
        model=model_name,
        reasoning_effort="medium",  # low | medium | high
        messages=[
            {
                "role": "developer",
                "content": (
                    "You are an AI Personal Coach. "
                    "Provide clear, personalized, practical advice. "
                    "Respond concisely with 3–5 concrete steps."
                ),
            },
            {
                "role": "user",
                "content": "Provide steps I can take to reduce stress during the work week."
            }
        ],
    )

    print("\n--- AI Personal Coach Response ---")
    print(response.choices[0].message.content)

except Exception as e:
    print(f"[Error] API call failed: {e}")
