import sys
from urllib import quote
import base64
import hmac
from hashlib import sha1

url = """
Action=QueryMetric&period=60&StartTime=2016-02-02T10:33:56Z
&Dimensions={instanceId:'i-23gp0zfjl'}&Timestamp=2016-02-04T03:17:29Z&Project=acs_ecs
&SignatureVersion=1.0&Format=JSON&SignatureNonce=53fddcfe-422a-4177-b983-e33981c9084c
&Version=2015-10-20&AccessKeyId=TestId&Metric=CPUUtilization&SignatureMethod=HMAC-SHA1&RegionId=cn
"""
parameters = {
    'Format': 'JSON',
    'Version': "2015-10-20",
    'SignatureVersion': '1.0',
    'SignatureMethod': 'HMAC-SHA1',
    'SignatureNonce': "530b9e7a-71e5-4744-8548-77c5df29b8cb",
    'Timestamp': '2016-02-04T03:17:29Z',
    'Metric':'CPUUtilization',
    'period':'60',
    'Action':'QueryMetric',
    "AccessKeyId":"TestId",
    "RegionId":'cn',
    'Dimensions':"{instanceId:'i-23gp0zfjl'}",
    'Project':'acs_ecs',
    'StartTime':'2016-02-02T10:33:56Z'
}

def percent_encode(line):
    if not isinstance(line, str):
        return line

    s = line


    #if sys.stdin.encoding is None and sys.getfilesystemencoding() is None:
        #s = line.decode().encode('utf8')
    #elif sys.stdin.encoding is None and sys.getfilesystemencoding():
        #s = line.decode(sys.getfilesystemencoding()).encode('utf8')
    #else:
        #s = line.decode(sys.stdin.encoding).encode('utf8')
    res = quote(s, '')
    res = res.replace('+', '%20')
    res = res.replace('*', '%2A')
    res = res.replace('%7E', '~')
    return res


sortedParameters = sorted(list(parameters.items()),
                          key=lambda items: items[0])

canonicalizedQueryString = ''
for k, v in sortedParameters:
    canonicalizedQueryString += '&' + percent_encode(k) \
        + '=' + percent_encode(v)
stringToSign = 'GET&%2F&' + percent_encode(canonicalizedQueryString[1:])
print(stringToSign)
#GET&%2F&AccessKeyId%3DTestId%26Action%3DQueryMetric%26Format%3DJSON%26Metric%3DCPUUtilization%26RegionId%3Dcn%26SignatureMethod%3DHMAC-SHA1%26SignatureNonce%3D53fddcfe-422a-4177-b983-e33981c9084c%26SignatureVersion%3D1.0%26TimeStamp%3D2016-02-04T03%253A17%253A29Z%26Version%3D2015-10-20%26period%3D60

#GET&%2F&AccessKeyId%3DTestId%26Action%3DQueryMetric%2626Format%3DJSON%26Metric%3DCPUUtilization%26Project%3Dacs_ecs%26RegionId%3Dcn%26SignatureMethod%3DHMAC-SHA1%26SignatureNonce%3D530b9e7a-71e5-4744-8548-77c5df29b8cb%26SignatureVersion%3D1.0%26StartTime%3D2016-02-02T10%253A33%253A56Z%26Timestamp%3D2016-02-04T03%253A17%253A29Z%26Version%3D2015-10-20%26period%3D60

#stringToSign="GET&%2F&AccessKeyId%3DTestId%26Action%3DQueryMetric%2626Format%3DJSON%26Metric%3DCPUUtilization%26Project%3Dacs_ecs%26RegionId%3Dcn%26SignatureMethod%3DHMAC-SHA1%26SignatureNonce%3D530b9e7a-71e5-4744-8548-77c5df29b8cb%26SignatureVersion%3D1.0%26StartTime%3D2016-02-02T10%253A33%253A56Z%26Timestamp%3D2016-02-04T03%253A17%253A29Z%26Version%3D2015-10-20%26period%3D60"
h = hmac.new("TestSecret" + "&", stringToSign, sha1)
signature = base64.encodestring(h.digest()).strip()
#IxsQ79fVwUu33iwZeH11Z2PfwqQ=
print(signature)
