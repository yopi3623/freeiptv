#!/usr/bin/python3

import requests
import re

print('#EXTM3U')
print('#EXT-X-VERSION:3')
print('#EXT-X-INDEPENDENT-SEGMENTS')
print('#EXT-X-STREAM-INF:CODECS="avc1.640029,mp4a.40.2",AVERAGE-BANDWIDTH=4611200,RESOLUTION=1280x720,FRAME-RATE=50.0,BANDWIDTH=7208960')

s = requests.Session()
response = s.get(f'https://hdfauth.ftven.fr/esi/TA?url=https://live-event.ftven.fr/dai/v1/master/f6695408824c1f922e63365d0de48c5fa3251476/events_RG_1/out/v1/a03e33307b5e42998022fd5f83cb55d8/index_france-domtom.m3u8')

string = response.text
response2 = s.get(string)

pattern = re.compile(r'/([\da-fA-F-]+?)/\d\.m3u8')
match = pattern.search(response2.text)
sessid = match.group(1)

new_string = string.replace("master", "manifest")
new_string2 = new_string.replace("out/v1/a03e33307b5e42998022fd5f83cb55d8/index_france-domtom.m3u8", f'{sessid}/4.m3u8')
print(new_string2)
