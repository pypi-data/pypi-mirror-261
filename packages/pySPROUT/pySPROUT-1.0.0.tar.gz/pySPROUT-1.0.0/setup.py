from setuptools import setup
from setuptools import find_packages
from pySPROUT.version import __version__

setup(name = 'pySPROUT',
    version=__version__,
    description='SPROUT: spectral sparsification helps restore the spatial structure at single-cell resolution.',
    url='https://github.com/deepomicslab/SPROUT/',
    author='Jingwan WANG',
    author_email='wanwang6-c@my.cityu.edu.hk',
    license='MIT',
    packages=find_packages(),
    install_requires=['umap-learn',
    'loess','tasklogger',
    'random2','scipy','numpy>=1.23.3',]
)
