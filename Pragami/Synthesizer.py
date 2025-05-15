# Import necessary libraries
import google.generativeai as genai
import json
from typing import List, Dict
from tabulate import tabulate

# Configure the Gemini API for synthesizing
GOOGLE_API_KEY = "AIzaSyDGKVnWUcM_vrl-PXTYZ7ZVeDo4gzJHluw"
if not GOOGLE_API_KEY:
    raise ValueError("Please set the GOOGLE_API_KEY environment variable.")
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-2.0-flash')

# Function to create insight cards
def create_insight_cards(feedback: List[str], num_cards: int = 3) -> List[Dict]:
    """
    Generates insight cards from a list of user feedback using a Language Model.

    Args:
        feedback: A list of strings, where each string is a user's feedback.
        num_cards: The number of insight cards to generate.

    Returns:
        A list of dictionaries, where each dictionary represents an insight card
        with a theme, supporting quotes, and an optional sentiment score.
    """
    prompt = f"""
    You are an AI-powered insight engine designed to analyze user feedback and
    extract key themes. Your task is to process the following survey responses
    and generate {num_cards} distinct insight cards. Each insight card should
    include a concise title representing the main theme, and 1-2 supporting
    quotes directly from the feedback that best illustrate this theme.
    Optionally, include a brief sentiment analysis (positive, negative, or neutral)
    for the theme based on the supporting quotes.

    Survey Responses:
    ```
    {' '.join(feedback)}
    ```

    Format your output as a JSON array of insight card objects, where each object
    has the following structure:
    ```json
    [
      {{
        "theme": "...",
        "quotes": ["...", "..."],
        "sentiment": "..." // Optional
      }},
      ...
    ]
    ```
    """

    response = model.generate_content(prompt)
    try:
        insights = json.loads(response.text)
        return insights
    except json.JSONDecodeError:
        print(f"Error decoding JSON response: {response.text}")
        return []

# Function to preprocess the user feedback
def preprocess_feedback(feedback: List[str]) -> List[str]:
    """
    Basic preprocessing function (can be expanded if needed).
    Currently, it just removes leading/trailing whitespace.

    Args:
        feedback: A list of raw feedback strings.

    Returns:
        A list of cleaned feedback strings.
    """
    return [f.strip() for f in feedback]

# Function for evaluation insights
def evaluate_insights(insight_cards: List[Dict], num_expected: int):
    """
    Performs basic evaluation of the generated insight cards.

    Args:
        insight_cards: A list of generated insight card dictionaries.
        num_expected: The expected number of insight cards.
    """
    num_generated = len(insight_cards)
    non_empty_insights = 0
    for card in insight_cards:
        if "theme" in card and card["theme"] and "quotes" in card and card["quotes"]:
            non_empty_insights += 1

    print("\n--- Evaluation Metrics ---")
    print(f"Number of Insights Generated: {num_generated}/{num_expected}")
    print(f"Number of Non-Empty Insights (Theme & Quotes): {non_empty_insights}/{num_expected}")
    print("\nNote: Quote relevance and sentiment consistency require manual inspection.")

# Function to display insights
def display_insights(insight_cards: List[Dict]):
    """
    Displays the generated insight cards in a table format.

    Args:
        insight_cards: A list of generated insight card dictionaries.
    """
    if not insight_cards:
        print("No insights to display.")
        return

    headers = ["Theme", "Quotes", "Sentiment (Optional)"]
    table_data = []
    for card in insight_cards:
        theme = card.get("theme", "N/A")
        quotes = "\n".join(card.get("quotes", []))
        sentiment = card.get("sentiment", "N/A")
        table_data.append([theme, quotes, sentiment])

    print("\n--- Generated Insight Cards ---")
    print(tabulate(table_data, headers=headers, tablefmt="grid"))

# Sample Input for testing
sample_feedback = [
    "I love the idea of an AI that writes emails...",
    "Privacy is my biggest concern...",
    "If this works with Gmail and Slack...",
    "Make sure it doesn't sound robotic.",
    "Would love integrations, but only if they're secure.",
    "The pricing seems a bit high for early-stage.",
    "I'm excited to see how this can save me time.",
    "Need better documentation.",
    "The UI is very intuitive.",
    "Integration with Google Calendar would be amazing.",
    "Not sure if I trust AI with sensitive information.",
    "The onboarding process was smooth.",
]

# Main function
if __name__ == "__main__":
    processed_feedback = preprocess_feedback(sample_feedback)
    num_insight_cards = 3
    insight_cards = create_insight_cards(processed_feedback, num_insight_cards)

    if insight_cards:
        display_insights(insight_cards)
        evaluate_insights(insight_cards, num_insight_cards)