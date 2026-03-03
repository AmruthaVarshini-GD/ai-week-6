def classify_ticket(generator, generate_response, text):

    prompt = f"""
Classify the customer support ticket into ONE category only:
Technical, Billing, General, Complaint.

Respond with ONLY the category name.

Ticket:
{text}
"""

    response = generate_response(generator, prompt, max_tokens=10, temperature=0.2)

    categories = ["Technical","Billing","General","Complaint"]

    for cat in categories:
        if cat.lower() in response.lower():
            return cat

    return "Unknown"
