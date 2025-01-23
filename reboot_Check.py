#!/usr/bin/env python3
import os
import shutil

def check_reboot():
    """Return True if the computer has a pending reboot."""
    return os.path.exists("/run/reboot-required")

def check_disk_space(disk="/"):
    """
    Return the percentage of free disk space.

    Args:
        disk (str): The path of the disk to check. Defaults to the root '/'.

    Returns:
        float: The percentage of free disk space.
    """
    usage = shutil.disk_usage(disk)
    free_space_percentage = (usage.free / usage.total) * 100
    return free_space_percentage

def main():
    if check_reboot():
        print("Reboot is required.")
    else:
        print("No reboot is required.")

    disk_free = check_disk_space()
    print(f"Free disk space: {disk_free:.2f}%")
    if disk_free < 20:
        print("Warning: Low disk space!")

if __name__ == "__main__":
    main()

