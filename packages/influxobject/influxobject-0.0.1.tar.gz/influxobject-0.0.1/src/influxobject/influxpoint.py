from typing import Dict, Optional, Union
from datetime import datetime


class InfluxPoint:
    def __init__(self) -> None:
        self.measurement: Optional[str] = None
        self.tags: Dict[str, str] = {}
        self.fields: Dict[str, Union[int, float, str]] = {}
        self.timestamp: Optional[datetime] = None

    def set_measurement(self, measurement: str) -> None:
        self.measurement = measurement

    def set_tags(self, tags: Dict[str, str]) -> None:
        self.tags = tags

    def set_fields(self, fields: Dict[str, Union[int, float, str]]) -> None:
        self.fields = fields

    def set_timestamp(self, timestamp: datetime) -> None:
        if not isinstance(timestamp, datetime):
            raise ValueError("Timestamp must be a datetime object")
        self.timestamp = timestamp

    def to_line_protocol(self) -> str:
        if self.measurement is None:
            raise ValueError("Measurement is not set")
        if self.timestamp is None:
            raise ValueError("Timestamp is not set")
        tags = ",".join([f"{k}={v}" for k, v in self.tags.items()])
        fields = ",".join([f"{k}={v}" for k, v in self.fields.items()])
        return f"{self.measurement},{tags} {fields} {int(self.timestamp.timestamp())}"

    def __str__(self) -> str:
        return self.to_line_protocol()

    def add_tag(self, key: str, value: str) -> None:
        self.tags[key] = value

    def add_field(self, key: str, value: Union[int, float, str]) -> None:
        self.fields[key] = value

    def remove_tag(self, key: str) -> None:
        del self.tags[key]

    def remove_field(self, key: str) -> None:
        del self.fields[key]

    def to_json(
        self,
    ) -> Dict[str, Union[str, Dict[str, str], Dict[str, Union[int, float, str]], str]]:
        return {
            "measurement": self.measurement,
            "tags": self.tags,
            "fields": self.fields,
            "timestamp": self.timestamp.timestamp() if self.timestamp else None,
        }
