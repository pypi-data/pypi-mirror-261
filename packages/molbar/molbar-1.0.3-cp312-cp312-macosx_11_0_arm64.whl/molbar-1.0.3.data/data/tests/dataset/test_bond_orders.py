import pandas as pd
import os
from molbar.barcode import get_molbars_from_coordinates
import numpy as np

def compare_bonds_to_xtb(bonds):

    sb_xtb = bonds[0]

    sb_mb = bonds[1]

    db_xtb = bonds[2]

    db_mb = bonds[3]

    tb_xtb = bonds[4]

    tb_mb = bonds[5]

    elements = bonds[6]

    ring_atoms = set(atom for ring in bonds[7] for atom in ring)

    sb_failure = 0

    n_sb = len(sb_xtb)

    mub_failure = 0

    n_mub = len(db_xtb) + len(tb_xtb)

    for sb in sb_xtb:

        if sb not in sb_mb:

            sb_failure += 1

    for db in db_xtb + tb_xtb:

        if (db not in db_mb) and (db not in tb_mb):

            elements_in_bond = [elements[atom-1] for atom in db]

            if "C" in elements_in_bond and "N" in elements_in_bond:

                carbon_index = db[elements_in_bond.index("C")]

                if carbon_index in ring_atoms:

                    continue
                   
            mub_failure += 1

    return sb_failure, n_sb, mub_failure, n_mub

#compare_bonds_to_xtb(df[["single_bonds", "single_bonds_mb", "double_bonds", "double_bonds_mb", "triple_bonds", "triple_bonds_mb", "elements", "rings"]].iloc[1681])

def get_data_from_coordinates(list_of_coordinates, list_of_elements):

    results = get_molbars_from_coordinates(list_of_coordinates=list_of_coordinates, list_of_elements=list_of_elements, threads=8, progress=True, return_data=True)

    all_single_bonds = []

    all_double_bonds = []

    all_triple_bonds = []

    all_elements = []

    all_rings = []

    for result in results:

        data = result[1]

        all_single_bonds.append(data["single_bonds"])

        all_double_bonds.append(data["double_bonds"])

        all_triple_bonds.append(data["triple_bonds"])

        all_elements.append(data["elements"])

        all_rings.append(data["cycles"])

    return all_single_bonds, all_double_bonds, all_triple_bonds, all_elements, all_rings


def add_data_to_df(list_of_coordinates, list_of_elements, permutation_keys=[]):

    if len(permutation_keys) != len(list_of_elements): 

        permutation_keys = [list(range(len(elements))) for elements in list_of_elements]

    results = get_molbars_from_coordinates(list_of_coordinates=list_of_coordinates, list_of_elements=list_of_elements, threads=8, progress=True, return_data=True)

    all_single_bonds = []

    all_double_bonds = []

    all_triple_bonds = []

    all_rings = []

    for idx in range(len(results)):

        result = results[idx]

        perm_key = list(np.array(permutation_keys[idx]))

        data = result[1]

        single_bonds = data["single_bonds"]

        double_bonds = data["double_bonds"]

        triple_bonds = data["triple_bonds"]

        sorted_single_bonds = sorted([sorted([perm_key[bond[0]-1]+1,perm_key[bond[1]-1]+1]) for bond in single_bonds], key=lambda x: (x[0], x[1]))

        sorted_double_bonds = sorted([sorted([perm_key[bond[0]-1]+1,perm_key[bond[1]-1]+1]) for bond in double_bonds], key=lambda x: (x[0], x[1]))

        sorted_triple_bonds = sorted([sorted([perm_key[bond[0]-1]+1,perm_key[bond[1]-1]+1]) for bond in triple_bonds], key=lambda x: (x[0], x[1]))

        all_single_bonds.append(sorted_single_bonds)

        all_double_bonds.append(sorted_double_bonds)

        all_triple_bonds.append(sorted_triple_bonds)

        all_rings.append(data["cycles"])

    
    return all_single_bonds, all_double_bonds, all_triple_bonds, all_rings


def compare_columns(column1, column2):

    fail = 0

    for element in column1:

        if element not in column2:

            fail +=1

    return fail


def test_bond_orders():

    script_path = os.path.dirname(os.path.abspath(__file__))

    filepath = os.path.join(script_path, f"organic_dataset.pkl")

    df = pd.read_pickle(filepath)

    all_single_bonds, all_double_bonds, all_triple_bonds, all_rings = add_data_to_df(df["coordinates"].values, df["elements"].values)

    df["single_bonds_mb"] = all_single_bonds
    df["double_bonds_mb"] = all_double_bonds
    df["triple_bonds_mb"] = all_triple_bonds
    df["rings"] = all_rings

    all_single_bonds, all_double_bonds, all_triple_bonds, all_rings = add_data_to_df(df["coordinates_permutated"].values, df["elements_permutated"].values, permutation_keys=df["permutation_key"].values)

    df["single_bonds_mb_perm"] = all_single_bonds
    df["double_bonds_mb_perm"] = all_double_bonds
    df["triple_bonds_mb_perm"] = all_triple_bonds
    df["rings_perm"] = all_rings


    df[["sb_failure", "n_sb_xtb", "mub_failure", "n_mub_xtb"]] = df[["single_bonds", "single_bonds_mb", "double_bonds", "double_bonds_mb", "triple_bonds", "triple_bonds_mb", "elements", "rings"]].apply(lambda x: compare_bonds_to_xtb(x), axis=1, result_type='expand')

    df["sb_permutation_failure"] =  df[["single_bonds_mb", "single_bonds_mb_perm"]].apply(lambda x: compare_columns(x[0], x[1]), axis=1)
    df["db_permutation_failure"] =  df[["double_bonds_mb", "double_bonds_mb_perm"]].apply(lambda x: compare_columns(x[0], x[1]), axis=1)
    df["tb_permutation_failure"] =  df[["triple_bonds_mb", "triple_bonds_mb_perm"]].apply(lambda x: compare_columns(x[0], x[1]), axis=1)

    df["n_sb_mb"] = df["single_bonds_mb"].apply(lambda x: len(x))
    df["n_db_mb"] = df["double_bonds_mb"].apply(lambda x: len(x))
    df["n_tb_mb"] = df["triple_bonds_mb"].apply(lambda x: len(x))

    n_sb_mb_total = df["n_sb_mb"].sum()
    n_db_mb_total = df["n_db_mb"].sum()
    n_tb_mb_total = df["n_tb_mb"].sum()

    n_sb_mb_fail = df["sb_permutation_failure"].sum()
    n_db_mb_fail = df["db_permutation_failure"].sum()
    n_tb_mb_fail = df["tb_permutation_failure"].sum()

    n_sb_xtb_total = df["n_sb_xtb"].sum()
    n_mub_xtb_total = df["n_mub_xtb"].sum()

    n_sb_xtb_fail = df["sb_failure"].sum()
    n_mub_xtb_fail = df["mub_failure"].sum()

    if n_sb_xtb_total > 0:

        print(n_sb_xtb_fail/n_sb_xtb_total*100)

        assert n_sb_xtb_fail/n_sb_xtb_total*100 < 3., "Discrepancy between WBO from GFN2-xTB and MolBar bond orders for single bonds."

    if n_mub_xtb_total > 0:

        print(n_mub_xtb_fail/n_mub_xtb_total*100 )

        assert n_mub_xtb_fail/n_mub_xtb_total*100 < 4.1, "Discrepancy between WBO from GFN2-xTB and MolBar bond orders for multiple bonds."

    #if n_tb_xtb_total > 0:
        
    #    print(n_tb_xtb_fail/n_tb_xtb_total*100)

    #    assert n_tb_xtb_fail/n_tb_xtb_total*100 < 0.5, "Discrepancy between WBO from GFN2-xTB and MolBar bond orders for triple bonds."

    if n_sb_mb_total > 0:

        assert n_sb_mb_fail/n_sb_mb_total*100 < 0.5, "Permutation variance detected for single bonds."

    if n_db_mb_total > 0:

        assert n_db_mb_fail/n_db_mb_total*100 < 0.5, "Permutation variance detected for double bonds."

    if n_tb_mb_total > 0:

        assert n_tb_mb_fail/n_tb_mb_total*100 < 0.5, "Permutation variance detected for triple bonds."

    

if __name__ == "__main__":

    test_bond_orders()