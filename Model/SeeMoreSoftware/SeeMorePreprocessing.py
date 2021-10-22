import os
import random
import time
import shutil
import pyheif
import zipfile
from PIL import Image
from LetsMeetData import LetsMeetData


class SeeMorePreprocessing:
    """
    - Pillar of OOP: By using encapsulation I have packaged the following functions into a blueprint
    that I can create multiple objects.
    - Pillar of OOP: Abstraction - hide away information and only give access to things that are crucial.
    """

    @staticmethod
    def cleanAndExtractZipData(path_to_file: str, output_path: str):
        """
        The following function makes a copy of a given zip file and creates at output_path a zip file
        without '__MACOSX' file as well as extract the cleaned zip file at output_path.
        :param path_to_file: Path to the directory which contains data.
        :param output_path: Place where the zip file will be extracted.
        """
        try:
            default_zip_file = zipfile.ZipFile(path_to_file, mode='r')
            without_rubbish_zip_file = zipfile.ZipFile(
                os.path.join(output_path, 'cleaned-' + os.path.basename(path_to_file)), mode='w')
            # without_rubbish_zip_file is a zipfile.ZipFile object: <zipfile.ZipFile filename='pathToZipFile' mode=''>
            for item in default_zip_file.infolist():
                '''
                infolist() return each file step by step hierarchically (everything as well as hidden files)
                item - file in the directory
                < ZipInfo filename = 'directory' compress_type = ... filemode = '' file_size = 688 compress_size = 334 >
                '''
                file_to_copy = default_zip_file.read(item.filename)  # Return the bytes of the file name in the archive.
                if not str(item.filename).startswith("__MACOSX"):
                    without_rubbish_zip_file.writestr(item, file_to_copy)  # ZipFile.writestr(zinfo_or_arcname, data)
            without_rubbish_zip_file.close()
            default_zip_file.close()
            with zipfile.ZipFile(without_rubbish_zip_file.filename, mode='r') as zipDataSet:
                zipDataSet.extractall(output_path)
        except IsADirectoryError as err:
            print("Zip file can not be converted because of:", err)
        except AttributeError as err:
            print("Zip file can not be converted because of:", err)

    def removeFile(self, directory_to_file: str):
        try:
            os.remove(directory_to_file)
        except FileNotFoundError:
            print("File not exists.")

    def getDirectoryAndFileName(self, directory_to_file: str) -> tuple:
        """
        An useful function to divide the directory to file into two parts.
        :param directory_to_file: Path to the data Set.
        :return: dataTuple: (directory_to_folder, file_name)
        """
        directory_to_folder = os.path.dirname(directory_to_file)  # return the directory name of pathname
        file_name = os.path.basename(directory_to_file)
        dataTuple = (directory_to_folder, file_name)
        return dataTuple

    def convertHeifImageToJpeg(self, directory_to_heif_image: str):
        directory, heif_image_name = self.getDirectoryAndFileName(directory_to_heif_image)
        name, end = heif_image_name.split(".")
        heif_file = pyheif.read(directory_to_heif_image)  # heif_file is a HeifFile object, read an encoded HEIF image
        # convert a HeifFile object to a Pillow Image object
        heif_file_decoded_to_Pillow_image = Image.frombytes(heif_file.mode, heif_file.size, heif_file.data, "raw",
                                                            heif_file.mode, heif_file.stride)
        # convert a Pillow object to a JPEG extension image
        heif_file_decoded_to_Pillow_image.save(os.path.join(directory, (name + ".jpg")), "JPEG")
        self.removeFile(directory_to_heif_image)  # remove unnecessary heif image

    def convertPngImageToJpeg(self, directory_to_png_image: str):
        directory, png_image_name = self.getDirectoryAndFileName(directory_to_png_image)
        (name, end) = os.path.splitext(png_image_name)
        try:
            with Image.open(directory_to_png_image) as image:
                rgb_image = image.convert("RGB")
                rgb_image.save(os.path.join(directory, (name+".jpg")))
        except (FileNotFoundError, ValueError, OSError) as err:
            print(f"Unable to convert an image to JPEG extension. - {err}")
        self.removeFile(directory_to_png_image)

    def _cleanImagesFolder(self, directory_to_folder: str, imagesNamesList: list):
        """
        If the format of the image is different
        than JPEG extension, the image is converted to that format. The JPEG extension is recommended for colourful
        images by the TensorFlow documentation. During the process of cleaning, also the '.DS_Store' file is deleted.
        :param directory_to_folder: which contains images
        :param imagesNamesList: list which contains names of the images
        """
        heic_number = 0
        png_number = 0
        jpg_number = 0
        dsFile_number = 0
        print(f"Converting images in the {os.path.basename(directory_to_folder)} data set...")
        start_process = time.time()
        for image in imagesNamesList:
            directory_to_file = os.path.join(directory_to_folder, image)
            if "HEIC" in image or "heic" in image:
                self.convertHeifImageToJpeg(directory_to_file)
                heic_number += 1
            elif image == ".DS_Store":
                self.removeFile(directory_to_file)
                dsFile_number += 1
            else:
                try:
                    with Image.open(directory_to_file) as img:
                        image_format = img.format
                        if image_format == "PNG":
                            self.convertPngImageToJpeg(directory_to_file)
                            png_number += 1
                        elif image_format == "JPEG":
                            jpg_number += 1
                except (FileNotFoundError, ValueError, OSError) as err:
                    print(f"Unable to convert an image to JPEG extension. - {err}")
        how_long = time.strftime("%H:%M:%S", time.gmtime(time.time() - start_process))
        print(f"\nInformation about the {os.path.basename(directory_to_folder)} data set:")
        print(f"There are {heic_number} HEIC images converted to JPEG extension.")
        print(f"There are {png_number} PNG images converted to JPEG extension.")
        print(f"There are {jpg_number} images with JPEG extension.")
        print(f"There is/are {dsFile_number} .DS_Store file/files which has been deleted online during converting process.")
        print(f'Number of the images: {len(os.listdir(directory_to_folder))}.')
        print(f"Time of the image cleaning: {how_long} [HH:MM:SS].")
        print("----------------------------------------------------------------------------------")

    def _cleanImagesDataSet(self, path_to_data_set: str):
        """
        The following function makes a process of cleaning a data set. It can works with one folder also with
        the main folder which contains subdirectories.
        :param path_to_data_set: folder where all images are stored.
        """
        # dataSetDictionary = { 'path1':[images1, ...], 'path2':[images2, ...], ... }
        dataSetDictionary = LetsMeetData.createDictionaryPathsAndFiles(path_to_data_set)
        for keyPath, valueImagesNamesList in dataSetDictionary.items():
            # items() returns a list containing a tuple for each key-value pair
            self._cleanImagesFolder(keyPath, valueImagesNamesList)

    @staticmethod
    def createNewFolder(path_to_folder: str):
        """
        The following function creates the new folder in a given path to folder as a parameter.
        :param path_to_folder: Path into the folder which will be created.
        """
        try:
            os.mkdir(path_to_folder)
        except FileExistsError:
            print(f"The following folder {os.path.basename(path_to_folder)} exists.")
        except FileNotFoundError:
            print(f"The following folder or directory has not been found. Unable to create the new folder.")

    @staticmethod
    def createFoldersForGenerators(path_to_folder: str) -> tuple:
        """
        The following function will create the main folder and two sub-folders for training and validation data.
        The two sub-folders named 'Training' and 'Validation' will be defined in the main folder afterwards.
        :param path_to_folder: path to the main folder, if the main folder does not exists, it will be created.
        :return: trainingDirectory, validationDirectory - directories into the training and validation data respectively.
        :rtype: tuple(str, str)
        """
        trainingDirectory = os.path.join(path_to_folder, "Training")
        validationDirectory = os.path.join(path_to_folder, "Validation")
        # map(give_me_function - action, give_me_parameters - data), returns a map object
        # doesn't modify the data parameter - immutable data
        any(map(SeeMorePreprocessing.createNewFolder, [path_to_folder, trainingDirectory, validationDirectory]))
        return trainingDirectory, validationDirectory  # tuple -> ()

    @staticmethod
    def _copyFile(file_source: str, file_destination: str):
        """
        The following function copies a file from file_source into the file_destination.
        :param file_source: entire path to the file
        :param file_destination: entire path to file
        """
        try:
            assert isinstance(file_source, str), f"The following path: {file_source} should not be a number."
            assert isinstance(file_destination, str), f"The following path: {file_destination} should not be a number."
            shutil.copyfile(file_source, file_destination)
        except shutil.SameFileError:
            print(f"File source path: {file_source} and a path to place where the file is copied are the same.")
        except AssertionError as error_message:
            print(error_message)
        except IsADirectoryError as err:
            print("Unable to copy the directory. The parameters should be a full path to image", err)

    @staticmethod
    def _createTrainingValidationDataSets(departue_path: str, approach_path: str):  # keep that method private
        """
        The following function creates the training and validation data sets. These data sets are essential
        for ImageDataGenerator and for the neural networks.
        :param departue_path: Path where the default items for neural networks are stored.
        :param approach_path: Path where the Training and Validation data sets will be created.
        """
        while True:
            try:
                trainingDataSize = int(input("Enter the size of the training set in [%] as an integer number: "))
                assert (trainingDataSize in range(1, 100)), "Give the size of a training data set in range from 1% to "\
                                                            "99%. - A training set shouldn\'t has 100% of the images"
                break
            except ValueError:
                print("The size of the training set should be entered as an integer number.\n")
            except AssertionError:
                print(
                    "Give the size of a training data set in range from 1% to 99%. - A training set shouldn\'t contain "
                    "100% of the images as well as this, the validation set should contain some images.\n")

        # Express the trainingDataSize as a percentage value
        trainingDataSize /= 100

        # Create the Training and Validation folders
        trainingDirectory, validationDirectory = SeeMorePreprocessing.createFoldersForGenerators(approach_path)

        # Get a data dictionary: { 'path1':[images1, ...], 'path2':[images2, ...], ... }
        dataImagesDictionary = LetsMeetData.createDictionaryPathsAndFiles(departue_path)

        for keyPath, valueImagesList in dataImagesDictionary.items():
            sub_folder = os.path.basename(keyPath)
            sub_folder_path_training = os.path.join(trainingDirectory, sub_folder)
            sub_folder_path_validation = os.path.join(validationDirectory, sub_folder)
            SeeMorePreprocessing.createNewFolder(sub_folder_path_training)
            SeeMorePreprocessing.createNewFolder(sub_folder_path_validation)

            '''
            Shuffle a valueImagesList, it doesn't return anything, only reorganize an existing list.
            The shuffle() method takes a sequence, like a list, and reorganize the order of the items.
            Note: This method changes the original list, it does not return a new list.
            '''
            random.shuffle(valueImagesList)

            # Set the size of the training and validation data sets
            trainingNumberImages = round(len(valueImagesList) * trainingDataSize)  # round float up into int number
            # validationNumberImages = len(valueImagesList) - trainingNumberImages

            # Create images list for training and validation data sets
            trainingImagesList = valueImagesList[:trainingNumberImages]  # [:x] - including the x-ith element
            validationImagesList = valueImagesList[trainingNumberImages:]  # [x:] - not including the x-ith element

            # Copy files (imagesNames) into the training and validation folders
            for image in trainingImagesList:
                departue_path_image = os.path.join(keyPath, image)
                approach_path_image = os.path.join(sub_folder_path_training, image)
                SeeMorePreprocessing._copyFile(departue_path_image, approach_path_image)
            for image in validationImagesList:
                departue_path_image = os.path.join(keyPath, image)
                approach_path_image = os.path.join(sub_folder_path_validation, image)
                SeeMorePreprocessing._copyFile(departue_path_image, approach_path_image)
