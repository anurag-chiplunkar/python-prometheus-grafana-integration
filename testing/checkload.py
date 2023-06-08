import psutil

"""
In this code:

The psutil.cpu_percent() function is used to retrieve the current CPU load as a percentage.
The interval parameter specifies the time interval in seconds over which the CPU load is calculated. In this example, the interval is set to 1 second.
The check_cpu_load() function encapsulates this functionality and returns the current CPU load as a floating-point value.
The returned CPU load can be used for further processing or printing as needed.
You can run the code as-is or integrate the check_cpu_load() function into your own project to monitor CPU load as desired.
"""

def check_cpu_load():
    cpu_load = psutil.cpu_percent(interval=10)
    return cpu_load

# Example usage: check current CPU load
current_load = check_cpu_load()
print(f"Current CPU load: {current_load}%")
