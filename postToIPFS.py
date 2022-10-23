import requests

url = "https://api.pinata.cloud/pinning/pinFileToIPFS"


#gotta generate my own meta deta here
payload={'pinataOptions': '{"cidVersion": 1}',
'pinataMetadata': '{"name": "MyFile", "keyvalues": {"company": "Pinata"}}'}

files=[
  ('file',('creatdInvoice.png',open('/Users/edisonqu/PycharmProjects/DeCargo-Pay/createdInvoice.png','rb'),'application/octet-stream'))
]

bearer = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySW5mb3JtYXRpb24iOnsiaWQiOiIwOTM3YzQxNC1jMjg5LTQ1ZDQtYjYyZS02NWZhZThkMmY3NDUiLCJlbWFpbCI6ImVkaXNvbnF1dUBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwicGluX3BvbGljeSI6eyJyZWdpb25zIjpbeyJpZCI6IkZSQTEiLCJkZXNpcmVkUmVwbGljYXRpb25Db3VudCI6MX0seyJpZCI6Ik5ZQzEiLCJkZXNpcmVkUmVwbGljYXRpb25Db3VudCI6MX1dLCJ2ZXJzaW9uIjoxfSwibWZhX2VuYWJsZWQiOmZhbHNlLCJzdGF0dXMiOiJBQ1RJVkUifSwiYXV0aGVudGljYXRpb25UeXBlIjoic2NvcGVkS2V5Iiwic2NvcGVkS2V5S2V5IjoiMzZkNTUyNWYxM2QyZmY2Mzc4OTQiLCJzY29wZWRLZXlTZWNyZXQiOiI3NTc1NDc0NmVmNjU3NWY1ZDFkZGQ2ZDVkZDZkMmVjOWVmZGQ4N2Y4NjFmZjVlZmY0YTJkMWJmN2QzMTQ3MDg0IiwiaWF0IjoxNjY2NDkyMzMwfQ.fj0QsVWCuRar1awZDVvLzplOGpzsCiemBrquACigR6Y"
headers = {'Authorization': 'Bearer {}'.format(bearer)}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
