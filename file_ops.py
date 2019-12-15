import os
import shutil


class FileOPS:
    """
    File Operations
    """

    @staticmethod
    def move_file(origin, destination):
        shutil.move(origin, destination)

    @staticmethod
    def rename_file(origin, destination) -> str:
        """
        :param origin: Path to file
        :param destination: Path with changed filename
        :return: Path with changed filename
        """

        os.rename(origin, destination)
        return destination

    @staticmethod
    def get_extension(path):
        return os.path.splitext(path)[1]
