from setuptools import setup

setup(
    name='rstblog',
    version='1.0',
    author='Armin Ronacher <armin.ronacher@active-4.com>',
    packages=['rstblog', 'rstblog.modules'],
    description='',
    long_description='',
    license='BSD License',
    package_data={'rstblog': [
        'templates/*.html',
        'templates/blog/*.html'
    ]},
    entry_points = {
        'console_scripts': [
            'rstblog-build = rstblog.cli:build',
            'rstblog-serve = rstblog.cli:serve',
        ],
    },
    install_requires=['PyYAML', 'Babel', 'blinker', 'docutils', 'Jinja2>=2.4', 'Werkzeug']
)
