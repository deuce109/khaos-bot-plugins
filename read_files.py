from discord import Attachment

COMMAND = "files"

def _determine_size(size_in_bytes: int) -> str:
    size_labels = ["B", "KB", "MB", "GB"]
    counter = 0
    size = size_in_bytes
    while size > 1024:
        size = size / 1024.0
        counter += 1 
        
    return f"{size}{size_labels[counter]}"

def execute(_: list[str], attachments: list[Attachment]) -> str:
    
    output = ""
    
    for attach in attachments:
        output += f"`{attach.filename}` Length: {_determine_size(attach.size)}\n"
        
    return output
