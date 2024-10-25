from Mapper import Mapper, _MapperRegistry

class AlbumMapper(Mapper):
    def __init__(self, gateway):
        super().__init__(gateway)
        self.__table_name = "Album"

    #region 1. Find
    def load(self, obj, data_row):
        super().load(obj, data_row)
        obj.title = data_row["title"]
        obj.release_date = data_row["release_date"]
        obj.track_list = _MapperRegistry.track_mapper.findForAlbum(obj.id)

    def findForArtist(self, artist_id):
        filter = f"artist_id = {artist_id}"
        rows = self.table.select(filter)
        result = []
        for row in rows:
            result.append(self.load(row))
        return result
    #endregion

    #region 2. Update
    def save(self, obj, data_row):
        super().save(obj, data_row)
        data_row['title'] = obj.title
        data_row['release_date'] = obj.release_date
        self.saveTrackList(obj)

    def saveTrackList(self, obj):
        for track in obj.track_list:
            _MapperRegistry.track_mapper.save(track)
    #endregion