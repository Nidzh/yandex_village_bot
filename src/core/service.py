from src.integrations.http.client import HTTPClient


class BaseService:
    def __init__(self, http_client: HTTPClient = None):
        self.http_client = http_client
