import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain.document_loaders import PyPDFLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.llms import OpenAI
from langchain.embeddings import OpenAIEmbeddings

# Embedding用
def mains():
    os.environ["OPENAI_API_TYPE"] = "azure"
    os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"
    os.environ["OPENAI_API_BASE"] = "https://***.openai.azure.com/"

    # テキストローダーを定義
    loader = PyPDFLoader("./data/twitter.pdf")

    # ベクトル化用モデルを定義
    embeddings = OpenAIEmbeddings(
        model='text-embedding-ada-002',
        deployment="teama-embedding-ada-002",
        chunk_size=1)

    # ChatGPT用
    os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"
    os.environ["OPENAI_API_BASE"] = "https://***.openai.azure.com/"
    llm = OpenAI(model_name='gpt-35-turbo', model_kwargs={"deployment_id":"teama-gpt-35-turbo"})
    # テキストをベクトル化/インデックス化
    index = VectorstoreIndexCreator(embedding=embeddings).from_loaders([loader])
    return index

print(mains())