import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='OrthogonalBarcodes',  
     version='0.1',
     scripts=['src/OrthogonalBarcode.py'] ,
     author="Kenny Pavan",
     author_email="kennypavan@protonmail.com",
     description="A simple Python class for generating custom orthogonal DNA/RNA barcodes.",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/kennypavan/OrthogonalBarcodes",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )