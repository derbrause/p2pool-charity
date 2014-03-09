from distutils.core import setup
from distutils.extension import Extension

# edit include_dirs and library_dirs to point to the corresponding folders on your system

setup(name="einsteinium_subsidys",
    ext_modules=[
        Extension("einsteinium_subsidy", ["einsteinium_GetBlockBaseValue.cpp"],
        libraries = ["boost_python"],
        include_dirs = ["c:/boost_1_55_0"],
        library_dirs = ["c:/boost_1_55_0/stage\lib"])])
