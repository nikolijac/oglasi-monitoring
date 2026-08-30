import psutil

cpu = psutil.cpu_percent(interval=1)
ram = psutil.virtual_memory().percent
disk = psutil.disk_usage("/").percent

print(f"CPU={cpu}%")
print(f"RAM={ram}%")
print(f"DISK={disk}%")