from skbuild import setup

setup(
    name="molbar",
    version="0.0.0",
    description="Molecular Barcode (MolBar): Molecular Identifier for Organic and Inorganic Molecules",
    packages=['molbar'],
    cmake_args=['-DSKBUILD=ON']
)