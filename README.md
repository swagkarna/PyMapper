# :eyes: PyMapper
Python ports scanning module

# :snake: Usage:
``` python
>>> import mapper
>>> result = mapper.scan("google.com")
>>> for r in result:
...     print(f"Port: {r.port}, State: {r.state}, Service: {r.service}")
... 
Port: 21, State: filtered, Service: ftp
Port: 22, State: filtered, Service: ssh
Port: 23, State: filtered, Service: telnet
Port: 80, State: open, Service: http
Port: 110, State: filtered, Service: pop3
Port: 143, State: filtered, Service: imap
Port: 443, State: open, Service: https
Port: 3389, State: filtered, Service: ms-wbt-server
>>> 

```
