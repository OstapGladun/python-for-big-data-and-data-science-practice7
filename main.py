from importlib import import_module
input_module = import_module("input")
output_module = import_module("output")

def main():
    text1 = input_module.read_from_console()
    text2 = input_module.read_from_file_builtin("data/input.txt")
    text3 = input_module.read_from_file_pandas("data/input.csv")

    output_module.write_to_console(text1)
    output_module.write_to_console(text2)
    output_module.write_to_console(text3)

    output_module.write_to_file_builtin("data/output.txt", text1)
    output_module.write_to_file_builtin("data/output.txt", text2)
    output_module.write_to_file_builtin("data/output.txt", text3)


if __name__ == "__main__":
    main()