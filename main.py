import math
import speedtest

def bytes_to_mb(size_bytes):
    i = int(math.floor(math.log(size_bytes,1024)))
    power = math.pow(1024,i)
    size = round(size_bytes/power,2)
    return f"{size} Mbps"

wifi = speedtest.Speedtest()

# ANSI escape codes for color formatting
GREEN = '\033[92m'
YELLOW = '\033[93m'
ENDC = '\033[0m'

# Print status messages with color
print(f"{YELLOW}Getting download speed...{ENDC}")
download_speed = wifi.download()

print(f"{YELLOW}Getting upload speed...{ENDC}")
upload_speed = wifi.upload()

# Print the results with color
print(f"Download: {GREEN}{bytes_to_mb(download_speed)}{ENDC}")
print(f"Upload: {GREEN}{bytes_to_mb(upload_speed)}{ENDC}")
