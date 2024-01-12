from Generator.Visitor import generate

import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <input_file>")
        exit(1)

    input_file = sys.argv[1]
    output_file = input_file.split('.')[0] + '.ll'
    generate(input_file, output_file)
