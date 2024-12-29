from .requests import Request
from .exceptions import UserNotFound

class ArtistListItem:
    """Artist data list"""
    def __init__(self, artist: list):
        self._artist = artist
    
    def __call__(self):
        return self._artist
    
    @property
    def name(self) -> str:
        """The name of the artist
        
           Type: str
        """
        return self._artist.get('name')
    
    @property
    def tracks(self) -> dict:
        """Amount of tracks
        
           Type: dict
        """
        return self._artist.get('tracks')

class MusicResponse:
    """Music data response from user ID"""
    def __init__(self, response: dict):
        self._response = response
    
    def __call__(self):
        return self._response

    @property
    def id(self) -> int:
        """The User ID it returns

           Type: int
        """
        return self._response.get('_id')
    
    @property
    def artists(self):
        """Returns the list of artists

           Type: list
        """
        return [ArtistListItem(x) for x in self._response.get('artists')]


class Music:
    """Music class for requesting Music data"""
    
    @staticmethod
    async def get_top_ten(id: str):
        """Gets the top 10 music data request"""
        response = await Request(
            headers={"Content-Type": "application/json"},
            params={"user_id": id}
        ).GET(
            "/music"
        )

        if response.status == 404:
            raise UserNotFound()
        
        else:
            return MusicResponse(await response.json())