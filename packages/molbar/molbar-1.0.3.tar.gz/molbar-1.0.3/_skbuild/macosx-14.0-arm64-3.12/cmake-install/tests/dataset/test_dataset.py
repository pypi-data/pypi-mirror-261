import pandas as pd
import os
from molbar.barcode import get_molbars_from_coordinates

def clean_up(files, barcodes) -> None:

    data = [[os.path.splitext(os.path.basename(file))[0], barcode] for file, barcode in zip(files, barcodes)]

    df_molbar = pd.DataFrame(data, columns=["file", "MolBar"])

    df_unique = df_molbar.drop_duplicates("MolBar")

    return df_molbar, len(df_unique)


def analyze_dataset(dataset, refval_dup, refval_perm):

    script_path = os.path.dirname(os.path.abspath(__file__))

    filepath = os.path.join(script_path, f"./{dataset}_dataset.pkl")

    df = pd.read_pickle(filepath)

    barcodes0 = get_molbars_from_coordinates(list_of_coordinates=df["coordinates"].values, list_of_elements=df["elements"].values, threads=8, progress=True) 

    n_files = len(df["coordinates"].values)

    barcodes1 = get_molbars_from_coordinates(list_of_coordinates=df["coordinates_permutated"].values, list_of_elements=df["elements_permutated"].values, threads=8, progress=True)  

    df_molbar0, n_unique_0 = clean_up(barcodes0, barcodes0)

    df_molbar1, n_unique_1 = clean_up(barcodes1, barcodes1)

    df = df_molbar0.merge(df_molbar1, on="file")

    df["failure"] = False

    df.loc[df["MolBar_x"] != df["MolBar_y"], "same"] = True

    n_duplicates0 = n_files - n_unique_0

    n_duplicates1 = n_files - n_unique_1

    n_failures = df["failure"].sum()

    rel_n_failures = round(n_failures/n_files*100, 2)

    print(f"Number of duplicates in first {dataset} dataset:", n_duplicates0)
    print(f"Number of duplicates in second {dataset} dataset:", n_duplicates1)
    print(f"Relative number of permutation failures in the organic dataset: {rel_n_failures} %")

    lower_threshold = refval_dup-0.05*refval_dup

    upper_threshold = refval_dup+0.05*refval_dup

    assert rel_n_failures <= refval_perm, f"Worse permutation invariance perfomance detected for the {dataset} datatset."
    assert n_duplicates0 >= lower_threshold, f"Less duplicates than expected for the {dataset} datatset."
    assert n_duplicates0 <= upper_threshold, f"More duplicates than expected for the {dataset} datatset."


def test_organic_dataset():

    analyze_dataset("organic", 360, 0.1)

def test_inorganic_dataset():

    analyze_dataset("inorganic", 2, 0.1)

if __name__ == "__main__":

    analyze_dataset("organic", 383, 0.1)

    
    

