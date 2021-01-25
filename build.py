import os
import PyInstaller.__main__

def main():
    PyInstaller.__main__.run([
    '--log-level=ERROR',
    '--noconsole',
    '--add-data=conf/*;conf',
    '--add-data=routes/*;routes',
    '--add-data=controllers/*;controllers',
    'server.py'
    ])

if __name__ == '__main__': 
     main()
