from datetime import datetime
from typing import Optional

from pydantic import BaseModel, PositiveInt

from timing.heplers import to_camel_case


class TimeInSchema(BaseModel):
    user_id: int
    hours: PositiveInt
    created_at: Optional[datetime]

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
