from setuptools import setup, find_packages

setup(
    name='CipherAlgos',
    version='0.1.0',
    author='Ilyad',
    author_email='idvb188@gmail.com',
    description='A simple encryption package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/idvb188/CipherAlgos',
    license='MIT',
    packages=find_packages(),
    install_requires=[
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',

    project_urls={
        "Source": "https://github.com/idvb188/CipherAlgos",
    },
)
