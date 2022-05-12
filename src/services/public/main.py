# /src/services/public/main.py

from fastapi import Depends, APIRouter, Request, Response, HTTPException

router = APIRouter(prefix='/user', tags=["Users"])