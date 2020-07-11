import json
from API.api import Api

api = Api()

data = json.dumps(api.get_all(), indent=2).encode('utf-8')
print(data)

data2 = json.loads(data)

print(data2)
