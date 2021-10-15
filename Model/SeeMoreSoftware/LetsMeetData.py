import os


class LetsMeetData:
    @staticmethod
    def walkThroughData(root_path):
        '''
        :param root_path:
        The function walkThroughData() walks through the main directory called as a parameter root_path,
        in order to read subdirectories as well as files placed in the root_path. Informations according to
        the root_path will be displayed.
        '''
        filesNumber = 0
        for directoryPath, subDirNames, fileNames in os.walk(root_path, topdown=True):
            # os.walk yields a 3-tuple: (dirpath, dirnames, filenames)
            print(f"There are {len(subDirNames)} sub-directories and {len(fileNames)} files in {directoryPath}.")
            filesNumber += len(fileNames)
        print(f"There are {filesNumber} files in {root_path}.")

    @staticmethod
    def createDictionaryPathsAndFiles(root_path):
        '''
        :param root_path:
        :return: dataDictionary - {path_to_folder (String): images_names (List)}
        The following function takes as in input the data type String (root_path), walks through that main directory
        and returns a dictionary data type called 'dataDictionary'. The keys are path to the subdirectories located
        in the root_path as well as this the values are list data type contains names of the images located
        inside the subdirectories.
        '''
        dataDictionary = {}
        for directoryPath, subDirNames, fileNames in os.walk(root_path, topdown=True):
            # os.walk yields a 3-tuple: (dirpath, dirnames, filenames)
            if len(subDirNames) > 0:
                continue
            else:
                dataDictionary.update({directoryPath: fileNames})
        return dataDictionary

    @staticmethod
    def getDirectoriesPathInDataSet(root_path):
        dataSetDictionary = LetsMeetData.createDictionaryPathsAndFiles(root_path)
        return dataSetDictionary.keys()
