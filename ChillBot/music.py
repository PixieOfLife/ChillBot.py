from .requests import Request
from .exceptions import UserNotFound

from dataclasses import dataclass, field

@dataclass(frozen=True)
class TrackItem:
    """Gets the track data"""

    name: str
    """The name of the track
        
       Type: str
    """
    plays: int
    """How many times it was played
        
       Type: int
    """


@dataclass(frozen=True)
class ArtistListItem:
    """Artist data list"""

    name: str
    """The name of the artist
        
       Type: str
    """
    tracks: list[TrackItem]
    """Amount of tracks
        
       Type: list[TrackItem]
    """


@dataclass(frozen=True)
class MusicResponse:
    """Music data response from user ID"""

    id: int
    """The User ID it returns

       Type: int
    """
    artists: list[ArtistListItem]
    """Returns the list of artists

       Type: list[ArtistListItem]
    """


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
            json_response = await response.json()

            return MusicResponse(
                json_response.get('_id'),
                [ArtistListItem(
                    x.get('name'),
                    [TrackItem(x, y) for x, y in x.get('tracks').items()]
                ) for x in json_response.get('artists')]
            )