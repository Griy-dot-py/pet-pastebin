from datetime import timedelta
from flasgger import Schema, fields
from marshmallow.validate import Range
from marshmallow import post_load


class TimeDeltaSchema(Schema):
    months = fields.Int(validate=[Range(max=11)])
    days = fields.Int(validate=[Range(max=30)])
    hours = fields.Int(validate=[Range(max=23)])
    minutes = fields.Int(validate=[Range(max=59)])
    
    @post_load
    def convert_into_timedelta(self, data: dict, **kwargs) -> timedelta|None:
        if not data:
            return None
        if "months" in data:
            as_days = data.pop("months") * 30
            if "days" not in data:
                data["days"] = 0
            data["days"] += as_days
        return timedelta(**data)
