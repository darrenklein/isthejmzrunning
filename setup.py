from setuptools import setup

setup(
    name='isthejmzrunning',
    packages=['isthejmzrunning'],
    version='0.0.1',
    author='Darren Klein',
    description='Fetch the current status of the New York City MTA\'s J, M, and Z trains.',
    include_package_data=True,
    python_requires='>3.6.4',
    install_requires=[
        'flask==0.12.2',
        'gtfs-realtime-bindings==0.0.5',
        'gunicorn==19.7.1',
    ],
)
