import re
import sys

def main():
    if len(sys.argv) != 2:
        sys.exit(1)
    
    ip = sys.argv[1]

    print(validate(ip))
    
def validate(ip):
    matches = re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$", ip)
    if not matches:
        return "Invalid IP"
    for i in matches.groups():
        if int(i) > 255:
            return "Invalid IP"
    
    return "Valid IP"

if __name__ == "__main__":
    main()