from setuptools import setup, find_packages

setup(
    name='geodata',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['django>=3.2'],
    author='Norman Mjomba',
    author_email='mjomban@gmail.com',
    description='A Django package for geographical data (regions, subregions, countries, states, cities)',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/mjombanorman/django-geodata.git',
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
