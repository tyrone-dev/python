'''
__init__.py is used to initialize python packages/modules

Given the following file structure:

package/
    __init__.py
    file.py
    file2.py
    subpackage/
        __init__.py
        submodule1.py
        submodule2.py

the inclusion of __init__.py indicated to Python Interpreter that the dir should be
treated as a Python Package - can 'import package'

__init__.py can be empty, but it is useful to use it to perform setup needed for the package:
    *imports
    *loading paths
    *etc

* imports : useful to import selected Classes, functions into the package level so that they
            can be imported from the package

          example: empty __init__.py: from package.file import File

          add to __init__.py:
            from file import File

            now can import File from package: from package import File
                (function, classes brought into package level)

* can also make subpackages/modules available with the __all__ variable:
    when doing:
        from package import *

    interpreter looks for __all__ var in __init__ that lists modules to import

        need to add subpackages/modules:

        in __init__.py in subpackages:
            
            __all__ = ['submodule1', 'submodule2']

'''

from file1 import file_func

__all__ = ['submodule1', 'submodule2']
