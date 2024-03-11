#
# PlasmaFHIRClient
# Copyright (c) 2024 10xDevelopment LLC
#

import base64
from .FHIRClient import FHIRClient

class PlasmaFHIRClient(FHIRClient):

    def __init__(self, fhir_base_url):
        default_headers = {}
        super().__init__(fhir_base_url, None, default_headers)

    # Initialize the client with no auth...
    @staticmethod
    def for_no_auth(base_url):
        return PlasmaFHIRClient(base_url, None, None)

    # Initialize the client with a Bearer token...
    @staticmethod
    def for_bearer_token(base_url, access_token):
        return PlasmaFHIRClient(base_url, access_token, "Bearer")

    # Initialize the client for Basic Auth...
    @staticmethod
    def for_basic_auth(base_url, user, pwd):
        # Create the access token by combining user/pwd...
        access_token = user + ':' + pwd
        access_token = base64.b64encode(access_token.encode('utf-8')).decode('utf-8')
        return PlasmaFHIRClient(base_url, access_token, "Basic")

    # Read a patient by ID...
    def read_patient(self, patient_id):
        return self.read_resource("Patient", patient_id)