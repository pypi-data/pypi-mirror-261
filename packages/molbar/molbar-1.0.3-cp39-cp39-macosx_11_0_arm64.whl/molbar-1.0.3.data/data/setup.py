from skbuild import setup

setup(
    name="molbar",
    version="1.0.3",
    description="a minimal example package (fortran version)",
    packages=['molbar'],
    cmake_args=['-DSKBUILD=ON']
)