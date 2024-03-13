# © https://github.com/MrMKN

import re
import setuptools


# find repository version
with open("fast2sms/__init__.py", encoding="utf-8") as f:
    version = re.findall(r"__version__ = \"(.+)\"", f.read())[0]

# read readme.md
with open("README.md", encoding="utf-8") as f:
    readme = f.read()
  
setuptools.setup(
    name="fast2sms",
    version=version,
    author="MrMKN",
    long_description_content_type="text/markdown",
    long_description=readme,
    license='GNU General Public License v3.0',
    description='Python package for Fast2 Sms API Client',                           
    package_data={
      "fast2sms": ["py.typed"],
    },
    url="https://github.com/MrMKN/fast2sms",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    py_modules=["fast2sms"],
)