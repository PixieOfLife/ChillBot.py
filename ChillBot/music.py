from .requests import Request
from .exceptions import UserNotFound

class TrackItem:
    """Gets the track data"""
    def __init__(self, name: str, plays: int):
        self._name = name
        self._plays = plays
    
    def __str__(self):
        return f"<TrackItem name={self._name} tracks={self._tracks}>"
    
    @property
    def name(self) -> str:
        """The name of the track
        
           Type: str
        """
        return self._name
    
    @property
    def plays(self) -> int:
        """How many times it was played
        
           Type: str
        """
        return self._plays

class ArtistListItem:
    """Artist data list"""
    def __init__(self, artist: list):
        self._artist = artist
    
    def __str__(self):
        return f"<ArtistListItem name={self.name} tracks={self.tracks}>"
    
    @property
    def name(self) -> str:
        """The name of the artist
        
           Type: str
        """
        return self._artist.get('name')
    
    @property
    def tracks(self) -> list[TrackItem]:
        """Amount of tracks
        
           Type: dict
        """
        return [TrackItem(x, y) for x, y in self._artist.get('tracks').items()]

class MusicResponse:
    """Music data response from user ID"""
    def __init__(self, response: dict):
        self._response = response
    
    def __str__(self):
        return f"<MusicResponse id={self.id} artists={self.artists}>"

    @property
    def id(self) -> int:
        """The User ID it returns

           Type: int
        """
        return self._response.get('_id')
    
    @property
    def artists(self) -> list[ArtistListItem]:
        """Returns the list of artists

           Type: list
        """
        return [ArtistListItem(x) for x in self._response.get('artists')]


class Music:
    """Music class for requesting Music data"""
    
    @staticmethod
    async def get_top_ten(id: str):
        """Gets the top 10 music data request

           Returns: MusicResponse
        """
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