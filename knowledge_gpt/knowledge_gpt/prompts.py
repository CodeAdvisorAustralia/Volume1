# flake8: noqa
from langchain.prompts import PromptTemplate

## Use a shorter template to reduce the number of tokens in the prompt
template = """USe your full capabilities to answer the Questions:"""

STUFF_PROMPT = PromptTemplate(
    template=template,
)
