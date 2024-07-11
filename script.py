import os


def main():
    directory = input("Enter the directory path: ")
    dir = os.listdir(f"./{directory}")
    for font in dir:
        os.system(f"fontforge -script font-patcher --complete -q -l --careful -out ./patched/{directory.replace("font/", "/")}/ ./{directory}/{font}")


if __name__ == "__main__":
    main()
