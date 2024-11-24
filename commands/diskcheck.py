from psutil import disk_usage


usage = disk_usage('/')
total_gb = usage.total / (1024 ** 3)
used_gb = usage.used / (1024 ** 3)
free_gb = usage.free / (1024 ** 3)


print(f"Total storage: {total_gb:.2f} GB")
print(f"Used storage: {total_gb-free_gb:.2f} GB")
print(f"Available storage: {free_gb:.2f} GB")
