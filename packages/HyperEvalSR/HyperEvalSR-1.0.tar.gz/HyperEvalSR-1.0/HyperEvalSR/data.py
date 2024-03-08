import os
import scipy.io as scio
import tifffile as tiff


def load(file_path):
    """Load an image from the specified file path.

    Args:
        file_path (str): The path to the image file.

    Returns:
        numpy.ndarray: The loaded image data.
    """
    root, extension = os.path.splitext(file_path)
    if extension == "tif":
        img = tiff.imread(file_path)
    if extension == "mat":
        img = scio.loadmat(file_path)
    return img
