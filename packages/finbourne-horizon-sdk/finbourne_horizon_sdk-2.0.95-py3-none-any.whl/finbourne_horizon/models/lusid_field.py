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
from pydantic import BaseModel, Field, StrictStr, conlist, constr

class LusidField(BaseModel):
    """
    A field on a LUSID entity  # noqa: E501
    """
    field_name: constr(strict=True, min_length=1) = Field(..., alias="fieldName", description="The name of the LUSID field.")
    default_value: Optional[StrictStr] = Field(None, alias="defaultValue", description="The default value for the field.")
    vendor_packages: conlist(StrictStr) = Field(..., alias="vendorPackages", description="The vendor package that contributes to this LUSID field.")
    vendor_namespaces: conlist(StrictStr) = Field(..., alias="vendorNamespaces", description="The vendor namespace that contributes to this LUSID field.")
    vendor_fields: conlist(StrictStr) = Field(..., alias="vendorFields", description="The underlying fields on the vendor package that contribute to this LUSID field")
    transformation_description: Optional[StrictStr] = Field(None, alias="transformationDescription", description="A description of how the vendor package's field(s) get mapped to the LUSID field")
    __properties = ["fieldName", "defaultValue", "vendorPackages", "vendorNamespaces", "vendorFields", "transformationDescription"]

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
    def from_json(cls, json_str: str) -> LusidField:
        """Create an instance of LusidField from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if default_value (nullable) is None
        # and __fields_set__ contains the field
        if self.default_value is None and "default_value" in self.__fields_set__:
            _dict['defaultValue'] = None

        # set to None if transformation_description (nullable) is None
        # and __fields_set__ contains the field
        if self.transformation_description is None and "transformation_description" in self.__fields_set__:
            _dict['transformationDescription'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LusidField:
        """Create an instance of LusidField from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LusidField.parse_obj(obj)

        _obj = LusidField.parse_obj({
            "field_name": obj.get("fieldName"),
            "default_value": obj.get("defaultValue"),
            "vendor_packages": obj.get("vendorPackages"),
            "vendor_namespaces": obj.get("vendorNamespaces"),
            "vendor_fields": obj.get("vendorFields"),
            "transformation_description": obj.get("transformationDescription")
        })
        return _obj
