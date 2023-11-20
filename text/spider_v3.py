import openai
import json

def process_messages(text, language, mode='cat', messages=[]):

    with open('./text/static/config.json', 'r') as f:
        info = json.load(f)

    if messages == []:
        openai.api_key = info['API_key']
        messages.append({"role": "system", "content": info[mode]})

    
        
    messages.append({"role": "user", "content": text + f"请用{language}（语言）回复我"})
        
    return messages