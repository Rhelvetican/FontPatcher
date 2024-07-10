import os


def main():
    dirs = os.listdir("./font")
    for dir in dirs:
        if dir.endswith(".ttf") or dir.endswith(".otf"):
            os.system(f"fontforge -script font-patcher font/{dir}")
            continue
        dir = os.listdir(f"./font/{dir}")
        for font in dir:
            os.system(f"fontforge -script font-patcher font/carto/{font}")


if __name__ == "__main__":
    main()
