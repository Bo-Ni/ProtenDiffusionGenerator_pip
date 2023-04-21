#!/bin/bash

# for debug purpose
# conda create --prefix=/HDD_bni/1_git_projects/VirEnv_Publication/1_test python=3.9
# conda activate /HDD_bni/1_git_projects/VirEnv_Publication/1_test

## excute the script within your virtual environment

# conda install python=3.8

# ===========================================================


# conda install python=3.8

# conda install python=3.8
## 2. on Pytorch: match this for omegafold
pip install torch==1.12.0+cu113 torchvision==0.13.0+cu113 torchaudio==0.12.0 --extra-index-url https://download.pytorch.org/whl/cu113


## 4. other packages
pip install pandas
pip install seaborn
pip install scikit-learn
# pip install numpy==1.22.4
# pip install pandas==1.5.3
pip install biopython
pip install kornia
pip install einops
pip install einops-exts
pip install pytorch-warmup
pip install ema-pytorch
pip install accelerate
pip install py3Dmol
pip install tqdm
pip install fsspec
pip install Pillow



## 5. on Tensorflow
conda install -c conda-forge cudatoolkit=11.8.0
pip install nvidia-cudnn-cu11==8.6.0.163
CUDNN_PATH=$(dirname $(python -c "import nvidia.cudnn;print(nvidia.cudnn.__file__)"))
echo $CUDNN
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CONDA_PREFIX/lib/:$CUDNN_PATH/lib
mkdir -p $CONDA_PREFIX/etc/conda/activate.d
echo 'CUDNN_PATH=$(dirname $(python -c "import nvidia.cudnn;print(nvidia.cudnn.__file__)"))' >> $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CONDA_PREFIX/lib/:$CUDNN_PATH/lib' >> $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
# pip install --upgrade pip
pip install tensorflow==2.12.0


## 1. on Ipython
pip install jupyter
pip install ipython
pip install ipykernel

# install omegafold from the source
## 3. omegafold
conda install -c anaconda git
pip install git+https://github.com/HeliXonProtein/OmegaFold.git@v1.1.0



