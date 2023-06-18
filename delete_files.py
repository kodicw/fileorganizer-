import os
import tomllib as toml
import re


if os.path.isfile("conf.toml"):
    with open("conf.toml", "rb") as f:
        CONFIG = toml.load(f)
        EXCLUDE = CONFIG["files"]["exclude"]

else:
    os.mkdir("conf.toml")


def main():
    file_exts = CONFIG["organize"].keys()
    conf_file = CONFIG
    organize_files(file_exts, conf_file)


def rm_list(exclude_list):
    pass


def is_excluded_file(exclude_list, file_list):
    if len(exclude_list) == 0 or len(file_list) == 0:
        return False
    else:
        for exclusion in exclude_list:
            for file in file_list:
                if exclusion == file:
                    return True
    return False

def organize_files(file_exts: list, conf: dict):
    for dir in conf["files"]["directrorys_to_monitor"]:
        try:
            os.chdir(dir)
        except Exception as e:
            print(f"was unable to change into this directory {dir}")
            raise e
        cwd = os.getcwd()
        list_o_files = os.listdir()
        if len(list_o_files) == 0: continue
        for ext in file_exts:
            pattern = re.compile(f"[A-Za-z0-9]+\.{ext}")
            new_file_name = conf['organize'][ext]
            for file in list_o_files:
                if is_excluded_file(EXCLUDE, list_o_files): continue
                if pattern.match(file):
                    if os.path.exists(new_file_name):
                        print("file exists")
                    else:
                        os.mkdir(new_file_name)
                    os.rename(f"{cwd}/{file}", f"{new_file_name}/{file}")
            

if __name__ == "__main__":
    main()
