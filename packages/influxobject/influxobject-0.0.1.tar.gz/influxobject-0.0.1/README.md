# Influx Point

This module enables the creation of an influx point object that can be transformed into either a JSON or LineProtocol format.

## Uage

```python

 influx_point = InfluxPoint()
        influx_point.set_measurement("measurement")
        influx_point.set_tags({"tag1": "value1"})
        influx_point.set_fields({"field1": 1, "field2": 2})
        influx_point.set_timestamp(datetime.datetime(2021, 1, 1))\
        
        print(influx_point.to_json())

            # {
            #     "measurement": "measurement",
            #     "tags": {"tag1": "value1"},
            #     "fields": {"field1": 1, "field2": 2},
            #     "timestamp": 1609455600,
            # }
        
        print(influx_point.to_line_protocol())

            # "measurement,tag1=value1 field1=1,field2=2 1609455600"
```
