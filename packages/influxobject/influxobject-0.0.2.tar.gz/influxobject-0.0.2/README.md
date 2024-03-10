# Influx Point

## Description

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


## Installation

To install the package use the pip package manager

```bash
    pip install influxobject==0.0.1
```

## Development


Tox is used as the test runner for this project. To run the tests use the following command

```bash
    tox

```bash
    tox -e py39
```

Build

```bash
python setup.py sdist
```

Publish

```bash
    twine upload dist/*
```
