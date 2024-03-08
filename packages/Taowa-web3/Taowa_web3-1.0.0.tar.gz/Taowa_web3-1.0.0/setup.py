from setuptools import setup



from setuptools import setup, find_packages

setup(
    name='Taowa_web3',
    version='1.0.0',
    description='',
    long_description_content_type='text/markdown',
    author='',
    author_email='',
    packages=find_packages(),

    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    # 如果有依赖包，可以在此处添加
    install_requires=[
        'web3',
    ],
)