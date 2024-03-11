from setuptools import setup, find_packages

setup(
    name='algo_fun_add',
    version='0.2.0',
    packages=find_packages(),
    install_requires=[
        # List your project dependencies here
    ],
    entry_points={
        'console_scripts': [
            # Add any command-line scripts here
        ],
    },
    author='Christophe Lagaillarde',
    author_email='chrislag94@gmail.com',
    description='Simple script to add numbers together',
    license='MIT',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://gitlab.com/ChristopheLagaillarde/add_algo',
    package_data={'': ['*.asc']},

)

