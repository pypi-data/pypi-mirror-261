from pydantic import BaseModel
from typing import List
from vbl_json_schema.models_unity import *

# Standard types and lists
class IDData(BaseModel):
    id: str

class Vector3Data(BaseModel):
    id: str
    value: Vector3

class Vector3List(BaseModel):
    id: str
    value: List[Vector3]

class ColorData(BaseModel):
    id: str
    value: Color

class ColorList(BaseModel):
    id: str
    value: List[Color]

class StringData(BaseModel):
    id: str
    value: str

class StringList(BaseModel):
    id: str
    value: List[str]

class FloatData(BaseModel):
    id: str
    value: float

class FloatList(BaseModel):
    id: str
    value: List[float]

class IntData(BaseModel):
    id: str
    value: int

class IntList(BaseModel):
    id: str
    value: List[int]

class BoolData(BaseModel):
    id: str
    value: bool

class BoolList(BaseModel):
    id: str
    value: List[bool]

# ID lists 
    
class IDList(BaseModel):
    id: List[str]

class IDListVector3Data(BaseModel):
    id: List[str]
    value: Vector3

class IDListVector3List(BaseModel):
    id: List[str]
    value: List[Vector3]

class IDListColorData(BaseModel):
    id: List[str]
    value: Color

class IDListColorList(BaseModel):
    id: List[str]
    value: List[Color]

class IDListStringData(BaseModel):
    id: List[str]
    value: str

class IDListStringList(BaseModel):
    id: List[str]
    value: List[str]

class IDListFloatData(BaseModel):
    id: List[str]
    value: float

class IDListFloatList(BaseModel):
    id: List[str]
    value: List[float]

class IDListIntData(BaseModel):
    id: List[str]
    value: int

class IDListIntList(BaseModel):
    id: List[str]
    value: List[int]

class IDListBoolData(BaseModel):
    id: List[str]
    value: bool

class IDListBoolList(BaseModel):
    id: List[str]
    value: List[bool]