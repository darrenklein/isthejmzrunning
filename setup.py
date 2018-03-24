from setuptools import setup

setup(
    name='isthejmzrunning',
    packages=['isthejmzrunning'],
    include_package_data=True,
    install_requires=[
        'flask',
        'gtfs-realtime-bindings'
    ],
)