import sys
global PROGRAM_OS
WIN = "win"
UIX = "unix"
OSX = "mac"
PORTS = []

def getPortsFromComports(listComports):
    devices = []
    for port in listComports:
        if "bluetooth" not in str(port).lower() and "wlan" not in str(port).lower():
            port = str(port.device)[8:].upper()
            devices.append(port)
    return devices


def checkOSandGetComports():
    if sys.platform.startswith('win'):
        from serial.tools import list_ports_windows
        return WIN, getPortsFromComports(list_ports_windows.comports())

    if sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        from serial.tools import list_ports_linux
        return UIX, getPortsFromComports(list_ports_linux.comports())

    if sys.platform.startswith('darwin'):
        from serial.tools import list_ports_osx
        return OSX, getPortsFromComports(list_ports_osx.comports())

    raise EnvironmentError('Unsupported platform')


if __name__ == '__main__':
    print("Coding is fun (almost)")

    PROGRAM_OS, PORTS = checkOSandGetComports()
    print("Current OS is: ", PROGRAM_OS, ",PORTS are ", PORTS)
