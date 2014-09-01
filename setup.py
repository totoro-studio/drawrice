from distutils.core import setup

import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

options = {
    'build_exe': {
        'compressed': True,
        'includes': [
            # 'exportfile',
            # 'importfile',
            # 'lotterywindows',
            # 'prizeitems',
            # 'res',
            # 'config.xml',
            # 'lottery.db',
            # 'readme.txt',
        ],
        'path': sys.path + ['modules']
    }
}

executables = [
    Executable('main.py',  icon="./res/drawrice.png", base=base)
]

setup(
    name='抽米',
    version='V1.0-内测版',
    packages=[''],
    url='',
    license='',
    author='Tony',
    author_email='tonypublic@163.com',
    description='为公司企业组织机构各类抽奖活动定制，支持各种形式的抽奖活动',
    options=options,
    executables=executables,
)
