from setuptools import setup, find_packages

setup(
    name="comgen", 
    version="0.0.21",
    description="explore chemical compositions",
    packages=find_packages(),
    package_data={'comgen.util': ['data_files/*.json', 'data_files/*.txt']},    
    install_requires=['pymatgen>=2022.5.26', 'z3-solver>=4.8.17.0', 'onnx>=1.15.0', 'ElMD>=0.4.25']
)
