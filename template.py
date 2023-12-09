

import os
from pathlib import Path
import logging # Because every run i want to show the logs in terminal


logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')

project_name = 'wasteDection' # This is root folder in which contain all the components related to the project

# Every Folder Must have an constructor file
list_of_files = [

    '.github/workflows/.gitkeep', # .github folder is needed for CI/CD deployment.changes in github it will automatically deploy in cloud.
                                  # .gitkeep because i can't push empty folder(workflows) in github , so i put a file in workflows. 

    'data/.gitkeep', # What ever user will input it'll save in data folder in backend.

    f'{project_name}/__init__.py',# i want to use 'wasteDection' as a local package. And what ever components inside the local package,i can import them to other file as well.
                                  # To Import them i need to install it as a local package and to install it i need a constructor.
    f'{project_name}/components/__init__.py',


    f'{project_name}/components/data_ingestion.py',
    f'{project_name}/components/data_validation.py',
    f'{project_name}/components/model_trainer.py',

    f'{project_name}/constant/__init__.py',
    f'{project_name}/constant/training_pipeline/__init__.py',
    f'{project_name}/constant/application.py',
    f'{project_name}/entity/config_entity.py',
    f'{project_name}/entity/artifacts_entity.py',
    f'{project_name}/exception/__init__.py', # It will contain our custom exception
    f'{project_name}/logger/__init__.py', # Contains our custom log
    f'{project_name}/pipeline/training_pipeline.py',
    f'{project_name}/utils/__init__.py',
    f'{project_name}/utils/main_utils.py', # It will contain all the utility related function
    'research/trials.ipynb',
    'templates/index.html',
    'app.py',
    'Dockerfile',
    'requirements.txt',
    'setup.py'
]

for filepath in list_of_files:
    filepath = Path(filepath) # in windows we define path as backward slash but Here every path i defined is contain forward slash.
                              # So that's why we need Path() it will automatically detect your operating system and this will convert that path to Your Operating System's desired path.
    filedir , filename = os.path.split(filepath)
    if filedir != '':
        os.makedirs(filedir , exist_ok=True)
        logging.info(f'Creating Directory: {filedir} for the file {filename}')

    if (not os.path.exists(filename)) or (os.path.getsize(filename) == 0):
        with open(filepath , 'w') as f:
            pass # because i only interested for creating file not the content in that file.
            logging.info(f'Creating empty file :{filename}')
    else:
        logging.info(f'{filename} is already created')
