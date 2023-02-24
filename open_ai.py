import openai

openai.api_key = "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"


def generate_response(prompt):
    response = openai.Completion.create(
        engine="davinci", prompt=prompt, max_tokens=1024, n=1, stop=None, temperature=0.7
    )
    message = response.choices[0].text.strip()
    return message


prompt = "Hello, how are you?"
response = generate_response(prompt)
print(response)
