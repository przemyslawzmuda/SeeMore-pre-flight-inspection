import os
import random
from PIL import Image
from collections import KeysView

from numpy import ndarray

import matplotlib.image as mimage
import matplotlib.pyplot as mpyplot


class LetsMeetData:
    """The following class is used to meet new data. Method are capable to make a research what king of data have
    been uploaded.

    Methods
    ----------
    walk_through_data
        The following function can be used to print number of the files in each subdirectories.
    create_dictionary_paths_and_files
        The following function takes as in input the data type String (root_path), walks through that main directory
        and returns a dictionary data type called 'data_dictionary'.
    get_directories_paths_from_data_set
        The following function is used to return the dict_keys object that contains all keys from the dictionary.
        According to the LetsMeetData.create_dictionary_paths_and_files(root_path) static method,
        the keys are the absolute paths into the subdirectories that contains images.
    return_random_image_from_directory
        The following function can be used to return a random absolute path into the image located inside
        the root_path.
    return_image_array
        The following function returns an image as an uint8 data type place in the numpy array.
    display_image
        The following function displays the image as a tensor image in the matrix.
    display_image_with_rgb_scale_reference
        The following function displays the considered image with the RGB scale reference.
    show_random_image
        The following function displays a random Image from given DataSet as a parameter into the function.
        The random image will be displayed in the figure.
    show_random_image_with_rgb_scale_reference
        The following function will display the original random image from the given path to data set as a parameter
        on the right hand side. As well as this, the considered image with RGB scale reference will be displayed
        on the right hand side in the figure.
    check_pixels_at_coordinates_image
        The following function enables to display the pixels value at the given coordinates.

    """

    @staticmethod
    def walk_through_data(root_path: str) -> None:
        """The following function walks through the main directory called as a parameter root_path,
        in order to read subdirectories as well as files placed in the root_path. Information according to
        the root_path will be displayed.

        :param root_path: Absolute String path into the folder.

        :return: None.
        """

        absolute_number_files = 0
        for directory_path, sub_dir_names, file_names in os.walk(root_path, topdown=True):
            number_sub_directories = len(sub_dir_names)
            number_files = len(file_names)
            if number_sub_directories == 1 and number_files == 1:
                # os.walk yields a 3-tuple: (dir_path, dir_names, file_names)
                print(f"There is {number_sub_directories} sub-directory and {number_files} file in {directory_path}.")
            elif number_sub_directories == 0 and number_files == 0:
                print(f"There is no sub-directories and there is not any file in {directory_path}.")
            elif number_sub_directories > 1 and number_files == 1:
                print(f"There are {number_sub_directories} sub-directories and {number_files} file in {directory_path}.")
            elif number_sub_directories == 1 and number_files > 1:
                print(f"There is {number_sub_directories} sub-directory and {number_files} files in {directory_path}.")
            else:
                print(
                    f"There are {number_sub_directories} sub-directories and {number_files} files in {directory_path}.")
                
            absolute_number_files += number_files

        if absolute_number_files == 0:
            print(f"To sum up, there is not any file in {root_path}.")
        elif absolute_number_files == 1:
            print(f"To sum up, there is 1 file in {root_path}.")
        else:
            print(f"To sum up, there are {absolute_number_files} files in {root_path}.")

    @staticmethod
    def create_dictionary_paths_and_files(root_path: str) -> dict:
        """The following function takes as in input the data type String (root_path), walks through that main directory
        and returns a dictionary data type called 'data_dictionary'. The keys are paths to the subdirectories located
        in the root_path as well as this the values are list of data type that contains names of the images located
        inside the subdirectories.

        :param root_path: String data type. Absolute path into the main folder.

        :return: data_dictionary: {absolute_path_to_folder (String): images_names (List)}.
        """

        data_dictionary = {}
        for directory_path, sub_dir_names, file_names in os.walk(root_path, topdown=True):
            # os.walk yields a 3-tuple: (dir_path, dir_names, file_names)
            if len(sub_dir_names) > 0:
                continue
            else:
                data_dictionary.update({directory_path: file_names})
        return data_dictionary

    @staticmethod
    def get_directories_paths_from_data_set(root_path: str) -> KeysView:
        """The following function is used to return the dict_keys object that contains all keys from the dictionary.
        According to the LetsMeetData.create_dictionary_paths_and_files(root_path) static method,
        the keys are the absolute paths into the subdirectories that contains images.

        :param root_path: Absolute path into the directory.

        :return: <class 'dict_keys'>.
        """

        data_set_dictionary = LetsMeetData.create_dictionary_paths_and_files(root_path)
        return data_set_dictionary.keys()

    @staticmethod
    def return_random_image_from_directory(root_path: str) -> str:
        """The following function can be used to return a random absolute path into the image located inside
        the root_path.

        :param root_path: Absolute String path into the directory.

        :return: outrightPathToRandomImage: <class 'str'>.
        """
        
        # Get a dictionary {'path': [img1, img2, ..., img_n]}
        images_dictionary = LetsMeetData.create_dictionary_paths_and_files(root_path)
        # Get items from imagesDictionary as dict_items: dict_items( [ (path1, [images]) ] )
        images_dictionary_items = images_dictionary.items()  # dict_items() object
        # Convert the following dict_items() object into a List data type: [ (path1, [images1], ... ]
        images_dictionary_items_list = list(images_dictionary_items)
        # Shuffle the following list, it does not return anything, only reorganize the existing list
        random.shuffle(images_dictionary_items_list)
        # Get a random tuple
        random_tuple = random.choice(images_dictionary_items_list)  # List data type: [ (path1, [images1], ... ]
        # Split the the tuple components into the two variables
        path_to_images, images_list = random_tuple
        # Return randomize the imagesList using random.sample(sequence, k)
        random_images_list = random.sample(images_list, len(images_list))  # k = len(imagesList)
        # Choose a random sample (image) from the randomImagesList
        random_image = random.choice(random_images_list)
        # create a complete path to the image
        outright_path_to_random_image = os.path.join(path_to_images, random_image)

        return outright_path_to_random_image

    @staticmethod
    def return_image_array(path_to_jpeg_image: str) -> ndarray:
        """The following function returns an image as an uint8 data type place in the numpy array.

        :param path_to_jpeg_image: Absolute path into the image.

        :rtype: <class 'numpy.ndarray'>
        """

        array_image = mimage.imread(path_to_jpeg_image)
        return array_image

    @staticmethod
    def display_image(path_to_image: str) -> None:
        """The following function displays the image as a tensor image in the matrix.

        :param path_to_image: Absolute String path into the image.

        :return: None.
        """

        mpyplot.imshow(mimage.imread(path_to_image))  # pass a tensor image in the matrix as an argument
        mpyplot.title(os.path.basename(path_to_image))
        mpyplot.axis(False)

    @staticmethod
    def display_image_with_rgb_scale_reference(path_to_image: str) -> None:
        """The following function displays the considered image with the RGB scale reference.
        
        :param path_to_image: Absolute String path into the image.
        
        :return: None.
        """

        random_image = mimage.imread(path_to_image)[:, :, 0]
        mpyplot.imshow(random_image)
        mpyplot.title(os.path.basename(path_to_image))
        mpyplot.axis(False)
        mpyplot.colorbar()

    @staticmethod
    def show_random_image(root_path_to_dataSet: str) -> None:
        """The following function displays a random Image from given DataSet as a parameter into the function.
        The random image will be displayed in the figure.
        
        :param root_path_to_dataSet: Absolute String path into the data set that contains for example sub-directories.
         
        :return: None.
        """

        path_to_random_image_from_data_set = LetsMeetData.return_random_image_from_directory(root_path_to_dataSet)

        # Display the image in the figure
        mpyplot.figure()
        mpyplot.subplot()
        LetsMeetData.display_image(path_to_random_image_from_data_set)
        mpyplot.show()

    @staticmethod
    def show_random_image_with_rgb_scale_reference(root_path_to_dataSet: str) -> None:
        """The following function will display the original random image from the given path to data set as a parameter
        on the right hand side. As well as this, the considered image with RGB scale reference will be displayed
        on the right hand side in the figure.

        :param root_path_to_dataSet: Absolute String path into the data set that contains for example sub-directories.

        :return: None.
        """

        path_to_random_image_from_data_set = LetsMeetData.return_random_image_from_directory(root_path_to_dataSet)

        mpyplot.figure()
        # Display the default image in the figure on the left hand side
        mpyplot.subplot(1, 2, 1)
        LetsMeetData.display_image(path_to_random_image_from_data_set)
        # Display the default image in the figure with the RGB scale reference on the right hand side
        mpyplot.subplot(1, 2, 2)
        LetsMeetData.display_image_with_rgb_scale_reference(path_to_random_image_from_data_set)
        mpyplot.show()

    @staticmethod
    def print_info_image(path_to_image: str) -> None:
        """The following function can be used to display the basic information according to the considered image.

        :param path_to_image: Absolute String path into the image.

        :return: None.
        """

        image = mimage.imread(path_to_image)
        print(f"Size of the image: {image.size}.\nShape of the image: {image.shape}.\nData type: {image.dtype}.\n")

    @staticmethod
    def check_pixels_at_coordinates_image(path_to_image: str) -> None:
        """The following function enables to display the pixels value at the given coordinates.

        :param path_to_image: Absolute String path into the image.

        :return: None.
        """

        image = Image.open(path_to_image)  # PIL.Image object
        print(f"Information according to the image:\n{image}")

        # check and print pixels value at (0, 0) coordinates
        rgb_image = image.convert("RGB")  # convert into RGB color space
        rgb_pixels_value_at_zero_zero_point = rgb_image.getpixel((0, 0))
        print(f"The pixel values at coordinates (0, 0) are: {rgb_pixels_value_at_zero_zero_point}.\n")

        x = int(input("Enter the position of the pixel on the X axis: "))
        y = int(input("Enter the position of the pixel on the Y axis: "))
        print("\n")
        r, g, b = rgb_image.getpixel((x, y))
        print(f"RGB values of the pixel at position ({x}, {y}) are: ({r}, {g}, {b}).")
        print(f"The value of Red color at position ({x}, {y}) is {r} |")
        print(f"The value of Green color at position ({x}, {y}) is {g} |")
        print(f"The value of Blue color at position ({x}, {y}) is {b}.")
        print("\n")
