import os
import subprocess
from file_ops import FileOPS


class ExtensionOPS:

    @staticmethod
    def log(origin, destination):
        if not os.path.exists(destination):
            os.makedirs(destination)
        FileOPS.move_file(origin, destination)

    @staticmethod
    def get_apk_version(path):
        cmd = "aapt dump badging {}".format(path)
        out = subprocess.getoutput(cmd)
        for line in out.splitlines():
            if "versionName=" in line:
                return list(filter(lambda x: "versionName=" in x, line.split(" ")))[0].split("=")[1].replace("'", "")

    @staticmethod
    def apk(origin, destination):
        # (1) New file name
        ver = ExtensionOPS.get_apk_version(origin)
        file = os.path.splitext(origin)
        new_filename = "{file}_{ver}".format(file=file[0], ver=ver)
        # print(new_filename)

        # (2) Rename
        origin = FileOPS.rename_file(origin, origin.replace(file[0], new_filename))

        # (3) Move
        if not os.path.exists(destination):
            os.makedirs(destination)
        FileOPS.move_file(origin, destination)
