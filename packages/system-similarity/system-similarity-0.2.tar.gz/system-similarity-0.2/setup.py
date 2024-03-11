from distutils.core import setup

setup(
    name='system-similarity',
    packages=['system-similarity'],
    version='0.2',
    license='MIT',
    description='Welcome to system-similarity, a powerful system designed to find similarities between articles using '
                'advanced natural language processing techniques. This system incorporates a specialized submodule '
                'for Article Recommendation, leveraging OpenAI modules for vector generation, and utilizing numpy and '
                'pandas for data cleaning and similarity calculations.',
    author='Cheng Phansivang',
    author_email='phansivang@gmail.com',
    url='https://github.com/user/reponame',
    download_url='https://github.com/user/reponame/archive/v_01.tar.gz',
    keywords=['system-similarity', 'Vectors Similarity', 'Article Recommendation', 'OpenAI Similarity'],
    install_requires=[
        'kiwisolver==1.4.5',
        'matplotlib==3.8.3',
        'numpy==1.26.4',
        'openai==1.13.3',
        'packaging==23.2',
        'pandas==2.2.1',
        'pillow==10.2.0',
        'plotly==5.19.0',
        'sklearn',
        'urllib3==2.2.1',
        'utils==1.0.2',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
