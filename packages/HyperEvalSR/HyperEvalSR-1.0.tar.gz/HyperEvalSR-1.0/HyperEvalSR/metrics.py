import numpy as np


def RMSE(ref_img, rec_img):
    """Calculate the Root Mean Square Error (RMSE) between two images.

    Args:
        ref_img (numpy.ndarray): The reference image.
        rec_img (numpy.ndarray): The reconstructed image.

    Returns:
        float: The computed RMSE value.
    """
    if ref_img.shape != rec_img.shape:
        raise ValueError(
            "Reference and reconstructed images must have the same dimensions."
        )
    if not isinstance(ref_img, np.ndarray) or not isinstance(rec_img, np.ndarray):
        raise TypeError("Input images must be numpy arrays.")
    diff = ref_img - rec_img
    squared_diff = np.square(diff)
    mse = np.mean(squared_diff)
    Recult_rmse = np.sqrt(mse)
    return Recult_rmse


# Correlation Coefficient (CC) function
def CC(ref_img, rec_img, mask=None):
    """
    Calculate the Cross-Correlation (CC) between corresponding bands of two images.

    Args:
        ref_img (numpy.ndarray): The reference image.
        rec_img (numpy.ndarray): The reconstructed image.
        mask (numpy.ndarray, optional): A mask to apply to the images. Defaults to None.

    Returns:
        float: The computed CC value.
    """
    # Check if the input images have the same shape
    if ref_img.shape != rec_img.shape:
        raise ValueError("Reference and reconstructed images must have the same shape.")

    # Check if the mask is a boolean array and has the same spatial dimensions as the input images
    if mask is not None and (
        mask.dtype != np.bool or mask.shape[:2] != ref_img.shape[:2]
    ):
        raise ValueError(
            "Mask must be a boolean array with the same spatial dimensions as the input images."
        )

    # Extract the number of bands from the reconstructed image
    _, _, bands = rec_img.shape

    # Initialize an array to hold the CC values for each band
    out = np.zeros(bands)

    # Iterate over each band
    for i in range(bands):
        # Extract the current band from the reconstructed and reference images
        tar_tmp = rec_img[:, :, i]
        ref_tmp = ref_img[:, :, i]

        # Apply the mask if provided
        if mask is not None:
            mask_ = np.nonzero(mask)
            tar_tmp = tar_tmp[mask_]
            ref_tmp = ref_tmp[mask_]

        # Compute the correlation coefficient between the flattened bands
        cc = np.corrcoef(tar_tmp.flatten(), ref_tmp.flatten())
        out[i] = cc[0, 1]  # Extract the off-diagonal value which is the CC
    # Calculate the mean CC across all bands
    Recult_CC = np.mean(out)
    return Recult_CC


# Difference Distance (DD) function
def DD(ref_img, rec_img):
    """
    Calculate the Mean Absolute Deviation (MAD) between two images.

    Args:
        ref_image (numpy.ndarray): The reference image.
        rec_image (numpy.ndarray): The reconstructed image.

    Returns:
        float: The computed MAD value.
    """
    # Check if the input images have the same shape
    if ref_img.shape != rec_img.shape:
        raise ValueError("Reference and reconstructed images must have the same shape.")
    deviation = np.abs(ref_img.ravel() - rec_img.ravel())
    Recult_DD = np.linalg.norm(deviation, ord=1) / ref_img.size
    return Recult_DD


# ERGAS function
def ERGAS(ref_img, rec_img, downsampling_scale):
    """
    Calculate the Erro Relative Global Accuracy (ERGAS) between two images.

    Args:
        ref_image (numpy.ndarray): The reference image.
        rec_image (numpy.ndarray): The reconstructed image.
        downsampling_scale (int): The downsampling scale factor.

    Returns:
        float: The computed ERGAS value.
    """
    # Check if the input images have the same shape
    if ref_img.shape != rec_img.shape:
        raise ValueError("Reference and reconstructed images must have the same shape.")

    # Ensure that both images have the same dimensions
    m, n, k = ref_img.shape
    mm, nn, kk = rec_img.shape
    m = min(m, mm)
    n = min(n, nn)
    k = min(k, kk)
    # Extract corresponding regions from both images
    imagery1 = ref_img[0:m, 0:n, 0:k]
    imagery2 = rec_img[0:m, 0:n, 0:k]
    # Initialize ERGAS value
    ergas = 0
    # Calculate ERGAS for each band
    for i in range(k):
        # Compute Mean Squared Error (MSE) and Root Mean Squared Error (RMSE) for each band
        mse = np.mean((imagery1[:, :, i] - imagery2[:, :, i]) ** 2)
        rmse = np.sqrt(mse)
        # Compute ERGAS contribution for each band
        ergas += (rmse / np.mean(imagery1[:, :, i])) ** 2

    # Compute overall ERGAS value
    Result_ERGAS = 100 * np.sqrt(ergas / k) / downsampling_scale
    return Result_ERGAS


# Peak Signal to Noise Ratio (PSNR) function
def PSNR(ref_img, rec_img):
    """
    Calculate the Peak Signal-to-Noise Ratio (PSNR) between two images.

    Args:
        ref_img (numpy.ndarray): The reference image.
        rec_img (numpy.ndarray): The reconstructed image.

    Returns:
        float: The computed PSNR value.
    """
    # Check if the input images have the same shape
    if ref_img.shape != rec_img.shape:
        raise ValueError("Reference and reconstructed images must have the same shape.")

    mse = np.mean((ref_img - rec_img) ** 2)
    max_val = np.max(ref_img)
    psnr = 20 * np.log10(max_val / np.sqrt(mse))
    return psnr


# Relative Signal to Noise Ratio (RSNR) function
def RSNR(ref_img, rec_img, mask=None):
    """
    Calculate the Relative Signal-to-Noise Ratio (RSNR) between corresponding bands of two images.

    Args:
        ref_image (numpy.ndarray): The reference image.
        rec_image (numpy.ndarray): The reconstructed image.
        mask (numpy.ndarray, optional): A mask to apply to the images. Defaults to None.

    Returns:
        numpy.ndarray: The computed RSNR value for each band.
    """
    tar = ref_img
    ref = rec_img
    _, _, bands = ref.shape

    if mask is None:
        ref = np.reshape(ref, (-1, bands))
        tar = np.reshape(tar, (-1, bands))

        msr = np.linalg.norm(ref - tar, "fro") ** 2
        max2 = np.linalg.norm(ref, "fro") ** 2
        rsnrall = 10 * np.log10(max2 / msr)

        out = {}
        out["all"] = rsnrall
        Result_RSNR = out["all"]

    else:
        ref = np.reshape(ref, (-1, bands))
        tar = np.reshape(tar, (-1, bands))
        mask = mask != 0

        msr = np.mean((ref[mask, :] - tar[mask, :]) ** 2, axis=0)
        max2 = np.max(ref, axis=0) ** 2

        psnrall = 10 * np.log10(max2 / msr)
        out = {}
        out["all"] = psnrall
        out["ave"] = np.mean(psnrall)
        Result_RSNR = out["all"]

    return Result_RSNR


# Spectral Angle Mapper (SAM) function
def SAM(ref_img, rec_img):
    """
    Calculate the Spectral Angle Mapper (SAM) between corresponding bands of two images.

    Args:
        ref_image (numpy.ndarray): The reference image.
        rec_image (numpy.ndarray): The reconstructed image.

    Returns:
        float: The computed SAM value.
    """
    tmp = (
        (np.sum(ref_img * rec_img, axis=2) + np.finfo(float).eps)
        / (np.sqrt(np.sum(ref_img**2, axis=2)) + np.finfo(float).eps)
        / (np.sqrt(np.sum(rec_img**2, axis=2)) + np.finfo(float).eps)
    )
    sam = np.mean(np.real(np.arccos(tmp)))
    return sam


# Structural Similarity Index Measure (SSIM) function
def SSIM(ref_img, rec_img, k1=0.01, k2=0.03, L=255):
    """
    Calculate the Structural Similarity Index Measure (SSIM) between two images.

    Args:
        ref_image (numpy.ndarray): The reference image.
        rec_image (numpy.ndarray): The reconstructed image.
        k1 (float, optional): Constant for stability. Defaults to 0.01.
        k2 (float, optional): Constant for stability. Defaults to 0.03.
        L (int, optional): Dynamic range of the images. Defaults to 255.

    Returns:
        float: The computed SSIM value.
    """
    c1 = (k1 * L) ** 2
    c2 = (k2 * L) ** 2
    mu_x = np.mean(ref_img, axis=(1, 2), keepdims=True)
    mu_y = np.mean(rec_img, axis=(1, 2), keepdims=True)
    sigma_x = np.std(ref_img, axis=(1, 2), keepdims=True)
    sigma_y = np.std(rec_img, axis=(1, 2), keepdims=True)
    sigma_xy = np.mean((ref_img - mu_x) * (rec_img - mu_y), axis=(1, 2), keepdims=True)
    ssim = (
        (2 * mu_x * mu_y + c1)
        * (2 * sigma_xy + c2)
        / ((mu_x**2 + mu_y**2 + c1) * (sigma_x**2 + sigma_y**2 + c2))
    )
    return np.mean(ssim)


# Universal Image Quality Index (UIQI) function
def UIQI(ref_img, rec_img):
    """
    Calculate the Universal Image Quality Index (UIQI) between two images.

    Args:
        ref_image (numpy.ndarray): The reference image.
        rec_image (numpy.ndarray): The reconstructed image.

    Returns:
        float: The computed UIQI value.
    """
    c1 = (0.01 * 255) ** 2
    c2 = (0.03 * 255) ** 2

    tensor1_sq = ref_img * ref_img
    tensor2_sq = rec_img * rec_img
    tensor1_tensor2 = ref_img * rec_img

    tensor1_mean = np.mean(ref_img)
    tensor2_mean = np.mean(rec_img)

    tensor1_sq_mean = np.mean(tensor1_sq)
    tensor2_sq_mean = np.mean(tensor2_sq)
    tensor1_tensor2_mean = np.mean(tensor1_tensor2)

    numerator = 4 * tensor1_tensor2_mean * tensor1_mean * tensor2_mean
    denominator = (tensor1_sq_mean + tensor2_sq_mean) * (
        tensor1_mean**2 + tensor2_mean**2
    )

    uiqi = numerator / (denominator + c1 + c2)

    return uiqi
