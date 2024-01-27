from setuptools import setup, find_packages
import os
import re
import codecs
NAME = "mypackage"
META_PATH = os.path.join(NAME,"__init__.py")
REQUIREMENTS = []
CLASSIFIERS = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "Natural Language :: English",
    "License :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
]
HERE = os.path.abspath(os.path.dirname(__file__))
# Construye una direccion absoluta desde *parts* y devuelve el contenido del archivo
def read(*parts):
    with codecs.open(os.path.join(HERE,*parts),"rb","utf-8") as f:
        return f.read()
    
META_FILE = read(META_PATH)
# Se extrae __*meta*__ desde META_FILE
def find_meta(meta):
    meta_match = re.search(
        r"^__{meta}__ = ['\"]([^'\"]*)['\"]".format(meta=meta),META_FILE,re.M 
    )
    if meta_match:
        return meta_match.group(1)
    raise RuntimeError("Unable to find __meta__ string.".format(meta=meta))

if __name__ == "__main__":
    setup(name = "mypackage",
          description=find_meta("description"),
          license=find_meta("license"),
          url = find_meta("url"),
          version= find_meta("version"),
          author=find_meta("author"),
          author_email=find_meta("email"),
          long_description= open("README.md").read(),
          packages= find_packages(),
          zip_safe = False,
          install_requires = ["mysql-connector"],
            )