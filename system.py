import platform
import psutil
import logging

COMMAND = "specs"

def _get_size(bytes_val, suffix="B"):

    """
    Scale bytes to its proper format e.g:
    1253656 => '1.20MB'
    1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes_val < factor:
            return f"{bytes_val:.2f}{unit}{suffix}"
        bytes_val /= factor
    return f"{bytes_val:.2f}P{suffix}"

def _get_cpu_info() -> list[str]:
    
    cpu_lines = []
    
    cpu_freq = psutil.cpu_freq()
    cpu_lines.append(f"CPU: {platform.processor()}")
    cpu_lines.append(f"  - Cores: {psutil.cpu_count(logical=False)} (Physical)")
    cpu_lines.append(f"  - Threads: {psutil.cpu_count(logical=True)} (Logical)")
    if cpu_freq:
        cpu_lines.append(f"  - Max Frequency: {cpu_freq.max:.2f} Mhz")
    return cpu_lines

def _get_disk_info() -> list[str]:
    drive_lines = []
    total_disk_size = 0
    total_used_disk = 0
    try:
        partitions = psutil.disk_partitions()
        for partition in partitions:
            # Sum up the total size of physical disks (avoids virtual/temp file systems)
            if 'rw' in partition.opts and partition.fstype:
                total_disk_size += psutil.disk_usage(partition.mountpoint).total
                total_used_disk += psutil.disk_usage(partition.mountpoint).used
        if total_disk_size > 0:
            drive_lines.append(f"Total Disk Space: {_get_size(total_disk_size)}")
        if total_used_disk > 0:
            drive_lines.append(f"Disk Space Used: {_get_size(total_used_disk)}")
            
        if total_disk_size > 0 and total_used_disk > 0:
            percentage_used = (total_used_disk / total_disk_size) * 100
            drive_lines.append(f"Percentage Disk Used: {percentage_used:.1f}%")
            
    
    except Exception as e:
        logging.warning("Could not determine total disk size: %s", e)
        
    return drive_lines
    

def execute():
    """Gathers and returns system specifications as a formatted string."""
    
    spec_lines = ["## System Specs:"]
    try:
        uname = platform.uname()

        # OS Info
        spec_lines.append(f"OS: {uname.system} {uname.release} ({uname.machine})")

        # CPU Info
        cpu_lines = _get_cpu_info()
        spec_lines.extend(cpu_lines)
       
        # RAM Info
        svmem = psutil.virtual_memory()
        spec_lines.append(f"RAM: {_get_size(svmem.total)}")
                
        drive_lines = _get_disk_info()
        spec_lines.extend(drive_lines)

    except Exception as e:
        logging.warning("Error getting platform information: %s", e)
        
    return "\n".join(spec_lines)