# Person을 상속 받은 자식 도메인 객체
# 부모인 Person으로부터 name filed를, 최상위 객체로부터 id field를 상속받음
from Domain.Person import Person

class Actor(Person):
    def __init__(self,id=None, name=None, agency=None):
        super().__init__(id, name)
        self.agency = agency