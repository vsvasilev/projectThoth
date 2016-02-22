import http.client

conn = http.client.HTTPConnection("64.103.37.51:9443")

headers = {
    'authorization': "Basic cm9vdDpDIXNjMDEyMw==",
    'content-type': "application/vnd.yang.data+json",
    'accept': "application/vnd.yang.data+json",
    'cache-control': "no-cache",
    'postman-token': "89817a36-5ea3-20e0-c317-afbbf6cf9413"
    }

conn.request("GET", "/api/running/interfaces/interface/GigabitEthernet3.1?deep=", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))