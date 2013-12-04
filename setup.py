from distutils.core import setup

setup(
    name='hack-exe',
    version='0.1',
    url='https://github.com/gardaud/hack-exe',
    author='Guillaume Ardaud',
    author_email='gardaud@acm.org',
    description=('An animated terminal application that pretends to be hacking a website, just like in the movies.'),
    license='MIT',
    packages=['hack_exe'],
    package_data={},
    scripts=[
        'bin/hack.exe'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2',
        'Topic :: Artistic Software',
    ],
)
