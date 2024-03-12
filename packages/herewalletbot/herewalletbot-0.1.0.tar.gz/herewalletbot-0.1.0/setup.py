from setuptools import setup, find_packages

setup(
    name='herewalletbot',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'selenium',
        'Pillow',
        'qrcode',
    ],
    entry_points={
        'console_scripts': [
            'herewalletbot=herewalletbot.herewalletbot:main',
        ],
    },
)
