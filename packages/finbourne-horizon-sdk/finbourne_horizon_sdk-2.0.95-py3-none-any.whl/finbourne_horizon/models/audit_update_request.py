# coding: utf-8

"""
    FINBOURNE Horizon API

    FINBOURNE Technology  # noqa: E501

    Contact: info@finbourne.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Any, Dict
from pydantic import BaseModel, Field, StrictStr

class AuditUpdateRequest(BaseModel):
    """
    An incoming request for a Horizon Update Event  # noqa: E501
    """
    id: StrictStr = Field(..., description="A unique ID identifiying the source of the event")
    user_id: StrictStr = Field(..., alias="userId", description="A unique ID identifiying who owns the schedule")
    scheduler_run_id: StrictStr = Field(..., alias="schedulerRunId", description="The GUID of the schedule run")
    start_time: datetime = Field(..., alias="startTime", description="When the run was started in UTC")
    message: StrictStr = Field(..., description="A descriptive message to accompany the status")
    __properties = ["id", "userId", "schedulerRunId", "startTime", "message"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> AuditUpdateRequest:
        """Create an instance of AuditUpdateRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AuditUpdateRequest:
        """Create an instance of AuditUpdateRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AuditUpdateRequest.parse_obj(obj)

        _obj = AuditUpdateRequest.parse_obj({
            "id": obj.get("id"),
            "user_id": obj.get("userId"),
            "scheduler_run_id": obj.get("schedulerRunId"),
            "start_time": obj.get("startTime"),
            "message": obj.get("message")
        })
        return _obj
