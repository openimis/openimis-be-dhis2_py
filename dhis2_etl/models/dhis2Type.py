# Copyright Patrick Delcoix <patrick@pmpd.eu>
# dhis2 types
from pydantic import constr
from pydantic import  BaseModel
from typing import List, Optional
from .dhis2Enum import ValueType

uid = constr(regex="^[a-zA-Z][a-zA-Z0-9]{10}$")
dateStr = constr(regex="^\d{4}-\d{2}-\d{2}$")
datetimeStr = constr(regex="^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}$")
str50 = constr(regex="^.{0,50}$")
str130 = constr(regex="^.{0,130}$")
str150 = constr(regex="^.{0,150}$")
str230  = constr(regex="^.{0,230}$")
str255  = constr(regex="^.{0,255}$")

class DHIS2Ref(BaseModel):
    id: Optional[uid]
    code: Optional[str]

class DeltaDHIS2Ref(BaseModel):
    additions: List[DHIS2Ref] = []
    deletions: List[DHIS2Ref] = []

class AttributeValue(BaseModel):
    created: Optional[datetimeStr]
    lastUpdated: Optional[datetimeStr]
    attribute: uid
    value: str
    storedBy: Optional[DHIS2Ref]

