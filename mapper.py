
# Import module
from urllib3 import PoolManager

class __Service:
    """ Service """
    def __init__(self, port, state, service):
        self.port = int(port.split("/")[0])
        self.state = state
        self.service = service
    
    def __repr__(self):
        return f"port={self.port}, state={self.state}, service={repr(self.service)}"

def __Request(address) -> str:
    """ Scan website using API """
    result = str(PoolManager().request("GET",
        "https://api.hackertarget.com/nmap/?q=" + address)
        .data.decode())
    return result

def __GetResult(data) -> list:
    """ Get list with services """
    result = []
    if not "Host is up" in data:
        return result
    for line in data.splitlines():
        if line.__contains__("/tcp"):
            TmpLine = ""
            for value in line.split(" "):
                if value: TmpLine += value + " "
            TmpLine = TmpLine.split(" ")
            result.append(__Service(TmpLine[0], TmpLine[1], TmpLine[2]))
    return result

def scan(address):
    """ Scan address and fetch result """
    return __GetResult(__Request(address))
