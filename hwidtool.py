import subprocess
import platform

def get_raw_hwid():
    system = platform.system()
    
    try:
        if system == "Windows":
            # Fetches the motherboard serial number on Windows systems
            cmd = 'wmic baseboard get serialnumber'
            output = subprocess.check_output(cmd, shell=True).decode().split('\n')
            return output[1].strip()
            
        elif system == "Linux":
            # Fetches the persistent Machine ID on Linux systems (e.g., Mint, Ubuntu)
            with open('/etc/machine-id', 'r') as f:
                return f.read().strip()
                
        else:
            return "Unsupported System"
            
    except Exception as e:
        return f"Error: {str(e)}"

hwid = get_raw_hwid()
print(f"Your ID is: {hwid}")
input("\nPress Enter to exit...")