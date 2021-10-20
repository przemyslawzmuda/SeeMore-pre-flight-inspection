import os
import pyheif
import zipfile
from PIL import Image


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

    @staticmethod
    def convertHeifImageToJpeg(directory_to_heif_image):
        directory = os.path.dirname(directory_to_heif_image)  # return the directory name of pathname
        heif_image_name = os.path.basename(directory_to_heif_image)
        (name, end) = heif_image_name.split(".")
        heif_file = pyheif.read(directory_to_heif_image)  # heif_file is a HeifFile object, read an encoded HEIF image
        # convert a HeifFile object to a Pillow Image object
        heif_file_decoded_to_Pillow_image = Image.frombytes(heif_file.mode, heif_file.size, heif_file.data, "raw",
                                                            heif_file.mode, heif_file.stride)
        # convert a Pillow object to a JPEG extension image
        heif_file_decoded_to_Pillow_image.save(os.path.join(directory, (name + ".jpg")), "JPEG")
        if os.path.exists(directory_to_heif_image):
            os.remove(directory_to_heif_image)  # remove unnecessary heif image
