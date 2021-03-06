import os
import time
import shutil
import zipfile

import pyheif
from PIL import Image

from Exception.PathException import NoChosenFilePathException, NoChosenDirectoryPathException
from IO.IOTkinter.DataInputWithTkinter.ChoosePath import InputFilePathWithTkinter, InputDirectoryPathWithTkinter
from IO.IOTkinter.DataOutputWithTkinter.DisplayNotifications import ShowInformationToUser, DisplayErrorNotification, \
    BreakWorkingLoopFunction


class SeeMorePreprocessingSoftware:
    """
    - Pillar of OOP: By using encapsulation I have packaged the following functions into a blueprint
    that I can create multiple objects.
    """

    @staticmethod
    def clean_and_extract_zip_data(path_to_file: str, output_path: str):
        """
        Open a ZIP file, where file can be a path to a file (a string), a file-like object or a path-like object.
        As well as this create and saved the new zip file without hidden files crated by MAC OS system.
        :param path_to_file: can be a string, a file-like object or a path-like object.
        :param output_path: path where the zip file should be saved.
        """
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
        time.sleep(2)
        ShowInformationToUser(
            "The process of unzipping of the file has been completed successfully.").runNotification()

    @staticmethod
    def extract_zip_file():
        """
        The following function makes a copy of a given zip file and creates at output_path a zip file
        without '__MACOSX' file as well as extract the cleaned zip file at output_path.
        """

        while True:
            try:
                path_to_file = InputFilePathWithTkinter("Choose the file to unzip.").runNotification()
            except NoChosenFilePathException as error_message:
                DisplayErrorNotification(error_message).runNotification()

            try:
                output_path = InputDirectoryPathWithTkinter("Choose a directory to extract "
                                                            "the zip file.").runNotification()
            except NoChosenDirectoryPathException as error_message:
                DisplayErrorNotification(error_message).runNotification()

            try:
                SeeMorePreprocessingSoftware.clean_and_extract_zip_data(path_to_file, output_path)
            except IsADirectoryError as err:
                DisplayErrorNotification(err).runNotification()
            except AttributeError as err:
                DisplayErrorNotification(err).runNotification()
            except FileNotFoundError:
                DisplayErrorNotification("The zip file has not been chosen. "
                                         "Choose available option").runNotification()
            except UnboundLocalError:
                answer = BreakWorkingLoopFunction("Unable to unzip the file.\nDo You want to choose "
                                                  "another process?").runNotification()
                if answer:
                    break

    def remove_file(self, directory_to_file: str):
        try:
            os.remove(directory_to_file)
        except FileNotFoundError:
            DisplayErrorNotification("File not exists.").runNotification()

    def get_directory_and_file_name(self, directory_to_file: str) -> tuple:
        """
        An useful function to divide the directory to file into two parts.
        :param directory_to_file: Path to the data Set.
        :return: dataTuple: (directory_to_folder, file_name)
        """

        directory_to_folder = os.path.dirname(directory_to_file)  # return the directory name of pathname
        file_name = os.path.basename(directory_to_file)
        dataTuple = (directory_to_folder, file_name)
        return dataTuple

    def convert_heif_image_to_jpeg(self, directory_to_heif_image: str):
        directory, heif_image_name = self.get_directory_and_file_name(directory_to_heif_image)
        name, end = heif_image_name.split(".")
        heif_file = pyheif.read(directory_to_heif_image)  # heif_file is a HeifFile object, read an encoded HEIF image
        # convert a HeifFile object to a Pillow Image object
        heif_file_decoded_to_Pillow_image = Image.frombytes(heif_file.mode, heif_file.size, heif_file.data, "raw",
                                                            heif_file.mode, heif_file.stride)
        # convert a Pillow object to a JPEG extension image
        heif_file_decoded_to_Pillow_image.save(os.path.join(directory, (name + ".jpg")), "JPEG")
        self.remove_file(directory_to_heif_image)  # remove unnecessary heif image

    def convert_png_image_to_jpeg(self, directory_to_png_image: str):
        directory, png_image_name = self.get_directory_and_file_name(directory_to_png_image)
        (name, end) = os.path.splitext(png_image_name)
        try:
            with Image.open(directory_to_png_image) as image:
                rgb_image = image.convert("RGB")
                rgb_image.save(os.path.join(directory, (name+".jpg")))
        except (FileNotFoundError, ValueError, OSError) as err:
            DisplayErrorNotification(f"Unable to convert an image to JPEG extension. - {err}").runNotification()
        self.remove_file(directory_to_png_image)

    def clean_images_folder(self, directory_to_folder: str, imagesNamesList: list):
        """
        If the format of the image is different than JPEG extension, the image is converted to that format.
        The JPEG extension is recommended for colourful images by the TensorFlow documentation.
        During the process of cleaning, also the '.DS_Store' file is deleted.
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
                self.convert_heif_image_to_jpeg(directory_to_file)
                heic_number += 1
            elif image == ".DS_Store":
                self.remove_file(directory_to_file)
                dsFile_number += 1
            else:
                try:
                    with Image.open(directory_to_file) as img:
                        image_format = img.format
                        if image_format == "PNG":
                            self.convert_png_image_to_jpeg(directory_to_file)
                            png_number += 1
                        elif image_format == "JPEG":
                            jpg_number += 1
                except (FileNotFoundError, ValueError, OSError) as err:
                    DisplayErrorNotification(f"Unable to convert an image to JPEG extension. - {err}").runNotification()
        how_long = time.strftime("%H:%M:%S", time.gmtime(time.time() - start_process))
        print(f"\nInformation about the {os.path.basename(directory_to_folder)} data set:")
        print(f"There are {heic_number} HEIC images converted to JPEG extension.")
        print(f"There are {png_number} PNG images converted to JPEG extension.")
        print(f"There are {jpg_number} images with JPEG extension.")
        print(f"There is/are {dsFile_number} .DS_Store file/files which has been deleted "
              f"online during converting process.")
        print(f'Number of the images: {len(os.listdir(directory_to_folder))}.')
        print(f"Time of the image cleaning: {how_long} [HH:MM:SS].")
        print("----------------------------------------------------------------------------------")

    def create_new_folder(self, path_to_folder: str):
        """
        The following function creates a new folder in the given path to folder as a parameter.
        :param path_to_folder: Path into the folder which will be created.
        """

        try:
            os.mkdir(path_to_folder)
        except FileExistsError:
            DisplayErrorNotification(f"The following folder {os.path.basename(path_to_folder)} "
                                     f"exists.").runNotification()
        except FileNotFoundError:
            DisplayErrorNotification(
                f"The following folder or directory has not been found. Unable to create "
                f"the new folder.").runNotification()

    def create_folders_for_generators(self, path_to_folder: str) -> tuple:
        """
        The following function will create the main folder and two sub-folders for training and validation data.
        The two sub-folders named 'Training' and 'Validation' will be defined in the main folder afterwards.
        :param path_to_folder: path to the main folder, if the main folder does not exists, it will be created.
        :return: trainingDirectory, validationDirectory - directories into the training and validation data respectively.
        :rtype: tuple(str, str)
        """

        try:
            mainDirectory = os.path.join(path_to_folder, "SeeMoreDataSets")
            trainingDirectory = os.path.join(mainDirectory, "Training")
            validationDirectory = os.path.join(mainDirectory, "Validation")
            # map(give_me_function - action, give_me_parameters - data), returns a map object
            # doesn't modify the data parameter - immutable data
            any(map(self.create_new_folder, [mainDirectory, trainingDirectory, validationDirectory]))
            return trainingDirectory, validationDirectory  # tuple -> ()
        except OSError:
            DisplayErrorNotification("Process of creating folders for learning, "
                                     "have not been completed.").runNotification()

    def copy_file(self, file_source: str, file_destination: str):
        """
        The following function copies a file from file_source into the file_destination.
        :param file_source: entire path to the file
        :param file_destination: entire path to the file
        """

        try:
            assert isinstance(file_source, str), f"The following path: {file_source} should not be a number."
            assert isinstance(file_destination, str), f"The following path: {file_destination} should not be a number."
            shutil.copy_file(file_source, file_destination)
        except shutil.SameFileError:
            DisplayErrorNotification(
                f"File source path: {file_source} and a path to place where the file "
                f"is copied are the same.").runNotification()
        except AssertionError as error_message:
            DisplayErrorNotification(error_message).runNotification()
        except IsADirectoryError:
            DisplayErrorNotification("Unable to copy the directory. The parameters should be "
                                     "a full path to image").runNotification()
