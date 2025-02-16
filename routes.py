"""
The contents of this file are property of pygate.org
Review the Apache License 2.0 for valid authorization of use
See https://github.com/pypeople-dev/pygate for more information
"""

# External imports
from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import JSONResponse

from service import Service

api_router = APIRouter()

@api_router.post("/api/organization")
async def user_details(request: Request):
    try:
        await Service.add_organization(request)
        return JSONResponse(content={"message": "Organization created"}, status_code=201)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@api_router.post("/api/organization-details")
async def user_details(request: Request):
    try:
        user = await Service.get_organization(request.get('organization'))
        user.pop('_id')
        return JSONResponse(content=user, status_code=201)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))