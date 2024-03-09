import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
  name = 'ip_sibylsys',
  version = '0.1.0',
  license='MIT',
  author = 'DreamGallery',
  author_email = 'infinite.virtual.reality.43@gmail.com',
  long_description=long_description,
  long_description_content_type="text/markdown",
  url = 'https://github.com/DreamGallery/IP-Sibyl-Core',
  packages=setuptools.find_packages(),
  classifiers=[
    'Development Status :: 4 - Beta', 
    "Operating System :: OS Independent",
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',   
    'Programming Language :: Python :: 3.12', 
  ],
)
