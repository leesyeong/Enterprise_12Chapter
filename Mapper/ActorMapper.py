# Actor 도메인 객체와 연관된 매퍼 클래스
from Mapper import AbstractPersonMapper
from Domain import Actor

class ActorMapper(AbstractPersonMapper):
    def __init__(self,gateway):
        super().__init__(gateway)
        self.__table_name = "Actor"

    #region 1. Find
    def find(self, id):
        return self.abstractFind(id)

    def load(self, obj, data_row):
        super().load(obj, data_row)
        obj.agency = data_row["agency"]

    def CreateDomainObject():
        return Actor()
    #endregion

    #region 2. Update
    def save(self, obj, data_row):
        super().save(obj, data_row)
        data_row["agency"] = obj.agency
    #endregion