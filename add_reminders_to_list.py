#!/usr/bin/env python

import argparse
import csv
import subprocess

parser = argparse.ArgumentParser(
  epilog='Provided with no garuntee or warranty',
  description='Allows you to add a CSV reminder file to your iOS Reminders App'
)

parser.add_argument('--in-file', required=True, dest='file')
parser.add_argument('--destination-list', required=True, dest="list_name")

args = parser.parse_args()

with open(args.file, newline='') as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    result = subprocess.run([
      './create_reminder.applescript',
      args.list_name,
      row['title'],
      str(row['status'] == 'completed')
    ], capture_output=True, check=False)
    if result.returncode != 0:
      print("Call to create_reminder.applescript failed.")
      print("STDERR:")
      print(result.stderr.decode('UTF-8'))
      print("STDOUT:")
      print(result.stdout.decode('UTF-8'))
      exit(1)
    print(result.stdout.decode('UTF-8'))