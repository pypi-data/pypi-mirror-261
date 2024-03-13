import numpy as np
from molbar.exceptions.error import FileNotFound, NotXYZFormat, NotCoordFormat, NotMolFormat, NotV2000orV3000Format, FileFormatNotSupported
import random

class FileReader:
    """
    A class to read a file containing molecular information such as coordinates and elements. 

    Methods:
        read_file(): Reads number of atoms in the molecule and geometry from either a .xyz-, coord- or .sdf/.mol-file.

    """

    def __init__(self, filepath=None):
        """
        Initializes the FileReader class.
        Args:
            filepath (str): Path to file.
        """

        if not hasattr(self, 'filepath'):

            self.filepath = filepath

    def read_file(self, filepath="") -> tuple:
        """
        Reads number of atoms in the molecule, cartesian coordinates and present atoms from .xyz file.

        Args:
            filepath (str): Path to file. Defaults to self.filepath.
        Returns:
            Tuple containing the number of atoms in the molecule (int), cartesian coordinates (np.ndarray) and present atoms (np.ndarray).

        Raises:
            XYZNotFound: If the file does not exist.
            NotXYZFormat: If the input geometry is not in .xyz format.
        """

        if filepath != "":

            self.filepath = filepath

        if self.filepath.endswith(".xyz"):
            n_atoms, geometry, atoms = self._read_xyz_file()

        elif self.filepath.endswith(".mol") | self.filepath.endswith(".sdf"):

            n_atoms, geometry, atoms = self._read_mol_file()

            self.is_2D = self._check_2D_molfile(geometry)
            
        elif self.filepath.endswith(".coord") | self.filepath.endswith(".tmol"):

            n_atoms, geometry, atoms = self._read_coord_file()

        else:
            raise FileFormatNotSupported(self.filepath)

        return n_atoms, geometry, atoms
    
    def _read_xyz_file(self):
        """
        Reads number of atoms in the molecule, cartesian coordinates and present atoms from .xyz file.

        Raises:
            FileNotFound: If the file does not exist.
            NotXYZFormat: If the input geometry is not in .xyz format.

        Returns:
            tuple: n_atoms, geometry, atoms
        """
        try:
            with open(self.filepath, 'r') as f:
                n_atoms = int(f.readline())
                comment = f.readline().strip()

                atoms, geometry = [], []
                for _ in range(n_atoms):
                    line = f.readline().split()
                    atoms.append(line[0])
                    geometry.append([float(xyz) for xyz in line[1:]])

        except OSError:
            raise FileNotFound(self.filepath)

        except (ValueError, IndexError):
            raise NotXYZFormat(self.filepath)

        try:

            geometry = np.array(geometry)

            atoms = np.array(atoms)

        except ValueError:

            raise NotXYZFormat(self.filepath)

        if (len(geometry) != n_atoms) or (len(atoms) != n_atoms):

            raise NotXYZFormat(self.filepath)

        return n_atoms, geometry, atoms

    def _read_mol_file(self):
        """
        Reads number of atoms in the molecule, cartesian coordinates and present atoms from .mol file.

        Raises:
            NotV2000orV3000Format: If the input geometry is not V2000 nor V3000 .mol format.
            FileNotFound: If the file does not exist.
            NotMolFormat: If the input geometry is not in .mol format in general.

        Returns:
            tuple: n_atoms, geometry, atoms
        """
        try:
            with open(self.filepath, 'r') as f:

                geometry, atoms = [], []

                comment = [f.readline().split() for _ in range(3)]

                checkline = f.readline()

                if checkline.endswith('V2000\n'):
                    n_atoms = int(checkline.split()[0])

                    for _ in range(n_atoms):
                        line = f.readline().split()
                        geometry.append([float(xyz) for xyz in line[:3]])
                        atoms.append(line[3])

                elif checkline.endswith('V3000\n'):
                    comment = f.readline()
                    n_atoms = int(f.readline().split()[3])
                    begin_atom_line = f.readline()
                    for _ in range(n_atoms):
                        line = f.readline().split()
                        atoms.append(line[3])
                        geometry.append([float(xyz) for xyz in line[4:7]])

                else:
                    raise NotV2000orV3000Format(self.filepath)

        except OSError:
            raise FileNotFound(self.filepath)

        except (ValueError, IndexError):
            raise NotMolFormat(self.filepath)

        try:

            geometry = np.array(geometry)

            atoms = np.array(atoms)

        except ValueError:

            raise NotMolFormat(self.filepath)

        if (len(geometry) != n_atoms) or (len(atoms) != n_atoms):

            raise NotMolFormat(self.filepath)

        return n_atoms, geometry, atoms

    def _read_coord_file(self):
        """
        Reads number of atoms in the molecule, cartesian coordinates and present atoms from .coord file.

        Raises:
            NotCoordFormat: If the input geometry is not in .coord format.
            FileNotFound: If the file does not exist.

        Returns:
            tuple: n_atoms, geometry, atoms
        """
        try:
            with open(self.filepath, 'r') as f:
                lines = f.readlines()

            geometry = []
            atoms = []
            flag = False
            bohr = True

            endswith_end = False

            for line in lines:
                if line.startswith('$end'):
                    endswith_end = True
                    break

                if flag:

                    if not line.startswith('$'):

                        parts = line.split()

                        x, y, z, atom = parts

                        if not bohr:
                            xyz = [float(x), float(y), float(z)]
                        else:
                            xyz = [float(x) * 0.529177, float(y)
                                   * 0.529177, float(z) * 0.529177]

                        geometry.append(xyz)
                        atoms.append(atom.capitalize())
                    else:
                        continue

                elif line.startswith('$coord'):
                    flag = True
                    if "angs" in line:
                        bohr = False

            if len(geometry) == 0:

                raise NotCoordFormat(self.filepath)

        except OSError:
            raise NotCoordFormat(self.filepath)

        except (ValueError, IndexError):
            raise NotCoordFormat(self.filepath)

        if not endswith_end:

            raise NotCoordFormat(self.filepath)

        try:

            geometry = np.array(geometry)

            atoms = np.array(atoms)

        except ValueError:

            raise NotCoordFormat(self.filepath)

        if (len(geometry) != len(atoms)):

            raise NotCoordFormat(self.filepath)

        n_atoms = len(atoms)

        return n_atoms, geometry, atoms
    
    def _check_2D_molfile(self, coordinates: np.ndarray):

        """
        Checks if the molecule is 2D or 3D. If all x-, y- or z-coordinates are 0.0, then the molecule is 2D.

        Args:
            coordinates (np.ndarray): Coordinates of the molecule of shape (n_atoms, 3).
        Returns:
            bool: True if molecule is 2D, False if molecule is 3D.
        """

        x_coordinates = coordinates[:, 0]

        y_coordinates = coordinates[:, 1]

        z_coordinates = coordinates[:, 2]

        if np.all(x_coordinates == 0.0) or np.all(y_coordinates == 0.0) or np.all(z_coordinates == 0.0):

            return True

        else:

            return False
