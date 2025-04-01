import input
import output

def main():
    text1 = input.read_from_console()
    text2 = input.read_from_file_builtin("data/input.txt")
    text3 = input.read_from_file_pandas("data/input.csv")

    output.write_to_console(text1)
    output.write_to_console(text2)
    output.write_to_console(text3)

    output.write_to_file_builtin("data/output.txt", text1)
    output.write_to_file_builtin("data/output.txt", text2)
    output.write_to_file_builtin("data/output.txt", text3)


if __name__ == "__main__":
    main()