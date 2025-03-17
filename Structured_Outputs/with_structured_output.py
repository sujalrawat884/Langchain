from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict

model = ChatGoogleGenerativeAI(model='gemini-2-pro')

#schema

class Review(TypedDict):

    summary : str
    sentiment : str

structed_models = model.with_structured_output(Review)

result = structed_models.invoke("""This mobile phone is really amazing comsed with snapdragon 732G processor and 5000mah battery its a gamingg flagship phone charing speed with 65W """)

print(result.summary)