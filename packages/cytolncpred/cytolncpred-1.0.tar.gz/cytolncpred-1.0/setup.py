from setuptools import setup, find_packages
from setuptools import  find_namespace_packages
# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='cytolncpred',
    version='1.0',
    description='A tool to predict probability of lncRNA localizing to Cytoplasm',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license_files = ('LICENSE.txt',),
    url='https://github.com/raghavagps/cytolncpred', 
    packages=find_namespace_packages(where="src"),
    package_dir={'':'src'},
    entry_points={ 'console_scripts' : ['cytolncpred = cytolncpred.python_scripts.cytolncpred:main']},
    include_package_data=False,
    python_requires='>=3.6',
    install_requires=[
        'numpy', 'pandas', 'argparse', 'torch', 'einops', 'peft', 'omegaconf', 'evaluate', 'accelerate', 'transformers==4.29'] # Add any Python dependencies here

)
