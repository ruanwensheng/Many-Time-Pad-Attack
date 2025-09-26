from setuptools import find_packages, setup
from typing import List
# find_packeges will run the init.py file in each folder to check if it is a package
def get_req(file_path: str)->List[str]:
    req = []
    with open(file_path) as f:
        req = f.readlines()
        req = [i.replace('\n',"") for i in req]
        if hyphen in req:
            req.remove(hyphen)
    return req
hyphen = '-e .'
setup(name='ds1',
      version='0.0.1',
      author='VT',
      author_email='ruanwensheng106@gmail.com',
      url='https://www.python.org/sigs/distutils-sig/',
      packages=find_packages(),
      install_requires=get_req('req.txt')
     )
