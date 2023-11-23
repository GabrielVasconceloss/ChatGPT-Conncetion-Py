from openai import OpenAI
import requests
import json
OPENAI_API_KEY = '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'
link = 'https://api.openai.com/v1/chat/completions'
model_id = "gpt-3.5-turbo"
headers = {"Authorization": f"Bearer {OPENAI_API_KEY}", "Content-Type": "application/json"}
body_meg = {
  "model": model_id,
  "messages": [{"role": "user", "content": "Quantos dias tem o Ano?"}]
}
body_meg = json.dumps(body_meg)

req = requests.post(link, headers=headers, data=body_meg)

print(req.text)

# client = OpenAI(api_key=OPENAI_API_KEY)
#
# completion = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "user", "content": "Quantos dias tem um ano?."}
#   ]
# )

# print(completion.choices[0].message)