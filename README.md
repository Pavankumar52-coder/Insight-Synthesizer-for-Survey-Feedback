#  Insight Synthesizer for Survey Feedback Using an LLM

## Overview:

This Python project utilizes the Gemini-2.0-flash large language model (LLM) from Google to analyze raw user feedback (survey responses) and extract structured insights. It generates "Insight Cards," each containing a concise theme summarizing the feedback and supporting quotes directly from the survey responses. Optionally, it can also provide a sentiment score for each theme.
This project mimics the functionality of Outlaw's insight engine for startup founders and product managers, providing a way to quickly identify key themes and user opinions from qualitative data.

## Features:
* **LLM-Powered Insight Generation:** Leverages the Gemini Pro model to identify patterns and themes in user feedback.
* **Structured Output:** Generates insight cards with a clear theme and supporting quotes in a JSON format.
* **Basic Preprocessing:** Includes a function for basic cleaning of the input feedback.
* **Evaluation Metrics:** Provides basic evaluation metrics such as the number of generated and non-empty insights.
* **Visual Output:** Displays the generated insight cards in a readable table format using the `tabulate` library.
* **Configurable Number of Insights:** Allows you to specify the number of insight cards to generate.

## Tech Stack

* Python
* Google Gemini API (`google-generativeai`)
* `tabulate` for visual output

## Setup

1.  **Clone the Repository (Optional):**
    ```bash
    git clone <your_repo_url>
    cd your_repo_name
    ```

2.  **Install Dependencies:**
    ```bash
    pip install google-generativeai python-dotenv tabulate
    ```

3.  **Configure Google Gemini API Key:**
    * Create a `.env` file in the same directory as your Python script.
    * Add your Google API key to the `.env` file:
        ```
        GOOGLE_API_KEY=YOUR_API_KEY
        ```
        **Note:** You can obtain an API key from the [Google AI Studio](https://makersuite.google.com/).

## Usage

1.  **Prepare Your Survey Feedback:** Ensure your survey responses are in a Python list format, where each element is a string representing one response.

2.  **Run the Python Script:**
    * Open the Python script (e.g., `insight_synthesizer.py`).
    * Replace the `sample_feedback` list with your actual survey responses.
    * Optionally, adjust the `num_insight_cards` variable to control the number of insight cards generated.
    * Run the script from your terminal:
        ```bash
        python your_script_name.py
        ```

3.  **View the Output:** The script will print the generated insight cards in a JSON format and a readable table in the console, followed by basic evaluation metrics.

## Code Structure

* `insight_synthesizer.py`: The main Python script containing the logic for generating and displaying insight cards.
    * `create_insight_cards(feedback: List[str], num_cards: int = 3) -> List[Dict]`: Function to generate insight cards using the Gemini Pro model.
    * `preprocess_feedback(feedback: List[str]) -> List[str]`: Function for basic preprocessing of feedback.
    * `evaluate_insights(insight_cards: List[Dict], num_expected: int)`: Function to perform basic evaluation of the generated insights.
    * `display_insights(insight_cards: List[Dict])`: Function to display the insights in a table format.
    * The main execution block (`if __name__ == "__main__":`) loads feedback, generates insights, displays them, and evaluates the output.

## Evaluation:

The script includes a basic evaluation that reports:

* Number of Insights Generated
* Number of Non-Empty Insights (containing a theme and at least one quote)

**Note:** The relevance of the quotes to the theme and the consistency of the sentiment analysis require manual inspection for a comprehensive evaluation. More advanced evaluation metrics would typically require labeled data or more sophisticated NLP techniques.

## Bonus: Offline LLM (Conceptual):
The comments in the `insight_synthesizer.py` provide a conceptual outline of how you might adapt the code to use an offline LLM from Hugging Face Transformers. This would involve:

1.  Installing the `transformers` library.
2.  Choosing and loading a suitable pre-trained language model.
3.  Adjusting the prompt format to be compatible with the chosen model.
4.  Using the model's generation capabilities to produce the insight cards.

Implementing this would require further research and experimentation with specific offline models and their usage.
