#
# PlasmaPlatformClient
# Copyright (c) 2024 10xDevelopment LLC
#

import base64
from .RESTClient import RESTClient

class FHIRClient(RESTClient):
    def __init__(self, base_url, access_token, access_token_type, default_headers = {}):
        # Initialize default headers...
        default_headers["accept"] = "application/json"
        default_headers["Content-Type"] = "application/json"

        super().__init__(base_url, access_token, access_token_type, default_headers)

    # Initialize the client with no auth...
    @staticmethod
    def for_no_auth(base_url):
        return FHIRClient(base_url, None, None)

    # Initialize the client with a Bearer token...
    @staticmethod
    def for_bearer_token(base_url, access_token):
        return FHIRClient(base_url, access_token, "Bearer")

    # Initialize the client for Basic Auth...
    @staticmethod
    def for_basic_auth(base_url, user, pwd):
        # Create the access token by combining user/pwd...
        access_token = user + ':' + pwd
        access_token = base64.b64encode(access_token.encode('utf-8')).decode('utf-8')
        return FHIRClient(base_url, access_token, "Basic")

    # Construct the FHIR URL...
    def __get_fhir_url(self, resourceType, resourceId = None, historyVersion = None):
        url = self.base_url + '/' + resourceType
        if resourceId:
            url += '/' + resourceId

        if historyVersion:
            url += '/_history/' + historyVersion

        return url

    # TODO: __get_fhir_search_url

    # Get the FHIR server's CapabilityStatement...
    def get_capability_statement(self):
        url = self.__get_fhir_url("metadata")
        return self.get_json(url)

    # TODO: create

    # Create a FHIR resource...
    def create_resource(self, resourceType, data):
        url = self.__get_fhir_url(resourceType)
        return self.post_json(url, data)

    # Read a FHIR resource...
    def read(self, resourceType, resourceId):
        url = self.__get_fhir_url(resourceType, resourceId)
        return self.get_json(url)

    # Read full history of a resource by ID
    def read_all_history(self, resourceType, resourceId):
        url = self.__get_fhir_url(resourceType, resourceId, "_history")
        return self.get_json(url)

    # Read a specific version of a resource by ID
    def read_history_by_version(self, resourceType, resourceId, version):
        url = self.__get_fhir_url(resourceType, resourceId, "_history", version)
        return self.get_json(url)

    # Update a FHIR resource...
    def update(self, resourceType, resourceId, data):
        url = self.__get_fhir_url(resourceType, resourceId)
        return self.put_json(url, data)

    # Deletes the given resource. Resource must have an id set.
    def delete(self, resource):
        return self.delete_by_id(resource.resourceType, resource.id)

    # Delete a FHIR resource...
    def delete_by_id(self, resourceType, resourceId):
        url = self.__get_fhir_url(resourceType, resourceId)
        return self.delete_json(url)

    # Search for a FHIR resource...
    def search(self, resourceType, params):
        url = self.__get_fhir_url(resourceType)
        return self.get_json(url, params)

    # TODO: search_resource (and filter bundle)


