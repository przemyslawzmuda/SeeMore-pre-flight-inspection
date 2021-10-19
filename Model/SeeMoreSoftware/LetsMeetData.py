import os
import random
import matplotlib.pyplot as mpyplot
import matplotlib.image as mimage


class LetsMeetData:
    @staticmethod
    def walkThroughData(root_path):
        """
        :param root_path:
        The function walkThroughData() walks through the main directory called as a parameter root_path,
        in order to read subdirectories as well as files placed in the root_path. Informations according to
        the root_path will be displayed.
        """
        filesNumber = 0
        for directoryPath, subDirNames, fileNames in os.walk(root_path, topdown=True):
            # os.walk yields a 3-tuple: (dirpath, dirnames, filenames)
            print(f"There are {len(subDirNames)} sub-directories and {len(fileNames)} files in {directoryPath}.")
            filesNumber += len(fileNames)
        print(f"There are {filesNumber} files in {root_path}.")

    @staticmethod
    def createDictionaryPathsAndFiles(root_path):
        """
        :param root_path:
        :return: dataDictionary - {path_to_folder (String): images_names (List)}
        The following function takes as in input the data type String (root_path), walks through that main directory
        and returns a dictionary data type called 'dataDictionary'. The keys are path to the subdirectories located
        in the root_path as well as this the values are list data type contains names of the images located
        inside the subdirectories.
        """
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

    @staticmethod
    def returnRandomImageFromDirectory(root_path):
        """
        :param root_path:
        :return: outrightPathToRandomImage
        The following function returns a path to the random image from the root_path directory.
        """
        # Get a dictionary {'path': [img1, img2, ..., img_n]}
        imagesDictionary = LetsMeetData.createDictionaryPathsAndFiles(root_path)
        # Get items from imagesDictionary as dict_items: dict_items( [ (path1, [images]) ] )
        imagesDictionaryItems = imagesDictionary.items()  # dict_items() object
        # Convert the following dict_items() object into a List data type: [ (path1, [images1], ... ]
        imagesDictionaryItemsList = list(imagesDictionaryItems)
        # Shuffle the following list, it does not return anything, only reorganize the existing list
        random.shuffle(imagesDictionaryItemsList)
        # Get a random tuple
        randomTuple = random.choice(imagesDictionaryItemsList)  # List data type: [ (path1, [images1], ... ]
        # Split the the tuple components into the two variables
        pathToImages, imagesList = randomTuple
        # Return randomize the imagesList using random.sample(sequence, k)
        randomImagesList = random.sample(imagesList, len(imagesList))  # k = len(imagesList)
        # Choose a random sample (image) from the randomImagesList
        randomImage = random.choice(randomImagesList)
        # create a complete path to the image
        outrightPathToRandomImage = os.path.join(pathToImages, randomImage)
        return outrightPathToRandomImage

    @staticmethod
    def displayImage(path_to_image):
        mpyplot.imshow(mimage.imread(path_to_image))  # pass a tensor image in the matrix as an argument
        mpyplot.title(os.path.basename(path_to_image))
        mpyplot.axis(False)

    @staticmethod
    def showRandomImage(root_path_to_dataSet):
        """
        :param root_path_to_dataSet:
        :return: Image
        The following function displays a random Image from DataSet given as a parameter into the function.
        The random image will be displayed in the figure.
        """
        pathToRandomImageFromDataSet = LetsMeetData.returnRandomImageFromDirectory(root_path_to_dataSet)

        # Display the image in the figure
        mpyplot.figure()
        mpyplot.subplot()
        LetsMeetData.displayImage(pathToRandomImageFromDataSet)
        mpyplot.show()
