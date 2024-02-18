# Bible QA

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