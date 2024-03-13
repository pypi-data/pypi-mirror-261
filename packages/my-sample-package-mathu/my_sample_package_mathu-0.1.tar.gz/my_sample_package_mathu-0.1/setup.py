from setuptools import setup, find_packages

setup(
    name='my_sample_package_mathu',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # Add any dependencies your package needs
    ],
    author='mathusuthanan_1981',
    author_email='mathusuthanan.thiruvengadam@gmail.com',
    description='Sample test package to demonstrate package distribution',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/mathusuthanan_1981/my_sample_package_mathu',
    license='MIT',
)