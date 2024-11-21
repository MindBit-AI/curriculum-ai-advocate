from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

prompt_template = ChatPromptTemplate.from_messages(
    [("user", "Tell me a {adjective} joke")],
)

model = ChatOpenAI(model="gpt-4o-mini")

parser = StrOutputParser()

# Old way
# prompt = prompt_template.invoke({"adjective": "funny car"})
# response = model.invoke(prompt)
# result = parser.invoke(response)
# print(result)

# New way! Chaining!
chain = prompt_template | model | parser
result = chain.invoke({"adjective": "funny"})
print(result)