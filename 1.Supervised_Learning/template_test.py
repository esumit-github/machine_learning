import os
from pathlib import Path
import logging
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

# logging string for despalyting the messages while executing this template.py
# instead of printing them the best practice is to log everything
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = '1.x_LinearRegression'

list_of_files = [
    #".github/workflows/.gitkeep",
    #f"src/{project_name}/README.md",
    #f"{project_name}/datasets/data.csv",
    #f"src/{project_name}/commands.txt",
    #f"src/{project_name}/config/configuration.py",
    #f"src/{project_name}/pipeline/__init__.py",
    #f"src/{project_name}/entity/__init__.py",
    #f"src/{project_name}/constants/__init__.py",
    #"config/config.yaml",
    #"dvc.yaml",
    #f"{project_name}/README.md",
    #f"{project_name}/requirements.txt",
    #f"{project_name}/commands.txt",
    f"{project_name}/research/trials.ipynb",
    #f"{project_name}/LASSO_Ridge_ElstNet_Regression_admns_dataset.py"
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    if filename == "tials":
        logging.info(f"This is the file path===>; {filepath}")

    else:
        logging.info(f"{filename} is already exists")
        
        
