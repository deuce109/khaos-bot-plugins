import os
import logging
import requests

COMMAND = "servers"

def _get_external_ip() -> str:
    try:
        res = requests.get("https://ifconfig.me/ip", timeout=5)
        if res.status_code == 200:
            return f"## External IP: {res.text.strip()}\n"
    except Exception as e:
        logging.warning(f"Error retrieving external IP: {e}")
    return ""

def _get_local_ip() -> str:
    local_ip = os.getenv("LOCAL_IP", "")
    
    if local_ip:
        return f"## Internal IP: {local_ip}\n"
    else: 
        return ""
        

def execute(_: list[str], __) -> str:
    message_lines = ["# Servers"]
    message_lines.append(_get_local_ip())
    message_lines.append(_get_external_ip())
    return "\n".join(message_lines)