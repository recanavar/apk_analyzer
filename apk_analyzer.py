from androguard.core.bytecodes.apk import APK
import argparse, json, sys

class Colors:
    Black = '\u001b[30m'
    Red = '\u001b[31m'
    Green = '\u001b[32m'
    Yellow = '\u001b[33m'
    Blue = '\u001b[34m'
    Magenta = '\u001b[35m'
    Cyan = '\u001b[36m'
    White = '\u001b[37m'
    Reset = '\u001b[0m'
    ENDC = '\u001b[37m'

# Extracting AndroidManifest.xml permissions to identify dangerous permissions.
def permissions(apk):
    print()
    print("========= PERMISSIONS =========")
    print()
    print(" - Not : DANGEROUS permissions may not be malicious for each application. ")
    print()

    with open("dangerous_permissions.json", 'r') as f :
        dangerous_permissions = json.load(f)

    apk_permissions = apk.get_permissions()
    perms = []

    for i in range(len(dangerous_permissions)): 
        perms.append(dangerous_permissions[i]["permission"])
        
    for perm in apk_permissions:
        if perm.split(".")[-1] in perms:
            print(f"[{Colors.Red}DANGEROUS{Colors.ENDC}] " + perm.split(".")[-1] + " - [" + Colors.Yellow + perm + Colors.ENDC + "]")
        else:
            print(f"[{Colors.Blue}INFO{Colors.ENDC}] " + perm.split(".")[-1] + " - [" + Colors.Yellow + perm + Colors.ENDC + "]")

# Parsing arguments
def parser():
    parser = argparse.ArgumentParser(description='APK analyzing tool.', prog='apk_analyzer.py', usage='%(prog)s [APK] [options]')
    parser.add_argument("apk", metavar="[APK]")
    args = vars(parser.parse_args())

    return args

def main():
    apk = APK(parser()["apk"])
    permissions(apk)

if __name__ == "__main__":
    main()
