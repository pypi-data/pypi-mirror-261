import requests

from ..exceptions import WykopApiError


class ApiRequester:
    def __init__(self, url: str, token: str | None):
        self.url = url
        self.header = {
            "Authorization": f"Bearer {token}"
        } if token else {}

    def get(self, params: dict | None = None) -> dict:
        if params:
            params = {k: v for k, v in params.items() if v} 
        
        response = requests.get(self.url, params, headers=self.header)
        if response.status_code >= 300:
            raise WykopApiError(response.json()["error"])
        
        return response.json()
    
    def post(self, data: dict | None = None) -> dict | None:
        if data:
            data = {k: v for k, v in data.items() if v}
        
        response = requests.post(
            self.url,
            json={"data": data} if data else None,
            headers=self.header
        )

        if response.status_code >= 300:
            raise WykopApiError(response.json()["error"])
        
        return response.json() if response.text else None
    

    def put(self, data: dict) -> dict:
        response = requests.put(self.url, json={"data": data}, headers=self.header)

        if response.status_code >= 300:
            raise WykopApiError(response.json()["error"])
        
        return response.json()
    
    def delete(self):
        response = requests.delete(self.url, headers=self.header)

        if response.status_code >= 300:
            raise WykopApiError(response.json()["error"])
