import psutil
from hurry.filesize import size

memory = dict(psutil.virtual_memory()._asdict())
disk = dict(psutil.disk_usage("/")._asdict())
cpu = psutil.cpu_percent()


state = {}
state["cpu"] = {}
state["memory"] = {}
state["disk"] = {}
state["cpu"]["percent"] = cpu

state["memory"]["total"] = size(memory["total"])
state["memory"]["used"] = size(memory["used"])
state["memory"]["available"] = size(memory["available"])
state["memory"]["percent"] = memory["percent"]


state["disk"]["total"] = size(disk["total"])
state["disk"]["used"] = size(disk["used"])
state["disk"]["free"] = size(disk["free"])
state["disk"]["percent"] = disk["percent"]

print(state)