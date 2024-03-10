# Github: https://github.com/beh185
# Telegram: https://T.me/BZHNM
# e-mail: BehnamH.dev@gmail.com
# ____________________________________________

from setuptools import setup, find_packages

with open(__file__.replace('setup.py', 'README.md'), 'r') as f:
    long_description = f.read()

setup(
        name="unsplash_lib",
        version='0.0.3',
        description='A python library that can download from Unsplash and also manage user account',
        long_description=long_description,
        long_description_content_type='text/markdown',
        author='Behnam',
        author_email='Behii@tutanota.com',
        url='https://github.com/beh185/unsplash_lib',
        license='MIT',
        keywords='download from Unsplash',
        packages=find_packages(),
        include_package_data=True,                                                  
        install_requires=['requests', 'tqdm'],
        python_requires='~=3.7',
        classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
        )
