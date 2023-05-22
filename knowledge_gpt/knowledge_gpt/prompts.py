from langchain.prompts import PromptTemplate

## Use a shorter template to reduce the number of tokens in the prompt
template = """ 
Do not mention pages, instead highlight the relevant clauses, follow the requirements of the question closely
So for every question, there should be two or three answers. Even if the answer is,
"to comply with weatherproofing there are three options, Deemed to Satisfy (H2D8), Performaance (H2P1) and the Verification method (H2V1). Which one would you like more information about?"
---------

QUESTION: How do i comply with the weatherproofing requirements, there are three answers. ?
=========
For a Deemed to Satisfy compliance, you need to following the information in H2D8,
For a Performance Pathway, you need to a report in line with A5G3 that addresses the performance requirements of H2P2
Or You can also comply with the performance requirements (H2P2) by having a report prepared that meets the requirements of the Verification Methods (H2V1).
=========
FINAL ANSWER: to comply with weatherproofing there are three options, Deemed to Satisfy (H2D8), Performaance (H2P1) and the Verification method (H2V1). Which one would you like more information about?

---------

QUESTION: {question}
=========
{summaries}
=========
FINAL ANSWER:"""

STUFF_PROMPT = PromptTemplate(
    template=template, input_variables=["summaries", "question"]
)
