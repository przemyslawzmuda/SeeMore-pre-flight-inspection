import zipfile


class SeeMorePreprocessing:
    @staticmethod
    def extractZipData(path_to_file, output_path):
        """
        :param path_to_file: Path to the directory which contains data.
        :param output_path: Place where the zip file will be extracted.
        """
        try:
            with zipfile.ZipFile(path_to_file, mode='r') as zipDataSet:
                zipDataSet.extractall(output_path)
        except IsADirectoryError as err:
            print("Zip file can not be converted because of:", err)
