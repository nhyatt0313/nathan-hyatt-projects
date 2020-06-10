import sys

# program arguments
# 0 - DirectoryPrinter.py
# 1 - directory to begin ("C:\Repos")
# 2 - file types to include/exclude - defaults to all (".py, .txt, .exe")
# 3 - include/exclude toggle - defaults to include (true)
if __name__ == "__main__":
    if len(sys.argv) <= 4:
        argKeys = ["Path", "Include" if sys.argv[3] else "Exclude"]
        for i, arg in enumerate(sys.argv):
            if i == 0:
                r = len(argKeys[0]) + len(sys.argv[1]) + 2
                for i in range(r):
                    print("_", end = "\n" if i == r - 1 else "")
            if i == 1 or i == 2:
                print(f"{argKeys[i - 1]}: {arg}")       
    else:
        print("Too many program arguments")
