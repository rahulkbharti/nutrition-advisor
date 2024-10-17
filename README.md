# Personalized Nutrition Advisor (AI-Nutritionist-App)

This is a Streamlit application that provides personalized nutrition advice based on user input. 

## Features
- Input dietary information
- Receive personalized nutrition suggestions
- Simple and user-friendly interface

## Prerequisites

- Python 3.x
- Streamlit
- Any necessary API for nutrition advice

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-repo/nutrition-advisor.git
    cd nutrition-advisor
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # For Linux/Mac
    venv\Scripts\activate     # For Windows
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## API Key Setup

To use this app, you need an API key for personalized nutrition advice. Follow these steps:

1. Open the `.env` file.
2. Replace the placeholder with your API key:

    ```python
    API_KEY = "your-api-key-here"
    ```

## Usage

1. Run the application:

    ```bash
    streamlit run app.py
    ```

2. Follow the on-screen instructions to input your dietary information and receive personalized nutrition advice.

## Output 
![output1](./outputs/Screenshot%202024-08-27%20102837.png)
![output2](./outputs/Screenshot%202024-08-27%20102921.png)

## Contributing

Feel free to submit a pull request or report any issues!

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
