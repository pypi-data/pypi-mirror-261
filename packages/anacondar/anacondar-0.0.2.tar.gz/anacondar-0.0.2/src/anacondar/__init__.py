import xml.etree.ElementTree as ET
from subprocess import run
import socket
import os
import sys

print(__file__)

running = False
def cd(direc):
  os.chdir(direc)
def exit():
  running = False
def terminal():
  running = True
  print(f'Anacondar - version 0.0.2 on {sys.platform.title()}')
  print(f'')
  while running:
    cmd = input(f'{socket.gethostname()}:{os.getcwd()} $ ')
    if cmd.split(' ')[0] == 'cd':
      cd(cmd.split(' ')[len(cmd.split(' '))-1])
      continue
    if cmd.split(' ')[0] == 'exit':
      exit()
      continue
    run(cmd, shell=True)
