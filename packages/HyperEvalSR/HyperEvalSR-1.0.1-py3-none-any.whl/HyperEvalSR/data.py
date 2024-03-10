import os
import scipy.io as scio
import tifffile as tiff
import numpy as np
import matplotlib.pyplot as plt
from typing import Optional, Union, List


def load(file_path: str) -> Union[np.ndarray, None]:
    """Load an image from the specified file path.

    Args:
        file_path (str): The path to the image file.

    Returns:
        numpy.ndarray or None: The loaded image data, or None if the file format is not supported.
    """
    root, extension = os.path.splitext(file_path)
    if extension == ".tif":
        img = tiff.imread(file_path)
    elif extension == ".mat":
        img = scio.loadmat(file_path)
    else:
        raise TypeError("Input images must be mat or tif files.")
    return img


def show(
    HSI: np.ndarray,
    band_set: Optional[List[int]] = None,
    show: bool = True,
    save: bool = False,
    path: Optional[str] = None,
) -> Union[plt.Axes, None]:
    """
    Display the hyperspectral image (HSI) using a pseudo-color composite of selected bands.
    If band_set is None, default to using the last, middle, and last bands of HSI.

    Args:
        HSI (ndarray): Hyperspectral image to display.
        band_set (list or None): List of 3 band indices to compose the pseudo-color image. Defaults to None.
        show (bool): Whether to display the image immediately. Defaults to True.
        save (bool): Whether to save the image. Defaults to False.
        path (str): Path to save the image if save is True.

    Returns:
        ax (matplotlib.axes.Axes or None): The axes object containing the displayed image if show is False, otherwise None.

    Raises:
        ValueError: If save is True but path is not specified.
    """
    # Function to normalize color values
    min_val = np.min(HSI)
    max_val = np.max(HSI)

    HSI = (HSI - min_val) / (max_val - min_val)
    normColor = lambda R: np.clip((R - np.mean(R)) / np.std(R), -2, 2) / 3 + 0.5

    # Default band set
    if band_set is None:
        n_bands = HSI.shape[2]
        band_set = [n_bands - 1, n_bands // 2, 0]

    # Select and normalize bands for display
    temp_show = HSI[:, :, band_set]
    temp_show = normColor(temp_show)

    # Create figure and axes
    fig, ax = plt.subplots()

    # Display the image
    ax.imshow(temp_show)

    # Hide axis
    ax.axis("off")

    if save:
        if path is None:
            raise ValueError(
                "Path to save the image must be specified when save is True."
            )
        else:
            plt.savefig(path)

    # Show the image if requested
    if show:
        plt.show()
        return None
    else:
        return ax
