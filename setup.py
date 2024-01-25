from setuptools import setup, find_packages

if __name__ = "__main__":
    setup(name = "mypackage",
          description="Aplicación Python con MySQL",
          license="MIT",
          url = "https://github.com/Luis89Flores/CRUD_Python_MySQL",
          version= "0.0.1",
          author="Luis Flores",
          author_email="luis.flores@gmail.com",
          long_description= open("README.md").read(),
          packages= find_packages(),
          zip_safe = False,
          install_requires = ["tkinter","mysql-connector"],
          classifiers=[
              "Development Status :: 5 - Production/Stable",
              "Intended Audience :: Developers",
              "Natural Language :: English",
              "License :: MIT License",
              "Operating System :: OS Independent",
              "Programming Language :: Python",
          ],)