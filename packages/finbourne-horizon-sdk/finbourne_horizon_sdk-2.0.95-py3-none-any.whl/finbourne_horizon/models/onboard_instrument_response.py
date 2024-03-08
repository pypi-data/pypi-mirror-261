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


from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist

class OnboardInstrumentResponse(BaseModel):
    """
    Simplified structure converted from the LUSID UpsertInstrumentReponse  # noqa: E501
    """
    href: Optional[StrictStr] = Field(None, description="The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.")
    values: conlist(StrictStr) = Field(..., description="The instruments which have been successfully updated or created.")
    failed: Dict[str, StrictStr] = Field(..., description="The instruments that could not be updated or created or were left unchanged without error along with a reason for their failure.")
    __properties = ["href", "values", "failed"]

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
    def from_json(cls, json_str: str) -> OnboardInstrumentResponse:
        """Create an instance of OnboardInstrumentResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if href (nullable) is None
        # and __fields_set__ contains the field
        if self.href is None and "href" in self.__fields_set__:
            _dict['href'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OnboardInstrumentResponse:
        """Create an instance of OnboardInstrumentResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OnboardInstrumentResponse.parse_obj(obj)

        _obj = OnboardInstrumentResponse.parse_obj({
            "href": obj.get("href"),
            "values": obj.get("values"),
            "failed": obj.get("failed")
        })
        return _obj
