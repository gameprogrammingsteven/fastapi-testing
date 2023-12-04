from fastapi import APIRouter, status, Response
from enum import Enum 
from typing import Optional

router = APIRouter(
    prefix="/blog",
    tags=['getblog']
)

#tags and /blog prefix handled by router
@router.get('/all')
def get_all_with_pagesize(page: Optional[int] = None, pagesize: int = 11): #def value means optional.
    return {"msg" : f"All with pagesize: {pagesize} page: {page}"}

class BlogType(str, Enum):
    short = 'short'
    medium = 'med'
    long = 'long'


# @router.get('/blog/type/{type}', tags=['blog','comment'])
@router.get('/type/{type}')
def get_type(type: BlogType):
    return {"type of:" : f"type {type}"}

# @router.get('/blogid/{id}', status_code=status.HTTP_200_OK, tags=['blog'], summary="get blog with #", response_description="Description res")
@router.get('/{id}', status_code=status.HTTP_200_OK, summary="get blog with #", response_description="Description res")
def Index2(id: int):
    """
    Get blog id.

    - **id**: Required.
    """
    if(id > 11):
        status_code=status.HTTP_404_NOT_FOUND
        return {"e" : f'message with Blog with ID {id} not found' }
    else:
        return {"message" : f'message with Blog with ID {id}' }

# @app.get('/randdemopath+queryparam/{id}/comment/{anotherPathVariable}', status_code=404, tags=['comments','test']) #tags swagger break up sections
# def Index2(id: int, random: int = 0, queryParam1: int = 1): #just a random demo of mix path params.
#     return {"message" : f'message with Blog with ID {id} {queryParam1}' }