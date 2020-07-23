import mapper
import sys
target = sys.argv[1]
result = mapper.scan(target)
for r in result:
     print(f"Port: {r.port}, State: {r.state}, Service: {r.service}")
