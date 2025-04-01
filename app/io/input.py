import pandas as pd

def read_from_console():
    """
    Reads and returns text from console.

    Returns:
        str: The string inputted into console.
    """
    return input("Enter text: ")

def read_from_file_builtin(file_path: str):
    """
    Reads text from a file using built-in Python functions.

    Args:
        file_path (str): Path to the file to be read.

    Returns:
        str: The content of the file as a string.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return "Error: File not found."
    except Exception as e:
        return f"Error: {e}"

def read_from_file_pandas(file_path: str):
    """
    Reads text from a file using the pandas library.

    Args:
        file_path (str): Path to the file to be read.

    Returns:
        str: The content of the file as a string.
    """
    try:
        df = pd.read_csv(file_path, header=None)
        return "\n".join(df[0].astype(str).tolist())
    except FileNotFoundError:
        return "Error: File not found."
    except Exception as e:
        return f"Error: {e}"