# Cooling System Serial Config Tool

This tool simplifies the configuration process by handling the binary protocol header.  
The user only needs to provide the serial port and the parameter string.

## Requirements

- Python 3.7 or newer
- pyserial (`pip install pyserial`)

## Usage

`py ./serial-config.py -P <COM port> "<PARAMETERS>"`

### Examples

**Single parameter:**  
`py ./serial-config.py -P COM9 "TARGET_TEMP=10"`

**Multiple parameters (separated by semicolons):**  
`py ./serial-config.py -P COM9 "MQTT_BROKER=192.168.0.220;MQTT_PORT=1883;MQTT_USER=admin;MQTT_PASS=1234"`

**Commands:**  
`py ./serial-config.py -P COM9 "CMD=6"`   (Save MQTT settings)