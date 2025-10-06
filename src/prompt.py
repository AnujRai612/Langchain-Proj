prompt_template="""
You are an expert at creating questions based on materials and documentation provided.
Your goal is to prepare user for their exams and tests.

------
{text}
------

Create questions that will prepare user for their exams and tests.
Make sure not to loose any important information.

QUESTIONS:
"""





refine_template = ("""
You are an expert at creating questions based on materials and documentation provided.
Your goal is to prepare user for their exams and tests.
We have received some practice questions to a certain extent:{existing_answer}.
We have the option to refine the questions or add new one (only if neccessary) with some more context below.

------------
{text}
------------

Given the new content, refine the orginial questions in English.
If the context is not helpful, please provide the original questions.
QUESTIONS:
""")