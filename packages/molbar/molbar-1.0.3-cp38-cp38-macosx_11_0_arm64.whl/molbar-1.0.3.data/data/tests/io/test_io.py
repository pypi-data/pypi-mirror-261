import os
import shutil
import numpy as np
from io import StringIO
from contextlib import redirect_stderr
from molbar.barcode import get_molbar_from_file, get_molbars_from_files, idealize_structure_from_file, get_molbar_from_coordinates, get_molbars_from_coordinates
from molbar.io.filereader import FileReader
from molbar.helper.input import _get_constraints, _transform_constraints

def test_idealize_structure_from_file():

    script_path = os.path.dirname(os.path.abspath(__file__))

    filepath = os.path.join(script_path, "../../example/binol_m.xyz")

    input_constraint = os.path.join(script_path, "../../example/binol_m.yml")

    debugpath = os.path.join(script_path, "../../example/data_molbar_binol_m_xyz")

    for return_data in [True, False]:

        for timing in [True, False]:

            for input_constraint in [None, input_constraint]:

                for write_trj in [True, False]:

                    with StringIO() as stderr_buffer, redirect_stderr(stderr_buffer):

                        result = idealize_structure_from_file(filepath, return_data=return_data, timing=timing, input_constraint=input_constraint, write_trj=write_trj)

                        stderr_output = stderr_buffer.getvalue()

                    if return_data == True:

                        assert isinstance(result[4], dict)

                        dihedral_constraints = result[4]["fragment_data"][1]["dihedrals"]

                        values = np.round([constraint["value"] for constraint in dihedral_constraints],2)
                    
                        if input_constraint:

                            assert 1.57 in values

                        else:

                            assert 1.57 not in values

                    if timing == True:

                        assert stderr_output.startswith("Duration")

                    if write_trj == True:

                        assert os.path.exists(debugpath)

                        try:
                            # Remove the directory and its contents
                            shutil.rmtree(debugpath)
                    
                        except OSError as e:

                            print(f"Error: {e}")


def test_get_molbar_from_file():

    script_path = os.path.dirname(os.path.abspath(__file__))

    filepath = os.path.join(script_path, "../../example/binol_m.xyz")

    input_constraint = os.path.join(script_path, "../../example/binol_m.yml")

    debugpath = os.path.join(script_path, "../../example/data_molbar_binol_m_xyz")

    for debug in [True, False]:

        for timing in [True, False]:

            for input_constraint in [None, input_constraint]:

                for mode in ["mb", "topo"]:

                    for write_trj in [True, False]:

                        with StringIO() as stderr_buffer, redirect_stderr(stderr_buffer):

                            result = get_molbar_from_file(filepath, return_data=debug, timing=timing, input_constraint=input_constraint, mode=mode, write_trj=write_trj)

                            stderr_output = stderr_buffer.getvalue()

                        if debug == True:

                            assert isinstance(result[1], dict)

                            if mode == "mb":

                                assert result[0].startswith("MolBar")

                                if input_constraint:

                                    assert " -14 0 4 " == result[0].split("|")[-1]

                                else:

                                    assert " 0 0 0 0 " == result[0].split("|")[-1]

                            elif mode == "topo":

                                assert result[0].startswith("TopoBar")

                        elif debug == False:

                            if mode == "mb":

                                assert result.startswith("MolBar")

                            elif mode == "topo":

                                assert result.startswith("TopoBar") 

                        if timing == True:

                            assert stderr_output.startswith("Duration")

                        if write_trj == True and mode == "mb":

                            assert os.path.exists(debugpath)

                            try:
                                # Remove the directory and its contents
                                shutil.rmtree(debugpath)
                        
                            except OSError as e:

                                print(f"Error: {e}")

def test_get_molbars_from_files():

    script_path = os.path.dirname(os.path.abspath(__file__))

    filepaths = [os.path.join(script_path, "../../example/binol_m.xyz"), os.path.join(script_path, "../../example/binol_p.xyz")]

    input_constraints = [os.path.join(script_path, "../../example/binol_m.yml"), os.path.join(script_path, "../../example/binol_p.yml")]

    debugpaths = [os.path.join(script_path, "../../example/data_molbar_binol_m_xyz"), os.path.join(script_path, "../../example/data_molbar_binol_p_xyz")]

    for debug in [True, False]:

        for input in [None, input_constraints]:

            for mode in ["mb", "topo"]:

                for write_trj in [True, False]:

                    result = get_molbars_from_files(filepaths, threads=2, return_data=debug, input_constraints=input, mode=mode, write_trj=write_trj)

                    if debug == True:

                        assert isinstance(result[0][1], dict)

                        if mode == "mb":

                            assert result[0][0].startswith("MolBar")

                            if input:

                                assert " -14 0 4 " == result[0][0].split("|")[-1]
                                assert " -4 0 14 " == result[1][0].split("|")[-1]

                            else:

                                assert " 0 0 0 0 " == result[0][0].split("|")[-1]
                                assert " 0 0 0 0 " == result[1][0].split("|")[-1]

                        elif mode == "topo":

                            assert result[0][0].startswith("TopoBar")

                    elif debug == False:

                        if mode == "mb":

                            assert result[0].startswith("MolBar")

                        elif mode == "topo":

                            assert result[1].startswith("TopoBar") 

                    if write_trj == True and mode == "mb":

                        assert os.path.exists(debugpaths[0])
                        assert os.path.exists(debugpaths[1])

                        try:
                            # Remove the directory and its contents
                            shutil.rmtree(debugpaths[0])
                            shutil.rmtree(debugpaths[1])
                    
                        except OSError as e:

                            print(f"Error: {e}")

def test_get_molbar_from_coordinates():

    script_path = os.path.dirname(os.path.abspath(__file__))

    filepath = os.path.join(script_path, "../../example/binol_m.xyz")

    constraint_path = os.path.join(script_path, "../../example/binol_m.yml")

    n_atoms, coordinates, elements = FileReader(filepath).read_file()

    input_constraint = _get_constraints(constraint_path)

    input_constraint = _transform_constraints(filepath, input_constraint)
    
    for debug in [True, False]:

        for timing in [True, False]:

            for input_constraint in [None, input_constraint]:

                for mode in ["mb", "topo"]:

                    with StringIO() as stderr_buffer, redirect_stderr(stderr_buffer):

                        result = get_molbar_from_coordinates(coordinates=coordinates, elements=elements, return_data=debug, timing=timing, input_constraint=input_constraint, mode=mode)

                        stderr_output = stderr_buffer.getvalue()

                    if debug == True:

                        assert isinstance(result[1], dict)

                        if mode == "mb":

                            assert result[0].startswith("MolBar")

                            if input_constraint:

                                assert " -14 0 4 " == result[0].split("|")[-1]

                            else:

                                assert " 0 0 0 0 " == result[0].split("|")[-1]

                        elif mode == "topo":

                            assert result[0].startswith("TopoBar")

                    elif debug == False:

                        if mode == "mb":

                            assert result.startswith("MolBar")

                        elif mode == "topo":

                            assert result.startswith("TopoBar") 

                    if timing == True:

                        assert stderr_output.startswith("Duration")

def test_get_molbars_from_coordinates():

    script_path = os.path.dirname(os.path.abspath(__file__))

    filepath_m = os.path.join(script_path, "../../example/binol_m.xyz")

    filepath_p = os.path.join(script_path, "../../example/binol_p.xyz")

    constraint_path_m = os.path.join(script_path, "../../example/binol_m.yml")

    constraint_path_p = os.path.join(script_path, "../../example/binol_p.yml")

    n_atoms, coordinates_m, elements = FileReader(filepath_m).read_file()

    n_atoms, coordinates_p, elements = FileReader(filepath_p).read_file()

    elements = [elements, elements]

    coordinates = [coordinates_m, coordinates_p]

    input_constraints = []

    for constraint_path in [constraint_path_m, constraint_path_p]:

        input = _get_constraints(constraint_path)

        input = _transform_constraints("", input)

        input_constraints.append(input)

    for debug in [True, False]:

        for input in [None, input_constraints]:

            for mode in ["mb", "topo"]:
                
                result = get_molbars_from_coordinates(list_of_coordinates=coordinates, list_of_elements=elements, threads=2, return_data=debug, input_constraints=input, mode=mode)

                if debug == True:

                    assert isinstance(result[0][1], dict)

                    if mode == "mb":

                        assert result[0][0].startswith("MolBar")

                        if input:

                            assert " -14 0 4 " == result[0][0].split("|")[-1]
                            assert " -4 0 14 " == result[1][0].split("|")[-1]

                        else:

                            assert " 0 0 0 0 " == result[0][0].split("|")[-1]
                            assert " 0 0 0 0 " == result[1][0].split("|")[-1]

                    elif mode == "topo":

                        assert result[0][0].startswith("TopoBar")

                elif debug == False:

                    if mode == "mb":

                        assert result[0].startswith("MolBar")

                    elif mode == "topo":

                        assert result[1].startswith("TopoBar") 

if __name__ == "__main__":

    test_idealize_structure_from_file()

    test_get_molbar_from_file()

    test_get_molbars_from_files()

    test_get_molbar_from_coordinates()

    test_get_molbars_from_coordinates()
