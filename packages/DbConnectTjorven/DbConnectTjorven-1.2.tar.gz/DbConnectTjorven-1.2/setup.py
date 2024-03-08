from distutils.core import setup

setup(
    name='DbConnectTjorven',
    packages=['DbConnectTjorven'],
    version='1.2',
    license='GNU',
    descriptoin='test',
    author='Tjorven Burdorf',
    author_email='BurdorfTjorven@gmail.com',
    url='https://github.com/tj0vtj0v/DbConnect',
    download_url='https://github.com/tj0vtj0v/DbConnect/archive/refs/tags/Alpha.tar.gz',
    keywords=['MYSQL', 'Database', 'Connector', 'Private'],
    install_requires=['mysql-connector-python'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
)
