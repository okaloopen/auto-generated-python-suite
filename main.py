#!/usr/bin/env python3

"""
main.py
---------

This module implements a simple TCP port scanner. Given a target host (IP address
or domain name) and an optional range of ports, it attempts to establish a
TCP connection to each port in the range and reports which ports are open.

The scanner uses the built-in `socket` library and does not rely on any
third-party packages. It sets a short timeout for each connection attempt to
prevent long waits on unreachable ports.

Example usage::

    python main.py 127.0.0.1 --start 1 --end 1024
"""

import argparse
import socket
from typing import Optional


def scan_port(host: str, port: int, timeout: float = 1.0) -> bool:
    """Attempt to connect to a given host and port.

    Args:
        host: Hostname or IP address of the target machine.
        port: TCP port number to check.
        timeout: Timeout in seconds for the connection attempt.

    Returns:
        True if the port is open (connection succeeded), False otherwise.
    """
    sock: Optional[socket.socket] = None
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((host, port))
        return result == 0
    except Exception:
        return False
    finally:
        if sock:
            sock.close()


def main() -> None:
    """Parse command-line arguments and perform the port scan."""
    parser = argparse.ArgumentParser(
        description=(
            "Simple TCP port scanner that checks a range of ports on a target host."
        )
    )
    parser.add_argument(
        "host",
        help="Target host to scan (IP address or domain name)",
    )
    parser.add_argument(
        "--start",
        type=int,
        default=1,
        help="Starting port number (default: 1)",
    )
    parser.add_argument(
        "--end",
        type=int,
        default=1024,
        help="Ending port number (default: 1024)",
    )
    args = parser.parse_args()

    host = args.host
    start_port = max(1, args.start)
    end_port = max(start_port, args.end)

    print(
        f"Scanning host '{host}' for open TCP ports in range {start_port}–{end_port}..."
    )

    open_ports = []
    for port in range(start_port, end_port + 1):
        if scan_port(host, port):
            print(f"Port {port} is open")
            open_ports.append(port)

    if not open_ports:
        print("No open ports found in the specified range.")
    print("Scan complete.")


if __name__ == "__main__":
    main()
