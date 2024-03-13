from molbar.io.filereader import FileReader
import os
import pandas as pd
from tqdm import tqdm
import random

if __name__ == "__main__":

    defaultdir = os.getcwd()

    files = [os.path.join("./conformer_independence/ru_cat", file) for file in os.listdir("./conformer_independence/ru_cat") if file.endswith(".xyz")]

    files_without_path = [file for file in os.listdir(".") if file.endswith(".xyz")]

    df = pd.DataFrame(files_without_path, columns=["file"])

    list_of_coordinates = []

    list_of_elements = []

    permutation_keys = []

    for file in tqdm(files):
        
        path = file.replace(".xyz", "")

        n_atoms, coordinates, elements = FileReader().read_file(file)

        permutation_key = list(range(n_atoms))
        
        random.shuffle(permutation_key)

        permutation_keys.append(permutation_key)

        list_of_coordinates.append(coordinates)
    
        list_of_elements.append(elements)

    df["coordinates"] = list_of_coordinates

    df["elements"] = list_of_elements

    #df["permutation_key"] = permutation_keys

    #df["coordinates_permutated"] = df[["coordinates", "permutation_key"]].apply(lambda x: x[0][x[1]], axis=1)

    #df["elements_permutated"] = df[["elements", "permutation_key"]].apply(lambda x: x[0][x[1]], axis=1)

    df.to_pickle('conformer_independence_inorganic.pkl')


