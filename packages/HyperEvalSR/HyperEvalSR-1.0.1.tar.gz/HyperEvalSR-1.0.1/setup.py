import setuptools

with open("README.md", "r") as f:
    long_description = f.read()
setuptools.setup(
    name="HyperEvalSR",
    version="1.0.1",
    author="jingmengzhiyue",
    author_email="jingmengzhiyue@gmail.com",
    description="An open source python package for super-resolution/recovery quality evaluation of hyperspectral images, including RMSE, ERGAS, SSIM, RSNR, PSNR, CC, DD, and SAM.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jingmengzhiyue/HyperEvalSR",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "matplotlib",
        "numpy",
        "scipy",
        "tifffile",
    ],
    python_requires=">=3.6",
)
