import os
from typing import Union
from fastapi import FastAPI
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel



load_dotenv()

app = FastAPI()

if "OPENAI_API_KEY" in os.environ:
  openai_api_key = os.environ["OPENAI_API_KEY"]

class GenerateArticleRequestBody(BaseModel):
    topic: str

class GenerateArticleResponseBody(BaseModel):
   article: str


@app.get("/")
def read_root():
  return {"Hello": "World"}


@app.get("/generate_article")
def generate_article_from_ai(request: GenerateArticleRequestBody):
  llm = ChatOpenAI(
          openai_api_key=openai_api_key,
          model_name="gpt-3.5-turbo",
          temperature=0.3,
          max_tokens=2000
        );
  
  prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a great writer, your task is to generate an nice article for the user input including summary of the article in 2 lines at the end of the article. Length of the article should be around 300 words only."),
    ("user", "{input}")
  ])
  topic = request.topic
  chain = prompt | llm
  output = chain.invoke({"input": topic})
  print(output)
  return GenerateArticleResponseBody(article = output.content) 



