import datetime
import unittest

from influxobject.influxpoint import InfluxPoint


class TestSimple(unittest.TestCase):

    # def test_add(self):
    #     self.assertEqual((InfluxObject(5) + InfluxObject(6)).value, 11)

    # def test_create(self):
    #     influx_object = InfluxObject(5)
    #     self.assertEqual(InfluxObject(5).value, 5)

    def test_init(self):
        influx_point = InfluxPoint()
        influx_point.set_measurement("measurement")
        self.assertEqual(influx_point.measurement, "measurement")

    def test_tags(self):
        influx_point = InfluxPoint()
        influx_point.tags = {"tag1": "value1"}
        self.assertEqual(influx_point.tags, {"tag1": "value1"})

        influx_point.add_tag("tag2", "value2")
        self.assertEqual(influx_point.tags, {"tag1": "value1", "tag2": "value2"})

        influx_point.remove_tag("tag1")
        self.assertEqual(influx_point.tags, {"tag2": "value2"})

    def test_fields(self):
        influx_point = InfluxPoint()
        influx_point.fields = {"field1": 1}
        self.assertEqual(influx_point.fields, {"field1": 1})

        influx_point.add_field("field2", 2)
        self.assertEqual(influx_point.fields, {"field1": 1, "field2": 2})

        influx_point.remove_field("field1")
        self.assertEqual(influx_point.fields, {"field2": 2})

    def test_timestamp(self):
        influx_point = InfluxPoint()
        influx_point.timestamp = "2021-01-01T00:00:00Z"
        self.assertEqual(influx_point.timestamp, "2021-01-01T00:00:00Z")

    def test_line_protocol(self):
        influx_point = InfluxPoint()
        influx_point.set_measurement("measurement")
        influx_point.set_tags({"tag1": "value1"})
        influx_point.set_fields({"field1": 1, "field2": 2})
        influx_point.set_timestamp(datetime.datetime(2021, 1, 1))
        self.assertEqual(
            influx_point.to_line_protocol(),
            "measurement,tag1=value1 field1=1,field2=2 1609455600",
        )

    def test_json(self):
        influx_point = InfluxPoint()
        influx_point.set_measurement("measurement")
        influx_point.set_tags({"tag1": "value1"})
        influx_point.set_fields({"field1": 1, "field2": 2})
        influx_point.set_timestamp(datetime.datetime(2021, 1, 1))
        self.assertEqual(
            influx_point.to_json(),
            {
                "measurement": "measurement",
                "tags": {"tag1": "value1"},
                "fields": {"field1": 1, "field2": 2},
                "timestamp": 1609455600,
            },
        )

        self.assertEqual(
            influx_point.to_line_protocol(),
            "measurement,tag1=value1 field1=1,field2=2 1609455600",
        )


if __name__ == "__main__":
    unittest.main()
