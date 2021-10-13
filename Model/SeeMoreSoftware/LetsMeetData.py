import os


class LetsMeetData:
    @staticmethod
    def walkThroughData(root_path):
        filesNumber = 0
        for directoryPath, subDirNames, fileNames in os.walk(root_path, topdown=True):
            # os.walk yields a 3-tuple: (dirpath, dirnames, filenames)
            print(f"There are {len(subDirNames)} sub-directories and {len(fileNames)} files in {directoryPath}.")
            filesNumber += len(fileNames)
        print(f"There are {filesNumber} files in {root_path}.")

    @staticmethod
    def createDictionaryPathsAndFiles(root_path):
        dataDictionary = {}
        for directoryPath, subDirNames, fileNames in os.walk(root_path, topdown=True):
            # os.walk yields a 3-tuple: (dirpath, dirnames, filenames)
            if len(subDirNames) > 0:
                continue
            else:
                dataDictionary.update({directoryPath: fileNames})
        return dataDictionary
