import openai
openai.api_key = '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'
def get_chat_completion(prompt, model="gpt-3.5-turbo"):
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return str(e)
