#!/usr/bin/env python3
import os 
def check_reboot():
    """Return True if the computere has a pending reboot."""
    return os.path.exist("/run/reboot-requiered")
def main():
    pass
main()


    
