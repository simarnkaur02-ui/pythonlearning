# import sys

# def count_lines(filename):
#     with open(filename) as f:
#         return len(f.readlines())
    

# if __name__ == "__main__":
#     #print(sys.argv)
#     #if len(sys.argv) != 2:
#         #print("Usage: python count_lines.py <filename>")
#         #sys.exit(1)

#     filename = sys.argv[1]
#     num_lines = count_lines(filename)
#     print(f"There are {num_lines} lines in {filename}")

import sys

def count_lines(filename):
    with open(filename) as f:
        return len(f.readlines())

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python count_lines.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    num_lines = count_lines(filename)
    print(f"There are {num_lines} lines in {filename}")
