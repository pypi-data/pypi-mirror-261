from typing import Dict, Optional, Union
from datetime import datetime
import re


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
        self.validate()
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
        self.validate()
        
        return {
            "measurement": self.measurement,
            "tags": self.tags,
            "fields": self.fields,
            "timestamp": self.timestamp.timestamp() if self.timestamp else None,
        }

    def validate(self) -> None:
        errors = []
        if self.measurement is None:
            errors.append("Measurement is not set")
        if self.timestamp is None:
            errors.append("Timestamp is not set")
        if not self.fields:
            errors.append("Fields are not set")
        if not self.tags:
            errors.append("Tags are not set")
        if errors:
            raise ValueError(", ".join(errors))
        
    def from_json(self, json: Dict[str, Union[str, Dict[str, str], Dict[str, Union[int, float, str]], str]]) -> None:
        measurement = json.get("measurement")
        tags = json.get("tags", {})
        fields = json.get("fields", {})
        timestamp = datetime.fromtimestamp(json.get("timestamp")) if json.get("timestamp") else None
        
        self.measurement = measurement
        self.tags = tags
        self.fields = fields
        self.timestamp = timestamp
        
    def parse_line_protocol(self, line_protocol: str) -> None:
        # Regex split on white space only that are not escaped with \
        measurement_tags, fields, epoch = re.split(r'(?<!\\)\s', line_protocol)
        self.set_timestamp(datetime.fromtimestamp(convert_to_seconds(int(epoch))))

        # Split the measurement and tags
        measurement, tags = re.split(r'(?<!\\),', measurement_tags, 1)
        self.set_measurement(measurement)
        # For each tag
        tags = re.split(r'(?<!\\),', tags)
        # Turn it into a dictionary
        for tag in tags:
            key, value = re.split(r'(?<!\\)=', tag)
            self.add_tag(key, value)

        # For each field
        fields = re.split(r'(?<!\\),', fields)
        # Turn it into a dictionary
        for field in fields:
            key, value = re.split(r'(?<!\\)=', field)
            self.add_field(key, value)

        # Map field value to int or float if possible
        for k, v in self.fields.items():
            if v.isdigit():
                self.fields[k] = int(v)
            elif v.replace(".", "", 1).isdigit():
                self.fields[k] = float(v)
        # Convert a int timestamp to a datetime object 
        # open('test.txt', 'w').write(f"{epoch} + {datetime.fromtimestamp(int(epoch))}")
        self.validate()
        

def convert_to_seconds(timestamp: int) -> float:
    length = len(str(timestamp))
    if length >= 19:  # nanoseconds
        return timestamp / 1_000_000_000
    elif length >= 16:  # microseconds
        return timestamp / 1_000_000
    elif length >= 13:  # milliseconds
        return timestamp / 1_000
    elif length >= 10:  # seconds
        return timestamp
    else:
        raise ValueError("Timestamp value is too short to be valid")