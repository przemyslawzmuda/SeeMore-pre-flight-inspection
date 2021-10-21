import os
import time
import pyheif
import zipfile
from PIL import Image
from LetsMeetData import LetsMeetData


class SeeMorePreprocessing:
    @staticmethod
    def cleanAndExtractZipData(path_to_file, output_path):
        """
        The following function makes a copy of a given zip file and returns at output_path a zip file
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

    def removeFile(self, directory_to_file):
        try:
            os.remove(directory_to_file)
        except FileNotFoundError:
            print("File not exists.")

    def getDirectoryAndFileName(self, directory_to_file: str) -> tuple:
        """
        :param directory_to_file:
        :return: dataTuple
        """
        directory_to_folder = os.path.dirname(directory_to_file)  # return the directory name of pathname
        file_name = os.path.basename(directory_to_file)
        dataTuple = (directory_to_folder, file_name)
        return dataTuple

    def convertHeifImageToJpeg(self, directory_to_heif_image):
        directory, heif_image_name = self.getDirectoryAndFileName(directory_to_heif_image)
        name, end = heif_image_name.split(".")
        heif_file = pyheif.read(directory_to_heif_image)  # heif_file is a HeifFile object, read an encoded HEIF image
        # convert a HeifFile object to a Pillow Image object
        heif_file_decoded_to_Pillow_image = Image.frombytes(heif_file.mode, heif_file.size, heif_file.data, "raw",
                                                            heif_file.mode, heif_file.stride)
        # convert a Pillow object to a JPEG extension image
        heif_file_decoded_to_Pillow_image.save(os.path.join(directory, (name + ".jpg")), "JPEG")
        self.removeFile(directory_to_heif_image)  # remove unnecessary heif image

    def convertPngImageToJpeg(self, directory_to_png_image):
        directory, png_image_name = self.getDirectoryAndFileName(directory_to_png_image)
        (name, end) = os.path.splitext(png_image_name)
        try:
            with Image.open(directory_to_png_image) as image:
                rgb_image = image.convert("RGB")
                rgb_image.save(os.path.join(directory, (name+".jpg")))
        except (FileNotFoundError, ValueError, OSError) as err:
            print(f"Unable to convert an image to JPEG extension. - {err}")
        self.removeFile(directory_to_png_image)

    def cleanImagesFolder(self, directory_to_folder: str, imagesNamesList: list):
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

    def cleanImagesDataSet(self, path_to_data_set: str):
        """
        The following function makes a process of cleaning a data set.  It can works with one folder also with
        the main folder which contains subdirectories.
        :param path_to_data_set: folder where all images are stored.
        """
        # dataSetDictionary = { 'path1':[images1, ...], 'path2':[images2, ...], ... }
        dataSetDictionary = LetsMeetData.createDictionaryPathsAndFiles(path_to_data_set)
        for keyPath, valueImagesNamesList in dataSetDictionary.items():
            # items() returns a list containing a tuple for each key-value pair
            self.cleanImagesFolder(keyPath, valueImagesNamesList)

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
        # map(give_me_function, give_me_parameters)
        any(map(SeeMorePreprocessing.createNewFolder, [path_to_folder, trainingDirectory, validationDirectory]))
        return trainingDirectory, validationDirectory  # tuple -> ()
