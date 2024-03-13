import pandas as pd
import os
from molbar.barcode import get_molbars_from_coordinates

def test_ru_cat():

    script_path = os.path.dirname(os.path.abspath(__file__))

    filepath = os.path.join(script_path, f"conformer_independence_inorganic.pkl")

    df = pd.read_pickle(filepath)

    barcodes = get_molbars_from_coordinates(list_of_coordinates=df["coordinates"].values, list_of_elements=df["elements"].values, threads=8, progress=True)

    df["MolBar"] = barcodes

    df_unique = df.drop_duplicates("MolBar")

    assert len(df_unique) == 3, "Insufficient unification of metal complexes."


if __name__ == "__main__":

    test_ru_cat()