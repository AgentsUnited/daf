import setuptools

long_description = "A package that provides a base class for implementing modules in the Agents United Dialogue and Argumentation Framework"

setuptools.setup(
     name='daf',
     version='0.1',
     author="Mark Snaith",
     author_email="mark@arg.tech",
     description="Package for creating modules for the Agents United Dialogue and Argumentation Framework",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://www.agents-united.org",
     packages=setuptools.find_packages(),
     install_requires = [
    'stomp.py==4.1.24',
    'pymongo'
     ],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
         "Operating System :: OS Independent",
     ],
 )
