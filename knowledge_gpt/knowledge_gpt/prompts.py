from langchain.prompts import PromptTemplate

## Use a shorter template to reduce the number of tokens in the prompt
template = """ 
Never mention pages, instead highlight the relevant sections such as B1P1, follow the requirements of the question closely
---------

QUESTION: what clauses detail termite requirements?
=========
FINAL ANSWER : Termite Actions are listed in B1P1(2)(o) as a method of satisfying compliance with 'B1P1 Structural Reliability' performance requirements

Additionally, the provision B1D4 relates to the determination of the structural resistance of materials and forms of construction. Specifically, it addresses termite risk management for primary building elements. The following points summarize the requirements outlined in the provision:

Primary building elements susceptible to subterranean termite attack must comply with AS 3660.1, a standard that provides guidelines for termite management.
Certain materials are considered not subject to termite attack, including steel, aluminum, concrete, masonry, fibre-reinforced cement, timber that is naturally termite resistant (as specified in Appendix C of AS 3660.1), and timber that is preservative treated (as outlined in Appendix D of AS 3660.1).
A durable notice must be permanently affixed to the building in a prominent location (such as the meter box) and include the following information:
The termite management system used.
The date of installation of the termite management system.
For chemical treatments, the life expectancy of the pesticide as listed on the appropriate authority's pesticides register label.
The recommendations from the installer or manufacturer regarding the scope and frequency of future inspections for termite activity.
These requirements aim to ensure proper termite management and provide information for ongoing inspections and maintenance of the building.
---------

Question: {question}
=========
{summaries}
=========
FINAL ANSWER:"""

STUFF_PROMPT = PromptTemplate(
    template=template, input_variables=["summaries", "question"]
)
