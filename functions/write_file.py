import os

def write_file(working_directory: str, file_path: str, content: str) -> str:


    working_dir_abs = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

    if os.path.commonpath([working_dir_abs, target_file]) != working_dir_abs:
       return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    if os.path.isdir(target_file):
        return f'Error: Cannot write to "{file_path}" as it is a directory'

    os.makedirs(os.path.dirname(target_file), exist_ok=True)

    with open(target_file, "w") as file:
        file.write(content)

    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'


schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Writes content into a file relative to the working directory and returns the character num written into the file",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path of the file to write, relative to the working directory",
                },
                "content": {
                    "type": "string",
                    "description": "Content that the function writes into the file",
                },
            },
        },
    },
}
