from dataclasses import dataclass
from http import HTTPStatus

from .exceptions import UserNotFound
from .requests import Request


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

        data: TrackItem | None = next(
            (x for x in self.tracks if x.name.lower() == name.lower()), None
        )

        return data


@dataclass(frozen=True)
class ArtistItem:
    """Gets the artist data"""

    name: str
    """The name of the artist
        
       Type: str
    """
    tracks: TrackList
    """Amount of tracks
        
       Type: TrackList
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

        data: ArtistItem | None = next(
            (artist for artist in self.artists if artist.name.lower() == name.lower()),
            None,
        )
        return data


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
    async def get_top_ten(id: str | int) -> MusicResponse:
        """Gets the top 10 music data request

        Returns: MusicResponse
        """
        response = await Request(
            headers={"Content-Type": "application/json"},
            params={"user_id": str(id)}
        ).GET(
            "/music"
        )

        if response.status == HTTPStatus.NOT_FOUND:
            raise UserNotFound()

        json_response = await response.json()

        return MusicResponse(
            id=json_response["_id"],
            artists=ArtistList(
                [
                    ArtistItem(
                        name=artist_data["name"],
                        tracks=TrackList(
                            [
                                TrackItem(name=track_name, plays=track_plays)
                                for track_name, track_plays in artist_data[
                                    "tracks"
                                ].items()
                            ]
                        ),
                    )
                    for artist_data in json_response.get("artists", [])
                ]
            ),
        )
