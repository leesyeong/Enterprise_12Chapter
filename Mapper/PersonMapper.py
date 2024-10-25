# 모든 매퍼의 인스턴스를 관리하는 매퍼 클래스
from Mapper import Mapper
from Mapper import ArtistMapper, ActorMapper

from Domain import Artist, Actor

class PersonMapper(Mapper):
    def __init__(self, gateway):
        self.artist_mapper = ArtistMapper(gateway)
        self.actor_mapper = ActorMapper(gateway)

    #region 1. Find
    def find(self, key):
        result = self.artist_mapper.find(key)
        if result is not None:
            return result
        result = self.actor_mapper.find(key)
        if result is not None:
            return result

        return None
    #endregion

    #region 2. Update
    def update(self, obj):
        self.mapperFor(obj).update(obj)

    def mapperFor(self, obj):
        if isinstance(obj, Artist):
            return self.artist_mapper
        elif isinstance(obj, Actor):
            return self.actor_mapper
        else:
            raise ValueError("Unknown object type")
    #endregion

    #region 3. Insert
    def insert(self, obj):
        return self.mapperFor(obj).insert(obj)
    #endregion

    #region 4. Delete
    def delete(self, obj):
        self.mapperFor(obj).delete(obj)