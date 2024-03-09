from setuptools import setup, find_packages

setup(
    name='tars_signal_processing',
    version='0.1',
    packages=find_packages(),
    # packages=[json, numpy, scipy],
    description='Action signals processing package',
    author='Thanos Papadopoulos',
    author_email='thanos.papadopoulos@netradyne.com',
    url='https://github.com/netradyne/tars.git',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)