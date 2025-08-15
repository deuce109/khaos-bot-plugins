from discord import Attachment

COMMAND = "files"

def execute(_: list[str], attachments: list[Attachment]) -> str:
    
    output = ""
    
    for attach in attachments:
        output += f"{attach.filename} Length: {attach.size}\n"
        
    return output
        
        