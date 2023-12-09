
from setuptools import find_packages,setup

setup(

    name= 'wasteDetection',
    version= '0.0.0',
    author='Arup Sankar Roy',
    author_email='arupsankarroy11@gmail.com',
    packages=find_packages(), # find_packages() will forward the constructor file in every folder.
                              # wherever the constructor is there it will try to install that folder as a local package.
                              # EX: i want to import 'data_ingestion' in a Package Manner : How i do it ?
                              # from wasteDetection.components import data_ingestion 
                              # This is Happened Due to setup.py file
    install_requires = []
)