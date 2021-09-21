#!/usr/bin/env python3
""" A simple script to move two file into ceph_storage
    This is themed after StarCraft Characters"""

# Import section
import shutil
import os

def main():
  os.chdir('/home/student/mycode/')
  shutil.move('raynor.obj', 'ceph_storage/')

  xname = input('What is the new name for kerrigan.obj? ')
  shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

main()
