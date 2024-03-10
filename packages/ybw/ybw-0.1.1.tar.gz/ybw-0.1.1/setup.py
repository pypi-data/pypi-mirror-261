# @Author: BingWu Yang <detailyang>
# @Date:   2016-09-20T20:27:36+08:00
# @Email:  detailyang@gmail.com
# @Last modified by:   detailyang
# @Last modified time: 2016-09-20T15:23:48+08:00
# @License: The MIT License (MIT)


from setuptools import setup, find_packages


setup(
    name='ybw',
    version='0.1.1',
    keywords=('ybw detailyang'),
    description='ybw',
    license='MIT License',
    install_requires=[
    ],
    entry_points={
        'console_scripts': [
            'ybw=ybw.index:main',
        ],
    },
    author='detailyang',
    author_email='detailyang@gmail.com',

    packages=find_packages(),
    platforms='any',
)
