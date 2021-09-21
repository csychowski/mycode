#!/usr/bin/env python3
#
# Check hostname against a value

hostname = input("What value should we set for hostname?")

# Use lower to mutate input value into something workable
if hostname.lower() == "mtg":
    print("The hostname was found to be mtg")
    print("hostname matches expected config")

# Awlays display exit sign
print("Exiting the script")
