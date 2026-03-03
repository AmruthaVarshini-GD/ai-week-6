import json
import pandas as pd
from src.model_loader import load_model, generate_response
from src.classifier import classify_ticket

print("Loading model...")
generator = load_model()
print("Model loaded successfully!\n")

with open("data/sample_tickets.json") as f:
    tickets = json.load(f)

results = []

for ticket in tickets:
    predicted = classify_ticket(generator, generate_response, ticket["text"])

    results.append({
        "id": ticket["id"],
        "expected": ticket["expected_category"],
        "predicted": predicted
    })

df = pd.DataFrame(results)
print(df)

accuracy = sum(df["expected"] == df["predicted"]) / len(df) * 100
print(f"\nAccuracy: {round(accuracy,2)}%")
