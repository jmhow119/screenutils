from distutils.core import setup

setup(
    name='screenutils',
    version='0.0.1dev',
    packages=['screenutils',],
    license='GNU Public License >=2 (ask me if you want other)',
    author="Christophe Narbonne",
    author_email="@Christophe31",
    description =
    "Handle gnu-screen: creates/close/list sessions, injects commands...",
    long_description=open('README.txt').read(),
)
