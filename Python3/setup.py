from setuptools import setup, find_packages

setup(
    name='tail_estimation',
    version='0.1',
    description="Fork of Ivan Voitalov's tail-estimation code.",
    author='Stefan McCabe (original author Ivan Voitalov)',
    author_email='stefanmccabe@gmail.com',
    url='https://github.com/sdmccabe/tail-estimation',
    packages=find_packages(),
    install_requires=[
        # List any third-party dependencies required by your module
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
