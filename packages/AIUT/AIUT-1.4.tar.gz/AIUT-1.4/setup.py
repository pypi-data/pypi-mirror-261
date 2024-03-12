from setuptools import setup, find_packages

setup(
    name='AIUT',
    version='1.4',
    
    packages=find_packages(),
    package_data={'AIUT': ['src/*.py', 'images/*.png', 'settings/*.ini','requirements/*.txt','modules/*.py']},
    install_requires=[
        # Add any dependencies your project needs
        'Pillow', 'openai==1.3.5',"prettytable"
    ],
    entry_points={
        'console_scripts': [
            'AIUT=AIUT.src.AIUT:main',  
        ],
    }
)
