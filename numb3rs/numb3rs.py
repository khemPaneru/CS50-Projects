import re

def main():
    prit

def validate(ip):
    if not re.match(r"^\d+\.\d+\.\d+\.\d+$", ip):
        return False
    try:
        octets = ip.split(".")
        if len(octets) !=4:
            
