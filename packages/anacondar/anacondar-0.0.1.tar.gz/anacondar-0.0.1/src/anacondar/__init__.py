import xml.etree.ElementTree as ET
from subprocess import run
import socket
import os
import sys

def cd(direc):
  os.chdir(direc)
def terminal():
  print(f'Anacondar - version 0.1 on {sys.platform.title()}')
  print(f'')
  while True:
    cmd = input(f'{socket.gethostname()}:{os.getcwd()} $ ')
    if cmd.split(' ')[0] == 'cd':
      cd(cmd.split(' ')[len(cmd.split(' '))-1])
      continue
    run(cmd, shell=True)
