from Mapper import AbstractMapper
from Mapper import _MapperRegistry

class TrackMapper(AbstractMapper):
    def __init__(self, gateway):
        super().__init__(gateway)
        self.__table_name = "Track"

    #region 1. Find
    def load(self, obj, data_row):
        super().load(obj, data_row)
        obj.title = data_row["title"]
        obj.track_num = data_row["track_num"]

    def findForAlbum(self, album_id):
        filter = f"artist_id = {album_id}"
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
        data_row['track_num'] = obj.track_num
    #endregion