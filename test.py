
import re

excluded_paths = ["/api/v1/stat*"]

arr = ["/api/v1/users", "/api/v1/status", "/api/v1/stats", " /api/v1/us"]

for val in arr:
    match = re.match("/api/v1/stat*", val)
    if match:
        print("found: ", re.match("/api/v1/stat*", val).string)
        
        
print(re.match('/api/v1/us*', "/api/v1/uas"))

print(re.search(re.compile('us.*'), "/api/v1/us"))


from datetime import datetime, timedelta

old = datetime.now()
future = datetime.now() + timedelta(seconds=20)

print(old < future)
