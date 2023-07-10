import os
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
# from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import main

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # リクエストを許可するオリジンを指定します。必要に応じて修正してください。
    allow_methods=["*"],  # 許可するHTTPメソッドを指定します。
    allow_headers=["*"],  # 許可するリクエストヘッダを指定します。
    allow_credentials=True,   # 追記により追加
)

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
    index, llm = main()
    response = index.query(llm=llm, question=question.question)
    max_length = 200  # 任意の最大文字数を設定
    shortened_response = response[:max_length]
    return {"answer": shortened_response}
    # return "hoge"
