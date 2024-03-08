# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""=====================================
@author : xiaozhengyi
@time   : 2024/3/8
@contact: 201930222056@hunnu.edu.cn
@desc   :
====================================="""
from setuptools import setup, find_packages

setup(
    name='cwruhunnu',  # 包的名称
    version='0.1.0',  # 包的版本
    author='xiaozhengyi',  # 你的名字
    author_email='201930222056@hunnu.edu.cn',  # 你的邮箱
    description='导入cwru数据集和一些预操作',  # 包的描述
    packages=find_packages(),  # 系统自动从当前目录开始找包
    package_data={
    'hunnucwru': ['CWRU/0HP/**/*.mat', 'CWRU/1HP/**/*.mat', 'CWRU/2HP/**/*.mat', 'CWRU/3HP/**/*.mat'],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    install_requires=[  # 该库需要的依赖库
        'torch',
        'numpy',
        'scipy',
        'scikit-learn',
        'tqdm',
        'requests',
    ],
    python_requires='>=3.6',
    license="apache 3.0",
    # include_package_data=True,




)
