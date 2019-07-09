from setuptools import setup

with open('README.md') as f:
    readme = f.read()

setup(
    name='yottadb_kernel',
    version='1.0',
    packages=['yottadb_kernel'],
    description='YottaDB kernel for Jupyter',
    long_description=readme,
    author='Winfried Bantel',
    author_email='winfried.bantel@hs-aalen.de',
    url='https://github.com/informatik-aalen/yottadb_kernel',
    install_requires=[
        'jupyter_client', 'IPython', 'ipykernel', 'pexpect'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
    ],
)
