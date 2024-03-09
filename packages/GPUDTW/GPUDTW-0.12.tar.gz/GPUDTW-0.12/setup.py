import setuptools

with open("./GPUDTW/README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="GPUDTW",
    version="0.12",
    author="Wang Zihao",
    author_email="qianlkzf@outlook.com",
    description=" dynamic time warping (DTW) by GPU accelerated",
    description_file='README.md',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/qianlkzf/GPUDTW",
    packages=setuptools.find_packages(),
    package_data={
        "GPUDTW":['./OpenCL.dll','./opencldtw.cl','./cudadtw.cu','./README.cn.md','./README.md']
    },
    install_requires=['numpy', 'numba'],
    keywords='DTW,GPU,OpenCL,CUDA',
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ),
    license='GNU GENERAL PUBLIC LICENSE Version 3',
)