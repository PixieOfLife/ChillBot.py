from .requests import Request
from .exceptions import UserNotFound

class MusicResponse:
    """Music data response from user ID"""
    def __init__(self, response: dict):
        self._response = response
    
    def __call__(self):
        return self._response

    @property
    def id(self) -> int:
        """The User ID it returns\n
        Type: int
        """
        return self._response.get('_id')
    
    @property
    def artists(self) -> list:
        """Returns the list of artists\n
        Type: list
        """
        return self._response.get('artists')


class Music:
    """Music class for requesting Music data"""
    def __init__(self):
        super().__init__()
    
    async def get_top_ten(self, id: str):
        """Gets the top 10 music data request"""
        response = await Request(
            headers={"Content-Type": "application/json"}
        ).GET(
            "/music",
            {"user_id": id}
        )

        if response.status_code == 404:
            raise UserNotFound
        
        else:
            MusicResponse(response.json())