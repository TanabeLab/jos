import time
import os
# import glob
import shutil
# import subprocess
# from distutils.core import run_setup
from setuptools import setup
# from packaging.version import Version

# 下記は入力値
# ---------------------------
# MAJOR_MINOR = '0.4.'  # __init__.pyは上書きされる
new_version = '0.6.0.dev2'

if __name__ == '__main__':
    # latest_package =  glob.glob('dist/*.tar')[-1]
    # latest_version = Version(os.path.basename(latest_package).replace('dx_database-', '').replace('.tar', ''))
    # for micro in range(1000):
    #     new_version = Version(MAJOR_MINOR + str(micro))
    #     if latest_version < new_version:
    #         break
    #
    with open('src/jos3/__init__.py', 'rt') as f:
        s = f.read().split('\n')
        s[-1] = f'__version__ = "{str(new_version)}"'

    with open('src/jos3/__init__.py', 'wt') as f:
        f.write('\n'.join(s))

    # 配布パッケージの作成
    distribution = setup(
        script_name='setup.py',
        script_args=['sdist', '--formats=tar'],
        version=new_version,
    )

    # 生成された .tar ファイルを探す
    for path in distribution.dist_files[0]:
        if os.path.exists(path) and path.endswith('.tar'):
            sdist_path = path
            break

    copy_to = r'G:\マイドライブ\60. 人体班\241012_asm'
    os.makedirs(copy_to, exist_ok=True)
    shutil.copy(sdist_path, copy_to)


    # copy_to = r'G:\マイドライブ\60. 人体班\241012_asm\Project\JOS-3'
    # # os.makedirs(copy_to, exist_ok=True)
    # if os.path.exists(copy_to):
    #     shutil.rmtree(copy_to)
    # shutil.copytree(r'C:\Users\takahashi-yosh\GitHub\JOS-3', copy_to)