### name 필드를 가진 Person 도메인 객체 (부모)
from Domain import DomainObject

class Person(DomainObject):
    def __init__(self, id = None, name = None):
        super().__init__(id)
        self.name = name
