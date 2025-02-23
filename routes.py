"""
The contents of this file are property of pygate.org
Review the Apache License 2.0 for valid authorization of use
See https://github.com/pypeople-dev/pygate for more information
"""

# External imports
from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import JSONResponse

from service import Service

router = APIRouter()

@router.post("/api/organization")
async def user_details(request: Request):
    try:
        await Service.add_organization(request)
        return JSONResponse(content={"message": "Organization created"}, status_code=201)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/api/organization-details")
async def organization_details(request: Request):
    try:
        request_data = await request.json()
        organization = await Service.get_organization(request_data.get('organization'))
        organization.pop('_id')
        return JSONResponse(content=organization, status_code=200)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")