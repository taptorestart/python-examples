from influxdb import InfluxDBClient
import datetime

json_body = [
    {
        "measurement": "temperature",
        "tags": {
            "country": "Korea",
            "location": "Seoul"
        },
        "time": datetime.datetime.now(),
        "fields": {
            "Celsius": -7.0
        }
    }
]

client = InfluxDBClient(host='host', port=8086, username='admin', password='verysecret!', database='weather')
client.write_points(json_body)
query_result = client.query('SELECT * FROM "weather"."autogen"."temperature"')
print(query_result)

'''
# result
ResultSet({'('temperature', None)': [{'time': '2022-01-12T21:29:51.348695Z', 'Celsius': -7.0, 'country': 'Korea', 'location': 'Seoul'}]})
'''
