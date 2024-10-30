import getpass
import os

from langchain_openai import AzureChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser

os.environ["AZURE_OPENAI_API_VERSION"] = "2024-10-01-preview"


# os.environ["AZURE_OPENAI_API_KEY"] = getpass.getpass()
# Instantiate the model with environment variables
model = AzureChatOpenAI(
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    openai_api_version=os.environ["AZURE_OPENAI_API_VERSION"],
)


messages = [
    SystemMessage(content="Translate the following from English into Italian"),
    HumanMessage(content="hi!"),
]

model.invoke(messages)

# print(model)
# print(messages)

parser = StrOutputParser()

result = model.invoke(messages)
# print(result.content)


# print(parser.invoke(result))
chain = model | parser
print(chain.invoke(messages))
