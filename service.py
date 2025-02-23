"""
The contents of this file are property of pygate.org
Review the Apache License 2.0 for valid authorization of use
See https://github.com/pypeople-dev/pygate for more information
"""

from database import db

class Service:
    organization_details_collection = db.get_collection('organization-details')

    async def add_organization(request):
        """
        Add a new user.
        """
        try:
            user_data = await request.json()
            if Service.organization_details_collection.find_one({'organization': user_data.get('organization')}):
                raise ValueError("organization already exists") 
            Service.organization_details_collection.insert_one(user_data)
        except Exception as e:
            raise

    @staticmethod
    async def get_organization(organization):
        """
        Retrieve simple organization details.
        """
        try:
            organization = Service.organization_details_collection.find_one({'organization': organization})
            if not organization:
                raise ValueError("organization not found")
            return organization
        except Exception as e:
            raise
