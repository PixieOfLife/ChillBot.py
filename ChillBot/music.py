from .requests import Request
from .exceptions import UserNotFound

class MusicResponse:
    def __init__(self, response: dict):
        self._response = response

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
    def __init__(self):
        super().__init__()
    
    async def get_top_ten(self, id: str):
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