import langextract as lx
import textwrap

# 1. Define the prompt and extraction rules
prompt = textwrap.dedent("""\
    Extract sentiment, emotions, and topics in order of appearance.
    Use exact text for extractions.""")

# 2. Provide a high-quality example to guide the model
examples = [
    lx.data.ExampleData(
        text="I recently called customer care to cancel a contract which was complete. The sales person advised me to keep the contract on a cheap rate in case there would be an iPad going on special then in that case I could upgrade. However when I tried to upgrade I was told sorry you can’t now until 3 years was up.",
        extractions=[
            lx.data.Extraction(
                extraction_class="sentiment",
                extraction_text="I recently called customer care to cancel a contract which was complete. The sales person advised me to keep the contract on a cheap rate in case there would be an iPad going on special then in that case I could upgrade. However when I tried to upgrade I was told sorry you can’t now until 3 years was up.",
                attributes={"sentiment": "negative"}
            ),
            lx.data.Extraction(
                extraction_class="emotion",
                extraction_text="I recently called customer care to cancel a contract which was complete. The sales person advised me to keep the contract on a cheap rate in case there would be an iPad going on special then in that case I could upgrade. However when I tried to upgrade I was told sorry you can’t now until 3 years was up.",
                attributes={"emotions": ["disappointment", "regret", "confusion", "frustration", "annoyance"]}
            ),
            lx.data.Extraction(
                extraction_class="topics",
                extraction_text="I recently called customer care to cancel a contract which was complete. The sales person advised me to keep the contract on a cheap rate in case there would be an iPad going on special then in that case I could upgrade. However when I tried to upgrade I was told sorry you can’t now until 3 years was up. ",
                attributes={"topics": ["Customer Service", "Pricing and Value", "Return and Refund", "Delivery Issues", "User Experience"]}
            ),
        ]
    )
]

def main(text: str) -> dict:
    response: dict= {}

    # Run the extraction
    result = lx.extract(
        text_or_documents=text,
        prompt_description=prompt,
        examples=examples,
        model_id="gemini-2.5-flash",
    )

    # Structured data
    response["text"] = result.text
    for ext in result.extractions:
        response[ext.extraction_class] = list(ext.attributes.values())[0]

    return response


if __name__ == "__main__":
    text = [
            "I had a great stay. The staff is friendly, professional, and always willing to help. The rooms are spacious, clean, and well-equipped. A special mention goes to the restaurant: the food is delicious, varied, and served with …",
            "Good day\n My car was in an accident on 20 July 2025. On 21 July 2025  I contacted Miway to report the accident. It took 10 days to submit, process and approve my claim. Please note during this time I had to make numerous calls to follow up on how far the process is. Also, my car is in a driving state, but I noticed that the bumper was starting to lower, which resulted in the gap between the right front tyre and bumper was n.."
        ]
    res = main(text[1])
    print(res)

"""# Save the results to a JSONL file
lx.io.save_annotated_documents([result], output_name="extraction_results.jsonl", output_dir=".")

# Generate the visualization from the file
html_content = lx.visualize("extraction_results.jsonl")
with open("visualization.html", "w") as f:
    f.write(html_content)
"""