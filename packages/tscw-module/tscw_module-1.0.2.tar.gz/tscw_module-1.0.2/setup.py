from setuptools import setup
from pathlib import Path
this_directory = Path(__file__).parent
long_description = this_directory.joinpath("README.md").read_text()


setup(name='tscw_module',
      version='1.0.2',
      description="Module to create input and process output of TSCW Software (c) UGS GmbH",
      long_description=long_description,
      author='Thomas Simader',
      author_email='simader@ugsnet.de',
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        ],
      packages=['tscw_module',],
      include_package_data=True,
      zip_safe=False,
      install_requires = [
        'matplotlib',
        'matplotlib-inline',
        'mplcursors',
        'numpy',
        'pandas',
        'pathlib',
        'scipy',
        'Sphinx',
        'sphinx-autodoc-typehints',
        'sphinx-rtd-theme',
        'sphinxcontrib-applehelp',
        'sphinxcontrib-devhelp',
        'sphinxcontrib-htmlhelp',
        'sphinxcontrib-jquery',
        'sphinxcontrib-jsmath',
        'sphinxcontrib-qthelp',
        'sphinxcontrib-serializinghtml',
        'sphinx_copybutton',
        'sphinxcontrib-video',
        'tqdm',
        'openpyxl',
      ]
)

# [tool.poetry.files]
# "README.md" = "README.md"
# "LICENSE.txt" = "LICENSE.txt"
# "calculateForces_benchmark.py" = "calculateForces_benchmark.py"
# "docs" = "docs"
# "tscw_module/ffmpeg" = "tscw_module/ffmpeg"
