import imported_file

imported_file.mir()
imported_file.hey()

from imported_file import *

mir()
hey()

from imported_file import mir as m, hey as h

m()
h()