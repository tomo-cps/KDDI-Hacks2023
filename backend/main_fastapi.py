import os
from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain.document_loaders import PyPDFLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.llms import OpenAI
from langchain.embeddings import OpenAIEmbeddings

# Embedding用
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
print(index)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    # allow_origins=[
    #     "http://54.238.157.42/",
    #     "http://54.238.157.42/chat1",
    #     "http://54.238.157.42/chat2",
    #     "http://54.238.157.42/chat3",
    #     "http://54.238.157.42/chat4",
    #     "http://54.238.157.42/chat5",
    #     "http://54.238.157.42/chat6",
    # ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

class Question(BaseModel):
    question: str

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/ask")
def ask_question(question: Question):
    response = index.query(llm=llm, question=question.question)
    res = llm(response+"/n"+"/n"+"上のテキスト情報の出力がキリが悪いので，キリをよくしてください.なお，高校生でもわかりやすい出力をしてください")
    # max_length = 200  # 任意の最大文字数を設定
    # shortened_response = response[:max_length]
    return {"answer": res}
