from setuptools import setup, find_packages
import sys

from ProteinDiffusionGenerator import __version__

with open("README.md", "r") as f:
    readme = f.read()

def get_url() -> str:
    if sys.version_info[:2] == (3, 8):
        _ver = "cp38"
    elif sys.version_info[:2] == (3, 9):
        _ver = "cp39"
    elif sys.version_info[:2] == (3, 10):
        _ver = "cp310"
    else:
        raise Exception(f"Python {sys.version} is not supported.")

    # FIXME: how to download on macox??
    if sys.platform == "win32":
        _os = "win_amd64"
    else:
        _os = "linux_x86_64"

    return f"https://download.pytorch.org/whl/cu113/torch-1.12.0%2Bcu113-{_ver}-{_ver}-{_os}.whl"

# ------------------------------------------------------------
# setup(
#     name="OmegaFold",
#     description="OmegaFold Release Code",
#     long_description=readme,
#     long_description_content_type="text/markdown",
#     license="Apache-2.0",
#     packages=find_packages(exclude=["tests", "tests.*"]),
#     entry_points={"console_scripts": ["omegafold=omegafold.__main__:main",],},
#     install_requires=[
#         "biopython",
#         f"torch@{get_url()}"
#     ],
#     python_requires=">=3.8",
# )
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
setup(
    name="ProteinDiffusionGenerator",
    version=__version__,
    
    description="ProteinDiffusionGenerator Release Code",
    long_description=readme,
    long_description_content_type="text/markdown",
    url='https://github.com/Bo-Ni/ProtenDiffusionGenerator_pip',
    author='Bo Ni',
    author_email='boni.mechanics@gmail.com',
    
    packages=find_packages(exclude=["tests", "tests.*"]),
    # entry_points={"console_scripts": ["omegafold=omegafold.__main__:main",],},
    install_requires=[
    ],
    python_requires=">=3.9",
)
# # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# setup(
#     name="ProteinDiffusionGenerator",
#     version=__version__,
    
#     description="ProteinDiffusionGenerator Release Code",
#     long_description=readme,
#     long_description_content_type="text/markdown",
#     url='https://github.com/Bo-Ni/ProtenDiffusionGenerator_pip',
#     author='Bo Ni',
#     author_email='boni.mechanics@gmail.com',
    
#     packages=find_packages(exclude=["tests", "tests.*"]),
#     # entry_points={"console_scripts": ["omegafold=omegafold.__main__:main",],},
#     install_requires=[
#         "biopython",
#         f"torch@{get_url()}",
#         "nvidia-cudnn-cu11==8.6.0.163",
#         "tensorflow==2.12.0",
#         "OmegaFold @ git+https://github.com/HeliXonProtein/OmegaFold.git@v1.1.0",
#         "numpy==1.22.4",
#         "pandas==1.5.3",
#         "einops",
#         "einops-exts",
#         "pytorch-warmup",
#         "ema-pytorch",
#         "accelerate",
#         "py3Dmol",
#         "pexpect",
#         'scikit-learn',
#         "ipython",
#         "ipykernel",
#         "pandas",
#         "seaborn",
#     ],
#     python_requires=">=3.8",
# )
