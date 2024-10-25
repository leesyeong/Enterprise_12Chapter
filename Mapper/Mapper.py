# 최상위 Mapper 클래스
import uuid

class Mapper:
    def __init__(self, gateway):
        self.gateway = gateway  # public variable
        self.__table_name = None # private variable(Name Mangling)

    @property
    def table(self):
        if self.__table_name not in self.gateway:
            return None
        return self.gateway[self.__table_name]

    #region 1. Find
    def abstractFind(self, id):
        data_row = self.findRow(id)

        if data_row is None:
            return None
        else:
            obj = self.createDomainObject()
            self.load(obj, data_row)
            return obj

    def findRow(self, id):
        filter = f"id = {id}"
        results = self.table.select(filter)

        if len(results) == 0:
            return None
        else:
            return results[0]

    def load(self, obj, data_row):
        obj.id = data_row["id"]

    def createDomainObject(self):
        # 자식 클래스에서 구현되므로 부모 클래스에서는 NotImplementedError를 발생시킴
        raise NotImplementedError("createDomainObject() must be implemented in subclass")
    #endregion

    #region 2. Update
    def update(self, obj):
        self.save(obj, self.findRow(obj.id))

    def save(self, obj, data_row):
        data_row["id"] = obj.id
    #endregion

    #region 3. Insert
    def insert(self, obj):
        data_row = self.table.newRow()
        obj.id = uuid.uuid4()
        data_row["id"] = obj.id
        self.save(obj, data_row)
        self.table.Rows.Add(data_row)
        return obj.id
    #endregion

    #region 4. Delete
    def delete(self, obj):
        data_row = self.findRow(obj.id)
        data_row.Delete()
    #endregion
