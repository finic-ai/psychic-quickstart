# Psychic Quickstart
This is the code for the [quickstart tutorial](https://docs.psychic.dev/quickstart) for Psychic. It showing how to connect documents from an application API (e.g. Notion, Confluence, Zendesk, etc) as a knowledge base for a LLMs using Psychic, Chroma, and LangChain.

## Running
1. Create an account at https://dashboard.psychic.dev/ (it's free) and connect any application account.
2. Rename `rename.env` to `.env` and fill in your own OPENAI_API_KEY and PSYCHIC_SECRET_KEY.
3. Replace `account_id` in `main.py` with the Account ID you used in step 1.
4. [Install poetry](https://python-poetry.org/docs/) to run this project in a virtual environment.
5. Run the following in order:
    ```bash
    poetry install
    poetry shell
    python main.py
    ```