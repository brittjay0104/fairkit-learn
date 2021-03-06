import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='fairkit_learn',  
     version='1.9',
     scripts=['fairkit_learn'] ,
     author="Brittany Johnson, Jesse Bartola, Rico Angell, Katherine Keith, Sam Witty, Stephen Giguere, and Yuriy Brun",
     author_email="bijohnsonphd@gmail.com",
     description="A machine learning fairness toolkit",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/brittjay0104/fairkit-learn",
     packages=setuptools.find_packages(),
     package_data={'fklearn': ['interface/static/data/explanations.json', 'interface/static/css/styles-notebook.css']},
    include_package_data=True,
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
