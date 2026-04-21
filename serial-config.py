#!/usr/bin/env python3
"""
Cooling System Configuration Tool
Sends a configuration string to the embedded device via serial using a custom protocol.
"""

import argparse
import sys
import serial

# Protocol constants
BREAK_CHARS = b'\xaa\xaa'
BAUDRATE = 115200
MIN_LENGTH = 3
MAX_LENGTH = 128

def send_config(port: str, config_string: str) -> None:
    """Pack and send the configuration string over serial."""
    # Validate string length
    str_len = len(config_string)
    if not MIN_LENGTH <= str_len <= MAX_LENGTH:
        sys.exit(f"ERROR: String length must be {MIN_LENGTH}-{MAX_LENGTH} chars. Got {str_len}.")

    # Build packet: 2 break characters + 1 length byte + ASCII payload
    length_byte = str_len.to_bytes(1, 'big')
    packet = BREAK_CHARS + length_byte + config_string.encode('ascii')

    try:
        with serial.Serial(port, BAUDRATE, timeout=1) as ser:
            ser.write(packet)
            print(f"SUCCESS: Sent {len(packet)} bytes to {port}")
            print(f"Payload: {config_string}")
    except serial.SerialException as e:
        sys.exit(f"ERROR: Could not open {port} - {e}")
    except Exception as e:
        sys.exit(f"ERROR: {e}")

def main():
    parser = argparse.ArgumentParser(
        description="Configure Cooling System via serial.",
        epilog='Example: %(prog)s -P COM3 "MQTT_BROKER=192.168.0.50;MQTT_PORT=1883"'
    )
    parser.add_argument(
        "-P", "--port",
        required=True,
        help="Serial port (e.g., COM3 on Windows, /dev/ttyUSB0 on Linux)"
    )
    parser.add_argument(
        "config_string",
        help="Configuration string (e.g., 'MQTT_BROKER=...;MQTT_PORT=...')"
    )
    args = parser.parse_args()
    send_config(args.port, args.config_string)

if __name__ == "__main__":
    main()