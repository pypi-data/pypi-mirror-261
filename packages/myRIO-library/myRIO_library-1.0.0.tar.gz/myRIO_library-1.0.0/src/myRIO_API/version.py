# version.py
__version__ = "1.0.0"

""" version notes
0.2.0: added __del__ method to myRio class to close the connection
       to the myRIO (2024/03/05)
0.2.3: fixed the Default.lvbitx error: now the file is distributed 
       with the package. We use the relative folder of __file__ (2024/3/6)
0.3.0: Added examples. Fixed a bug in the digital write function. (2024/3/7)
0.3.1: Bug fix: examples folder was not being copied to the site-packages
0.4.0: Addded Flask-waitress-API server (2024/03/11)
1.0.0: API_client added (2024/03/12)
"""
