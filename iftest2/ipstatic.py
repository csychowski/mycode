#!/usr/bin/env python3
ipchk = input("Apply an IP address: ") # this line now prompts the user for input

# a string tests as True
if ipchk == "127.0.0.1":
   print("Looks like the IP address was set to localhost: " + ipchk + " This is not recommeded.")
elif ipchk:
   print("Looks like the IP address was set: " + ipchk)
else:
   print("You did not provide input.")
