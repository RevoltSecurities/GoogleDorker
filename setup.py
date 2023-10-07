from setuptools import setup, find_packages

setup(
    name='Dorker',
    version='1.0.0',
    author='D.Sanjai Kumar',
    author_email='bughunterz0047@gmail.com',
    description='An advanced level CLI and API based Gogle dorking tool',
    packages=find_packages(),
    install_requires=[
        'google_api_python_client==2.98.0',
        'colorama==0.4.4',
        'httpx==0.25.0',
        'PyYAML==6.0.1',
        'setuptools==68.1.2'
    ],
    entry_points={
        'console_scripts': [
            'dorker = dorker.dorker:main'
        ]
    },
)
