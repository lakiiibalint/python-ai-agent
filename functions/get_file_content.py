import os


def get_file_content(working_directory: str, file_path: str) -> str:

    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(
            os.path.join(working_dir_abs, file_path))

        if os.path.commonpath([working_dir_abs, target_file]) != working_dir_abs:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        MAX_CHARS = 10_000

        with open(target_file, "r") as file:
            file_content_string = file.read(MAX_CHARS)

        # After reading the first MAX_CHARS...
            if file.read(1):
                file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

        return file_content_string

    except Exception as e:
        return f"Error: {e}"


schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "Providing the content of a file, if the file is too large to read, returns where did it stop",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path to locate the desired file, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}
