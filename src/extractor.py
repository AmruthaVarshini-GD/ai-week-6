import json

def extract_information(generator, generate_response, text):

    prompt = f"""
Extract:
1. Product (if mentioned)
2. Issue type (short phrase)

Return JSON format:
{{"product":"...","issue":"..."}}

Ticket:
{text}
"""

    response = generate_response(generator, prompt, max_tokens=80, temperature=0.2)

    try:
        start = response.find("{")
        end = response.rfind("}") + 1
        return json.loads(response[start:end])
    except:
        return {"product":"Not Found","issue":"Not Found"}
