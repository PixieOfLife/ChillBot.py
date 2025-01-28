from .requests import Request
from .exceptions import UserNotFound

from dataclasses import dataclass

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
class TrackList:
    """Track data list"""

    tracks: list[TrackItem]
    """List of tracks
        
       Type: list[TrackItem]
    """

    def filter(self, name: str) -> TrackItem | None:
        """Filters the tracks

           Returns: TrackItem | None
        """

        data = [x for x in self.tracks if x.get('name').lower() == name.lower()]

        if len(data) == 0:
            return None

        return TrackItem(data[0].get('name'), data[0].get('plays'))

@dataclass(frozen=True)
class ArtistItem:
    """Gets the artist data"""

    name: str
    """The name of the artist
        
       Type: str
    """
    tracks: list[TrackItem]
    """Amount of tracks
        
       Type: list[TrackItem]
    """

@dataclass(frozen=True)
class ArtistList:
    """Artist data list"""

    artists: list[ArtistItem]
    """List of artists
        
       Type: list[ArtistItem]
    """

    def filter(self, name: str) -> ArtistItem | None:
        """Filters the artist

           Returns: ArtistItem | None
        """

        data = [x for x in self.artists if x.get('name').lower() == name.lower()]

        if len(data) == 0:
            return None
        
        return ArtistItem(data[0].get('name'), TrackList([TrackItem(x, y) for x, y in data[0].get('tracks').items()]))


@dataclass(frozen=True)
class MusicResponse:
    """Music data response from user ID"""

    id: int
    """The User ID it returns

       Type: int
    """
    artists: ArtistList
    """Returns the list of artists

       Type: ArtistList
    """


class Music:
    """Music class for requesting Music data"""
    
    @staticmethod
    async def get_top_ten(id: str | int):
        """Gets the top 10 music data request

           Returns: MusicResponse
        """
        response = await Request(
            headers={"Content-Type": "application/json"},
            params={"user_id": str(id)}
        ).GET(
            "/music"
        )

        if response.status == 404:
            raise UserNotFound()
        
        else:
            json_response = await response.json()

            return MusicResponse(
                json_response.get('_id'),
                ArtistList(
                    [ArtistItem(
                        x.get('name'),
                        TrackList(
                            [TrackItem(x, y) for x, y in x.get('tracks').items()]
                        )
                    ) for x in json_response.get('artists')]
                )
            )