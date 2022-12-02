import threading
import psutil
import platform

# os.system("ls -l")

class Process:
  def __init__(self, pid, name, status):
    self.pid = pid,
    self.name = name,
    self.status = status

class Memory:
  def __init__(self, total, available, used, percent):
    self.total = total,
    self.available = available,
    self.used = used,
    self.percent = percent,

class System:
   def __init__(self, system, version, node, machine):
    self.system = system,
    self.version = version,
    self.node = node,
    self.machine = machine,

def all_processes():
  processes = []

  for pid in psutil.pids():
    process = psutil.Process(pid)
    new_process = Process(pid, process.name(), process.status())
    processes.append(new_process)  

  return processes

def hardware_info():
  return

def system_info():
  uname = platform.uname()
  
  system = System(uname.system, uname.version, uname.node, uname.machine) 

  return system

def memorys():
  def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

  vmemory = psutil.virtual_memory()
  smemory = psutil.swap_memory() 
  virtual_memory = Memory(get_size(vmemory.total), get_size(vmemory.available), get_size(vmemory.used), get_size(vmemory.percent))
  swap_memory = Memory(get_size(smemory.total), get_size(smemory.free), get_size(smemory.used), get_size(smemory.percent))

  return [virtual_memory, swap_memory]
  