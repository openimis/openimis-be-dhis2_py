# DHIS2 program
# Copyright Patrick Delcoix <patrick@pmpd.eu>
# # FROM https://github.com/dhis2/dhis2-python/blob/main/dhis2_core/src/dhis2/e2b/models/e2b.py
from typing import Dict, List, Optional, Union, Tuple
from datetime import datetime, date
from uuid import uuid4
from pydantic import  BaseModel, ValidationError, validator, Field, AnyUrl, EmailStr
from dhis2.utils import *
from .dhis2Enum import *
from .dhis2Type import *


   

class EventDataValue(BaseModel):
    created: Optional[datetimeStr]
    lastUpdated: Optional[datetimeStr]
    dataElement: uid
    value: str
    valueType: Optional[ValueType]
    providedElsewhere: Optional[bool]
    storedBy: Optional[DHIS2Ref]



class Event(BaseModel):
    created: Optional[datetimeStr]
    lastUpdated: Optional[datetimeStr]
    event: Optional[uid]
    program: uid
    programStage: uid
    trackedEntityInstance: uid
    orgUnit: uid
    status: str
    dueDate: Optional[dateStr]
    eventDate: dateStr
    completedDate: Optional[dateStr]
    storedBy: Optional[DHIS2Ref]
    dataValues: Union[Dict[str, EventDataValue], List[EventDataValue]] = []

class Enrollment(BaseModel):
    created: Optional[datetimeStr]
    lastUpdated: Optional[datetimeStr]
    enrollment: Optional[uid]
    trackedEntityInstance: Optional[uid] # optionnal only if part of the TEI creation
    orgUnit: uid
    storedBy: Optional[DHIS2Ref]
    status: str
    incidentDate: dateStr
    enrollmentDate: dateStr
    events: List[Event] = []
    attributes: Union[Dict[str, AttributeValue], List[AttributeValue]] = []
    program: uid



class TrackedEntityInstance(BaseModel):
    created: Optional[datetimeStr]
    lastUpdated: Optional[datetimeStr]
    trackedEntityInstance: Optional[uid]
    trackedEntityType: uid
    orgUnit: uid
    storedBy: Optional[DHIS2Ref]
    enrollments: List[Enrollment] = []
    attributes: Union[Dict[str, AttributeValue], List[AttributeValue]] = []
    #validator('trackedEntity','orgUnit')



class TrackedEntityInstanceBundle(BaseModel):
    trackedEntityInstances:List[TrackedEntityInstance]

class EventBundle(BaseModel):
    events:List[Event]

class EnrollmentBundle(BaseModel):
    enrollments:List[Enrollment]





 



