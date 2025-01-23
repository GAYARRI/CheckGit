
import os
import sys

def check_reboot():
    """Return True if the computer has a pending reboot."""
    return os.path.exists("/run/reboot-required")

def main():
    if check_reboot():
        print("Atención : Reinicio pendiente.")
        sys.exist(1)    
    else:
        print("Todo esta correcto.")
        sys.exit(0)
        

if __name__ == "__main__":
    main()



    
