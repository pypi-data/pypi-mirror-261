import os 
import shutil
import subprocess
from tqdm import tqdm
import pandas as pd

def generate_wbo(file, path):
    try:
    # Try to create the directory
        os.mkdir(path)
    except FileExistsError:
        # If the directory already exists, remove it and create a new one
        shutil.rmtree(path)
        os.mkdir(path)

    shutil.copy2(file, os.path.join(path, "coord.xyz"))

    os.chdir(path)

    command = "xtb coord.xyz --wbo > xtb.out"

    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")

    os.chdir(defaultdir)


def read_bond_file(file_path):
    bonds = []
    bond_orders = []

    single_bonds = []
    double_bonds = []
    triple_bonds = []

    with open(file_path, 'r') as file:
        for line in file:
            # Split the line into three integers

            idx1, idx2, wbo = line.strip().split()
        
            #atomic_index1, atomic_index2, bond_order = 

            # Append the bond tuple and bond order to their respective lists
            bonds.append((int(idx1), int(idx2)))
            bond_orders.append(float(wbo))

    for i, wbo in enumerate(bond_orders):

        if wbo >= 0.5 and wbo < 1.2:

            single_bonds.append(sorted(bonds[i]))

        elif wbo >= 1.2 and wbo < 2.5:

            double_bonds.append(sorted(bonds[i]))
        
        elif wbo >= 2.5 and wbo < 3.5:

            triple_bonds.append(sorted(bonds[i]))

        else:

            pass
    
    sorted_single_bonds = sorted(single_bonds, key=lambda x: (x[0], x[1]))

    sorted_double_bonds = sorted(double_bonds, key=lambda x: (x[0], x[1]))

    sorted_triple_bonds = sorted(triple_bonds, key=lambda x: (x[0], x[1]))

    return sorted_single_bonds, sorted_double_bonds, sorted_triple_bonds


if __name__ == "__main__":

    from molbar.io.filereader import FileReader

    import random

    defaultdir = os.getcwd()

    files = [os.path.join(defaultdir, file) for file in os.listdir(".") if file.endswith(".xyz")]

    files_without_path = [file for file in os.listdir(".") if file.endswith(".xyz")]

    df = pd.DataFrame(files_without_path, columns=["file"])

    all_single_bonds = []

    all_double_bonds = []

    all_triple_bonds = []

    list_of_coordinates = []

    list_of_elements = []

    permutation_keys = []

    for file in tqdm(files):
        
        path = file.replace(".xyz", "")

        n_atoms, coordinates, elements = FileReader().read_file(file)

        permutation_key =list(range(n_atoms))
        
        random.shuffle(permutation_key)

        permutation_keys.append(permutation_key)

        list_of_coordinates.append(coordinates)
    
        list_of_elements.append(elements)

        generate_wbo(file, path)

        single_bonds, double_bonds, triple_bonds = read_bond_file(os.path.join(path, "wbo"))

        all_single_bonds.append(single_bonds)

        all_double_bonds.append(double_bonds)

        all_triple_bonds.append(triple_bonds)
    
    df["coordinates"] = list_of_coordinates

    df["elements"] = list_of_elements

    df["single_bonds"] = all_single_bonds

    df["double_bonds"] = all_double_bonds

    df["triple_bonds"] = all_triple_bonds

    df["permutation_key"] = permutation_keys

    df.to_pickle('organic_dataset.pkl')







