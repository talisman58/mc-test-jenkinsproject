#!/usr/bin/env python3
"""
Simple Jenkins test script
"""

import datetime
import socket

def main():
    # Print a hello message
    print("Hello from Jenkins Python job!")

    # Show current timestamp
    now = datetime.datetime.now()
    print(f"Current time: {now}")

    # Show hostname of the Jenkins agent
    host = socket.gethostname()
    print(f"Running on host: {host}")

    # Exit cleanly
    print("Script completed successfully.")

if __name__ == "__main__":
    main()
