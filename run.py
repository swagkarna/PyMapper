GNU nano 4.9.3           run.py
import mapper
import sys
target = sys.argv[1]
result = mapper.scan(target)
for r in result:
     print(f"Port: {r.port}, State: {r.state}, Service: {r.service}")
