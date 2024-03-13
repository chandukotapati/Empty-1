# Data Types

# Python contains a number of build-in modules
# Open CMD:
# --> python3
# --> help()
# --> modules

# __future__          _testmultiphase     getopt              runpy
# __hello__           _thread             getpass             sched
# __phello__          _threading_local    gettext             secrets
# _abc                _tokenize           glob                select
# _aix_support        _tracemalloc        graphlib            selectors
# _ast                _typing             grp                 setuptools
# _asyncio            _uuid               gzip                shelve
# _bisect             _warnings           hashlib             shlex
# _blake2             _weakref            heapq               shutil
# _bootsubprocess     _weakrefset         hmac                signal
# _bz2                _xxsubinterpreters  html                site
# _codecs             _xxtestfuzz         http                sitecustomize
# _codecs_cn          _zoneinfo           idlelib             smtpd
# _codecs_hk          abc                 idna                smtplib
# _codecs_iso2022     aifc                imaplib             sndhdr
# _codecs_jp          antigravity         imghdr              socket
# _codecs_kr          argparse            imp                 socketserver
# _codecs_tw          array               importlib           sqlite3
# _collections        asgiref             inspect             sqlparse
# _collections_abc    ast                 io                  sre_compile
# _compat_pickle      asynchat            ipaddress           sre_constants
# _compression        asyncio             itertools           sre_parse
# _contextvars        asyncore            json                ssl
# _crypt              atexit              keyword             stat
# _csv                audioop             lib2to3             statistics
# _ctypes             base64              linecache           string
# _ctypes_test        bdb                 locale              stringprep
# _curses             binascii            logging             struct
# _curses_panel       bisect              lzma                subprocess
# _datetime           builtins            mailbox             sunau
# _dbm                bz2                 mailcap             symtable
# _decimal            cProfile            marshal             sys
# _distutils_hack     calendar            math                sysconfig
# _elementtree        certifi             mimetypes           syslog
# _functools          cgi                 mmap                tabnanny
# _hashlib            cgitb               modulefinder        tarfile
# _heapq              charset_normalizer  multiprocessing     telnetlib
# _imp                chunk               netrc               tempfile
# _io                 cmath               nis                 termios
# _json               cmd                 nntplib             test
# _locale             code                ntpath              textwrap
# _lsprof             codecs              nturl2path          this
# _lzma               codeop              numbers             threading
# _markupbase         collections         numpy               time
# _md5                colorsys            opcode              timeit
# _multibytecodec     compileall          operator            tkinter
# _multiprocessing    concurrent          optparse            token
# _opcode             configparser        os                  tokenize
# _operator           contextlib          pathlib             tomllib
# _osx_support        contextvars         pdb                 trace
# _pickle             copy                pickle              traceback
# _posixshmem         copyreg             pickletools         tracemalloc
# _posixsubprocess    crypt               pip                 tty
# _py_abc             csv                 pipes               turtle
# _pydecimal          ctypes              pkg_resources       turtledemo
# _pyio               curses              pkgutil             types
# _queue              dataclasses         platform            typing
# _random             datetime            plistlib            unicodedata
# _scproxy            dbm                 poplib              unittest
# _sha1               decimal             posix               urllib
# _sha256             difflib             posixpath           urllib3
# _sha3               dis                 pprint              uu
# _sha512             distutils           profile             uuid
# _signal             django              pstats              venv
# _sitebuiltins       doctest             psycopg2            warnings
# _socket             dotenv              pty                 wave
# _sqlite3            email               pwd                 weakref
# _sre                encodings           py_compile          webbrowser
# _ssl                ensurepip           pyclbr              wheel
# _stat               enum                pydoc               wsgiref
# _statistics         errno               pydoc_data          xdrlib
# _string             faulthandler        pyexpat             xml
# _strptime           fcntl               queue               xmlrpc
# _struct             filecmp             quopri              xxlimited
# _symtable           fileinput           random              xxlimited_35
# _sysconfigdata__darwin_darwin fnmatch             re                  xxsubtype
# _testbuffer         fractions           readline            zipapp
# _testcapi           ftplib              reprlib             zipfile
# _testclinic         functools           requests            zipimport
# _testimportmultiple gc                  resource            zlib
# _testinternalcapi   genericpath         rlcompleter         zoneinfo

# what is class: class is blueprint or a template
# E.g.: Number: This build-in class contains properties, methods, objects

# what is object: an object is an instance of class, object name and class name must be same

# what are datatypes in python?
# Numbers: int float boolean complex

# Sequences : list, tuple, set, frozenset, bytes, bytearray, str

# Boolean: bool

# Mapping : dict

# Other datatypes: None

# Shell
# datatype --> class --> object --> default value
#  int --> class int --> int()  --> 0

# float --> class float --> float() --> 0.0

# bool --> class bool --> bool() --> False

# statement
# a = 10
# b = 20
# print(a+b)
# print(a-b)
# print(a*b)
#
# print(a.__add__(b))
# print(a.__sub__(b))
# print(a.__mul__(b))

# Employee
username = "Sai Kiran"
user_id = 45678
user_sal = 10000.00
user_designation = "software trainee"
user_present = True

# username, user_id, user_sal, user_designation, user_present = variables
# what is variable: variable hold the value stores the value

print(username, user_id, user_sal, user_designation, user_present)
# Sai Kiran 45678 10000.0 software trainee True

# type(variable)
print(type(username), type(user_id), type(user_sal), type(user_designation), type(user_present))
# <class 'str'> <class 'int'> <class 'float'> <class 'str'> <class 'bool'>
