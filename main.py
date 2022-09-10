from typing import Union

import uvicorn
from fastapi import FastAPI

app = FastAPI()

post = []


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/post/{id}")
def get_post(id: str):
    for i in post:
        if i.get("id") == id:
            return i
    return {"message": "Post not found!"}

@app.get("/post")
def get_all_post():
    return {"data": post}


@app.post("/post")
def add_post(id: str, title: str):
    post.append({"id": id, "title": title})
    return {"message": "Added successfully."}


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
