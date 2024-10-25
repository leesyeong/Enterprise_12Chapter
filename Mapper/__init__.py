from .Mapper import Mapper
from .AbstractPersonMapper import AbstractPersonMapper
from .ArtistMapper import ArtistMapper
from .ActorMapper import ActorMapper

from .AbstractMapper import AbstractMapper
from .AlbumMapper import AlbumMapper
from .TrackMapper import TrackMapper

__all__ = ["Mapper", "AbstractPersonMapper", "ArtistMapper", "ActorMapper", "AbstractMapper", "AlbumMapper", "TrackMapper"]

class MapperRegister:
    def __init__(self):
        self.album_mapper = AlbumMapper()
        self.artist_mapper = ArtistMapper()

_MapperRegistry = MapperRegister()
