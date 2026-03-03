def generate_support_reply(generator, generate_response, text):

    prompt = f"""
Generate a polite professional response to this customer complaint:

{text}
"""

    return generate_response(generator, prompt, max_tokens=120, temperature=0.5)
