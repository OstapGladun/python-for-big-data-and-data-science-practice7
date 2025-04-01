def write_to_console(text: str):
    """
    Writes text to the console.

    Args:
        text (str): The text to print.
    """
    print(text)

def write_to_file_builtin(file_path: str, text: str):
    """
    Writes text to a file using built-in Python functions.

    Args:
        file_path (str): Path to the file to write to.
        text (str): The text to write.
    """
    try:
        with open(file_path, "a", encoding="utf-8") as file:
            file.write(text + "\n")
    except Exception as e:
        print(f"Error writing to file: {e}")

    pass
