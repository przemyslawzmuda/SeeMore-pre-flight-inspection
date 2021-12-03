import os
import random
import numpy
from PIL import Image
import matplotlib.pyplot as mpyplot
import matplotlib.image as mimage


class LetsMeetData:
    """
    The following class is used to meet new data. Method are capable to make a research what king of data have
    been uploaded.

    Methods
    ----------
    walk_through_data(root_path: str)
        The following function can be used to print number of the files in each subdirectories.
    create_dictionary_paths_and_files(root_path: str) -> dict:
    """

    @staticmethod
    def walk_through_data(root_path: str):
        """
        The following function walks through the main directory called as a parameter root_path,
        in order to read subdirectories as well as files placed in the root_path. Information according to
        the root_path will be displayed.

        :param root_path:
        """
        number_files = 0
        for directoryPath, subDirNames, fileNames in os.walk(root_path, topdown=True):
            if len(subDirNames) == 1 and len(fileNames) == 1:
                # os.walk yields a 3-tuple: (dirpath, dirnames, filenames)
                print(f"There is {len(subDirNames)} sub-directory and {len(fileNames)} file in {directoryPath}.")
            elif len(subDirNames) == 0 and len(fileNames) == 0:
                print(f"There is no sub-directories and there is not any file in {directoryPath}.")
            elif len(subDirNames) > 1 and len(fileNames) == 1:
                print(f"There are {len(subDirNames)} sub-directories and {len(fileNames)} file in {directoryPath}.")
            elif len(subDirNames) == 1 and len(fileNames) > 1:
                print(f"There is {len(subDirNames)} sub-directory and {len(fileNames)} files in {directoryPath}.")
            else:
                print(f"There are {len(subDirNames)} sub-directories and {len(fileNames)} files in {directoryPath}.")
            number_files += len(fileNames)

        if number_files == 0:
            print(f"To sum up, there is not any file in {root_path}.")
        elif number_files == 1:
            print(f"To sum up, there is 1 file in {root_path}.")
        else:
            print(f"To sum up, there are {number_files} files in {root_path}.")

    @staticmethod
    def create_dictionary_paths_and_files(root_path: str) -> dict:
        """
        The following function takes as in input the data type String (root_path), walks through that main directory
        and returns a dictionary data type called 'dataDictionary'. The keys are paths to the subdirectories located
        in the root_path as well as this the values are list of data type that contains names of the images located
        inside the subdirectories.

        :param root_path: String data type. Absolute path into the main folder.

        :return: dataDictionary: {absolute_path_to_folder (String): images_names (List)}
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
    def returnArrayImage(path_to_jpeg_image: str) -> object:
        """
        The following function returns an image as an uint8 data type.
        :param path_to_jpeg_image: absolute path onto the image
        :rtype: <class 'numpy.ndarray'>
        """
        array_image = mimage.imread(path_to_jpeg_image)
        return array_image

    @staticmethod
    def displayImage(path_to_image):
        mpyplot.imshow(mimage.imread(path_to_image))  # pass a tensor image in the matrix as an argument
        mpyplot.title(os.path.basename(path_to_image))
        mpyplot.axis(False)

    @staticmethod
    def displayImageWithRgbScaleReference(path_to_image):
        randomImage = mimage.imread(path_to_image)[:, :, 0]
        mpyplot.imshow(randomImage)
        mpyplot.title(os.path.basename(path_to_image))
        mpyplot.axis(False)
        mpyplot.colorbar()

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

    @staticmethod
    def showRandomImageWithRgbScaleReference(root_path_to_dataSet):
        pathToRandomImageFromDataSet = LetsMeetData.returnRandomImageFromDirectory(root_path_to_dataSet)

        mpyplot.figure()
        # Display the default image in the figure on the left hand side
        mpyplot.subplot(1, 2, 1)
        LetsMeetData.displayImage(pathToRandomImageFromDataSet)
        # Display the default image in the figure with the RGB scale reference on the right hand side
        mpyplot.subplot(1, 2, 2)
        LetsMeetData.displayImageWithRgbScaleReference(pathToRandomImageFromDataSet)
        mpyplot.show()

    @staticmethod
    def printInfoImage(path_to_image):
        image = mimage.imread(path_to_image)
        print(f"Size of the image: {image.size}.\nShape of the image: {image.shape}.\nData type: {image.dtype}.\n")

    @staticmethod
    def checkPixelsAtCoordinatesImage(path_to_image):
        image = Image.open(path_to_image)  # PIL.Image object
        print(f"Information according to the image:\n{image}")

        # check and print pixels value at (0, 0) coordinates
        rgb_image = image.convert("RGB")  # convert into RGB color space
        rgbPixelValueZero = rgb_image.getpixel((0, 0))
        print(f"The pixel values at coordinates (0, 0) are: {rgbPixelValueZero}.\n")

        x = int(input("Enter the position of the pixel on the X axis: "))
        y = int(input("Enter the position of the pixel on the Y axis: "))
        print("\n")
        r, g, b = rgb_image.getpixel((x, y))
        print(f"RGB values of the pixel at position ({x}, {y}) are: ({r}, {g}, {b}).")
        print(f"The value of Red color at position ({x}, {y}) is {r} |")
        print(f"The value of Green color at position ({x}, {y}) is {g} |")
        print(f"The value of Blue color at position ({x}, {y}) is {b}.")
        print("\n")
