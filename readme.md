# Interactive Chatbot with OpenAI's GPT-4-Turbo 🤖

An interactive chatbot leveraging OpenAI's latest GPT-4-turbo model to engage in meaningful conversations. Tailored for civil and structural engineering queries, it provides succinct, professional, and technically precise responses. Each response is conveniently copied to your clipboard, thanks to the `pyperclip` library.

This chatbot was developed for my friend Scott, a blind civil engineer who likes to simplify things by working directly in powershell or the CLI. This is a bare bones version of GPT 4-Turbo that streamlines his workflow.

## Features ✨

- **Contextual Conversations**: Maintains a history for coherent and context-aware interactions.
- **Clipboard Integration**: Automatically copies the AI's response to your clipboard.
- **Customizable**: Easily adaptable to various professional domains beyond engineering.

## Prerequisites 📋

Before you start, ensure you have the following:

- An OpenAI API key.
- `python-dotenv` for environment variable management.
- `pyperclip` for clipboard functionality.

## Getting Started 🚀

### Setup Environment

1. **Clone the repository** to your local machine.

2. **Navigate into the project directory**:
   cd path/to/your/project

3. **Install dependencies** using [Poetry](https://python-poetry.org/) or pip:
   poetry install

   # or

   pip install -r requirements.txt

4. **Set up your `.env` file** at the project root with your OpenAI API key:
   `OPENAI_API_KEY='your_api_key_here`

### Usage

Run the script in your terminal, and interact with the chatbot as you would with a human:

`python path/to/your/chatbot_script.py`

Type your messages after the prompt `You:` and witness the AI crafting responses tailored to civil and structural engineering—or any other domain you configure it for.

To exit, simply type `quit`.

## Contributions 🤝

Interested in enhancing this project? Your contributions are welcome! Please feel free to fork the repository, make your changes, and submit a pull request.

## License 📄

Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgments 💡

- [OpenAI](https://platform.openai.com/docs/models/gpt-4-and-gpt-4-turbo) for the GPT-4 Turbo model.
- [Python-dotenv](https://github.com/theskumar/python-dotenv) for environment variable management.
- [Pyperclip](https://github.com/asweigart/pyperclip) for clipboard operations.

## Contact 📧

Got questions or feedback? Reach out to me at [info@flocode.dev](mailto:info@flocode.dev).
