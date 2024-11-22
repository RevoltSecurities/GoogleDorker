from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as streamr:
    long_description = streamr.read()

setup(
    name='GoogleDorker',
    version='1.0.1',
    author='D.Sanjai Kumar',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RevoltSecurities/GoogleDorker",
    author_email='bughunterz0047@gmail.com',
    description='GoogleDorker - Unleash the power of Google dorking for ethical hackers with custom search precision.',
    packages=find_packages(),
    install_requires=[
        'aiofiles>=24.1.0',
        'alive_progress>=3.2.0',
        'appdirs>=1.4.4',
        'art>=6.3',
        'colorama>=0.4.4',
        'fake_useragent>=1.5.1',
        'httpx>=0.27.2',
        'PyYAML>=6.0.2',
        'Requests>=2.32.3',
        'setuptools>=74.1.2',
    ],
    entry_points={
        'console_scripts': [
            'dorker = dorker.dorker:main'
        ]
    },
)
