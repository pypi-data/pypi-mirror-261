from setuptools import setup

setup(
    name='discordpy_bypass',
    version='1.1',
    packages=['discordpy_bypass'],
    install_requires=[
        'requests',
        'pywin32; sys_platform == "win32"',
    ],
)
