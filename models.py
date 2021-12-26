
from typing import List, Optional
from uuid import UUID, uuid4
from pydantic import BaseModel

from enum import Enum

class Gender(str,Enum):
    male="male"
    female="female"

class Role(str,Enum):
    student="student"
    user="user"
    admin="admin"
    



class User(BaseModel):
     id: Optional[UUID] = uuid4()
     firstName:str
     lastName:str
     middleName:Optional[str]
     gender:Gender
     roles:List[Role]


class UserUpdateRequest(BaseModel):
    firstName:Optional[str]
    lastName:Optional[str]
    middleName:Optional[str]
    gender:Optional[Gender]
    roles:Optional[List[Role]]