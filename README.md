# ProtenDiffusionGenerator_pip
## Instruction for local installation:
## Step 1: Create the virtual environment
```bash
conda create -n ProteinDiffusionGenerator python=3.9
conda activate ProteinDiffusionGenerator
```

## Step 2: Set up the environment and install the package
```bash
git clone https://github.com/Bo-Ni/ProtenDiffusionGenerator_pip.git
cd ProtenDiffusionGenerator_pip
bash prepare_virenv.sh
```
Accept all the updates during the process

Next, install the Protein Generator package
```bash
pip install -e .
```


## Step 3: Conduct the inference
```bash
cd notebooks
```
Test Model_B_Inference.ipynb for model B, Model_A_Inference.ipynb for model A.