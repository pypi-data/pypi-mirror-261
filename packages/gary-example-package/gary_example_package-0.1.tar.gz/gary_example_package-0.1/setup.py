from setuptools import setup, find_packages

setup(
    name='gary_example_package',
    version='0.1',
    packages=find_packages(),
    description='A simple gary_example_package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='GARY',
    author_email='gary109@gmail.com',
    license='MIT',
    install_requires=[
        # 依賴包列表，本例不需要
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
