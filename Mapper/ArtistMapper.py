# Artist 도메인 객체와 연관된 매퍼 클래스
from Mapper import AbstractPersonMapper, _MapperRegistry
from Domain import Artist

class ArtistMapper(AbstractPersonMapper):
    def __init__(self, gateway):
        super().__init__(gateway)
        self.__table_name = "Artist"

    #region 1. Find
    def find(self, id):
        return self.abstractFind(id)

    def load(self, obj, data_row):
        super().load(obj, data_row)
        obj.stage_name = data_row["stage_name"]
        obj.album_list = _MapperRegistry.album_mapper.findForArtist(obj.id)

    def createDomainObject():
        return Artist()
    #endregion

    #region 2. Update
    def save(self, obj, data_row):
        super().save(obj, data_row)
        data_row["stage_name"] = obj.stage_name
        self.saveAlbumList(obj)

    def saveAlbumList(self, obj):
        for album in obj.album_list:
            _MapperRegistry.album_mapper.save(album)
    #endregion