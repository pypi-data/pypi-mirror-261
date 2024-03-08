# setup.py
from setuptools import setup, find_packages
import os , sys

cam_name = 'cam_utils'
cam_version = '0.1.1'


setup(
    name = 'cam_utils',
    version = cam_version,
    packages=find_packages(),
    license='MIT',
    description='CAM UTILS LIBRARY TO PYTHON PROJECTS',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author = 'CAM TECNOLOGIA LTDA ME',
    author_email='atendimento@camtecnologia.com.br',
    url='https://repo.camvoip.com.br/engenharia/bibliotecas-cam/python/cam_utils',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
