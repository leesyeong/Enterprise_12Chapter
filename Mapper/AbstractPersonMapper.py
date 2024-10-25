# 모든 하위 매퍼가 상속받는 추상 매퍼 클래스

from Mapper import Mapper

class AbstractPersonMapper(Mapper):
    def __init__(self, gateway):
        super().__init__(gateway)

    #region 1. Find
    def load(self, obj, data_row):
        super().load(obj, data_row)
        obj.name = data_row["name"]
    #endregion

    #region 2. Update
    def save(self, obj, data_row):
        super().save(obj, data_row)
        data_row["name"] = obj.name
    #endregion