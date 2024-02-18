# Bible QA

Ask a question about the Bible and get an answer.

This uses ColBERT embeddings to retrieve relevant passages from the Bible (ESV) and then uses OpenAI's `gpt-3.5-turbo-0125` to answer the question.

# Setup

```bash
pyenv local 3.11
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# install in editable mode
pip install -e .

# setup pre-commit
pre-commit install
```