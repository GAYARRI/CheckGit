
import os

def check_reboot():
    """Return True if the computer has a pending reboot."""
    return os.path.exists("/run/reboot-required")

def main():
    if check_reboot():
        print("Reinicio pendiente.")
    else:
        print("No hay reinicios pendientes.")

if __name__ == "__main__":
    main()



    
