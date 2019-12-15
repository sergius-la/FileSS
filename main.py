import os
from file_ops import FileOPS
from extension_ops import ExtensionOPS

source_path = os.path.join(os.environ['HOME'], "Downloads")
extensions = {
    ".log": {"operation": ExtensionOPS.log, "destination": "Logs"},
    ".apk": {"operation": ExtensionOPS.apk, "destination": "Android builds"}
}

if __name__ == '__main__':

    for file in os.listdir(source_path):
        ext = FileOPS.get_extension(file)
        if extensions.get(ext) is not None:
            path = os.path.join(source_path, file)
            destination = os.path.join(source_path, extensions.get(ext).get("destination"))
            extensions.get(ext).get("operation")(path, destination)
