# import time
import os
# import glob
import shutil
# import subprocess
# from distutils.core import run_setup
from setuptools import setup
# from packaging.version import Version


if __name__ == '__main__':
    # 配布パッケージの作成
    distribution = setup(script_name='setup.py', script_args=['sdist', '--formats=tar'])

    # 生成された .tar ファイルを探す
    for path in distribution.dist_files[0]:
        if os.path.exists(path) and path.endswith('.tar'):
            sdist_path = path
            break

    copy_to = r'G:\マイドライブ\60. 人体班\241012_あしも'
    os.makedirs(copy_to, exist_ok=True)
    shutil.copy(sdist_path, copy_to)

    copy_to = r'G:\マイドライブ\60. 人体班\241012_あしも\Project\JOS-3'
    # os.makedirs(copy_to, exist_ok=True)
    if os.path.exists(copy_to):
        shutil.rmtree(copy_to)
    shutil.copytree(r'C:\Users\takahashi-yosh\GitHub\JOS-3', copy_to)