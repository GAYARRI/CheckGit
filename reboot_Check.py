#!/usr/bin/env python3
import os

def check_reboot():
    """Return True if the computer has a pending reboot."""
    return os.path.exists("/run/reboot-required")

def main():
    if check_reboot():
        print("Reboot is required.")
    else:
        print("No reboot is required.")

if __name__ == "__main__":
    main()
)


    
