# ProtenDiffusionGenerator_pip
## Instruction for local installation:
### Step 1: Create the virtual environment with basic packages
```bash
conda create -n ProteinDiffusionGenerator python=3.9 git jupyter jupyterlab dssp -c anaconda -c conda-forge -c salilab
conda activate ProteinDiffusionGenerator
```

### Step 2: Install the ProteinDiffusionGenerator package
Download the package.
```bash
git clone https://github.com/Bo-Ni/ProtenDiffusionGenerator_pip.git
```
Next, install the package locally.
```bash
cd ProtenDiffusionGenerator_pip
pip install -e .
```

### Step 3: Conduct the inference
```bash
jupyter notebook
```
Test model B using ./notebooks/Model_B_Inference.ipynb and model A using ./notebooks/Model_A_Inference.ipynb

### Save the environment if needed
```bash
conda env export > environment.yml
```