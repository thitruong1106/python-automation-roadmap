#11/09/2025

"""
Write a program that logs "script ran at [timestamp]" into a file every time you run it 
"""

from datetime import datetime

now = datetime.now()
stamp = now.strftime("%Y-%m-%d %H:%M:%S")  # 2025-09-11 16:05:22

with open("timestamp.txt", "a") as f:
    f.write(f"Script ran at {stamp}\n")
