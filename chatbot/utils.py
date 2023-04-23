import openai

openai.api_key = "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"

def generate_chatbot_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return response.choices[0].text.strip()
