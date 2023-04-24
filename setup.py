from setuptools import setup, find_packages
import sys

from ProteinDiffusionGenerator import __version__

with open("README.md", "r") as f:
    readme = f.read()

def get_url_torch() -> str:
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
#
# source: https://download.pytorch.org/whl/cu113/
def get_url_torchvision() -> str:
    # https://download.pytorch.org/whl/cu113/torchvision/
    # return f"https://download.pytorch.org/whl/cu113/torchvision/torchvision-0.13.0+cu113-cp39-cp39-linux_x86_64.whl"
    return f"https://download.pytorch.org/whl/cu113/torchvision-0.13.0%2Bcu113-cp39-cp39-linux_x86_64.whl"

def get_url_torchaudio() -> str:
    return f"https://download.pytorch.org/whl/cu113/torchaudio-0.12.0%2Bcu113-cp39-cp39-linux_x86_64.whl"


print(get_url_torch())
print()
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
#     ],
#     python_requires=">=3.9",
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
        f"torch@{get_url_torch()}",
        # "torch==1.12.0+cu113",
        f"torchvision@{get_url_torchvision()}",
        # "torchvision==0.13.0+cu113",
        f"torchaudio@{get_url_torchaudio()}",
        # "torchaudio==0.12.0+cu113",
        "nvidia-cudnn-cu11==8.6.0.163",
        "tensorflow==2.12.0",
        "OmegaFold @ git+https://github.com/HeliXonProtein/OmegaFold.git@v1.1.0",
        # +++++++++++++++++++++++++++++++++
        "biopython==1.81",
        "pandas==2.0.0",
        "seaborn==0.12.2",
        "scikit-learn==1.2.2",
        "kornia==0.6.12",
        "einops==0.6.1",
        "einops-exts==0.0.4",
        "pytorch-warmup==0.1.1",
        "ema-pytorch==0.2.3",
        "accelerate==0.18.0",
        "py3Dmol==2.0.1.post1",
        "tqdm==4.65.0",
        "fsspec==2023.4.0",
        "Pillow==9.5.0",
        # "jupyter",
    ],
    dependency_links=[
        'https://download.pytorch.org/whl/cu113/'
    ],
    python_requires=">=3.9",
)
