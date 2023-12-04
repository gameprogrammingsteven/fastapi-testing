from fastapi import FastAPI, Response, status
from enum import Enum 
from typing import Optional
from router import blog_get, blog_post

app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)


@app.get('/')
def Index():
    return 'Hello! Web'

@app.get('/pathid/all')
def Index2():
    return f'all blogifies'


@app.get('/pathid/{id}', status_code=404)
def Index2(id: int):
    return {"message" : f'message with Blog with ID {id}' }

@app.get('/randdemopath+queryparam/{id}/comment/{anotherPathVariable}', status_code=404, tags=['comments','test']) #tags swagger break up sections
def Index2(id: int, random: int = 0, queryParam1: int = 1): #just a random demo of mix path params.
    return {"message" : f'message with Blog with ID {id} {queryParam1}' }