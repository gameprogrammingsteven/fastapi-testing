from fastapi import APIRouter, status, Response
from enum import Enum 
from typing import Optional

router = APIRouter(
    prefix="/blog",
    tags=['post Blog']
)

@router.post('/')
def create_blog():
    pass

