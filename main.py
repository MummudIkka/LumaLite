import openai

openai.api_key = "your-openai-api-key"

def get_response(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are Luma, a helpful AI assistant."},
                  {"role": "user", "content": user_input}]
    )
    return response["choices"][0]["message"]["content"]
