import os

##########################
# LIBRARY Method         #
##########################

def test_cxx_cxx_lib():
    cmd_return = os.system( 
        "./$(find ../build/driver_lib_cxx*) -mdi \"-role DRIVER -name driver -method LIBRARY -out output\" " )
    assert cmd_return == 0

    # read the output file
    output_file = open("output", "r")
    output = output_file.read()

    assert output == " Engine name: MM\n"

def test_py_py_lib():
    cmd_return = os.system( 
        "python ../build/lib_py.py -mdi \"-role DRIVER -name driver -method LIBRARY -out output\" " )
    assert cmd_return == 0

    # read the output file
    output_file = open("output", "r")
    output = output_file.read()

    expected = '''Start of driver
Setting generic command
SUCCESS
NATOMS: 123
'''

    assert output == expected



##########################
# MPI Method             #
##########################

def test_cxx_cxx_mpi():
    command = '''mpiexec -n 1 ./$(find ../build/driver_cxx*) -mdi \"-role DRIVER -name driver -method MPI -out output\" : \\
    -n 1 ./$(find ../build/engine_cxx*) -mdi \"-role ENGINE -name MM -method MPI\"'''

    cmd_return = os.system( command )
    #assert cmd_return == 0

    # read the output file
    output_file = open("output", "r")
    output = output_file.read()

    assert output == " Engine name: MM\n"

def test_cxx_f90_mpi():
    command = '''mpiexec -n 1 ./$(find ../build/driver_cxx*) -mdi \"-role DRIVER -name driver -method MPI -out output\" : \\
    -n 1 ./$(find ../build/engine_f90*) -mdi \"-role ENGINE -name MM -method MPI\"'''

    cmd_return = os.system( command )
    #assert cmd_return == 0

    # read the output file
    output_file = open("output", "r")
    output = output_file.read()

    assert output == " Engine name: MM\n"

def test_cxx_py_mpi():
    command = '''mpiexec -n 1 ./$(find ../build/driver_cxx*) -mdi \"-role DRIVER -name driver -method MPI -out output\" : \\
    -n 1 python ../build/engine_py.py -mdi \"-role ENGINE -name MM -method MPI\"'''

    cmd_return = os.system( command )
    #assert cmd_return == 0

    # read the output file
    output_file = open("output", "r")
    output = output_file.read()

    assert output == " Engine name: MM\n"

def test_f90_cxx_mpi():
    command = '''mpiexec -n 1 ./$(find ../build/driver_f90*) -mdi \"-role DRIVER -name driver -method MPI -out output\" : \\
    -n 1 ./$(find ../build/engine_cxx*) -mdi \"-role ENGINE -name MM -method MPI\"'''

    cmd_return = os.system( command )
    #assert cmd_return == 0

    # read the output file
    output_file = open("output", "r")
    output = output_file.read()

    assert output == " Engine name: MM\n"

def test_f90_f90_mpi():
    command = '''mpiexec -n 1 ./$(find ../build/driver_f90*) -mdi \"-role DRIVER -name driver -method MPI -out output\" : \\
    -n 1 ./$(find ../build/engine_f90*) -mdi \"-role ENGINE -name MM -method MPI\"'''

    cmd_return = os.system( command )
    #assert cmd_return == 0

    # read the output file
    output_file = open("output", "r")
    output = output_file.read()

    assert output == " Engine name: MM\n"

def test_f90_py_mpi():
    command = '''mpiexec -n 1 ./$(find ../build/driver_f90*) -mdi \"-role DRIVER -name driver -method MPI -out output\" : \\
    -n 1 python ../build/engine_py.py -mdi \"-role ENGINE -name MM -method MPI\"'''

    cmd_return = os.system( command )
    #assert cmd_return == 0

    # read the output file
    output_file = open("output", "r")
    output = output_file.read()

    assert output == " Engine name: MM\n"

def test_py_cxx_mpi():
    command = '''mpiexec -n 1 python ../build/driver_py.py -mdi \"-role DRIVER -name driver -method MPI -out output\" : \\
    -n 1 ./$(find ../build/engine_cxx*) -mdi \"-role ENGINE -name MM -method MPI\"'''

    cmd_return = os.system( command )
    #assert cmd_return == 0

    # read the output file
    output_file = open("output", "r")
    output = output_file.read()

    assert output == " Engine name: MM\n"

def test_py_f90_mpi():
    command = '''mpiexec -n 1 python ../build/driver_py.py -mdi \"-role DRIVER -name driver -method MPI -out output\" : \\
    -n 1 ./$(find ../build/engine_f90*) -mdi \"-role ENGINE -name MM -method MPI\"'''

    cmd_return = os.system( command )
    #assert cmd_return == 0

    # read the output file
    output_file = open("output", "r")
    output = output_file.read()

    assert output == " Engine name: MM\n"

def test_py_py_mpi():
    command = '''mpiexec -n 1 python ../build/driver_py.py -mdi \"-role DRIVER -name driver -method MPI -out output\" : \\
    -n 1 python ../build/engine_py.py -mdi \"-role ENGINE -name MM -method MPI\"'''

    cmd_return = os.system( command )
    #assert cmd_return == 0

    # read the output file
    output_file = open("output", "r")
    output = output_file.read()

    assert output == " Engine name: MM\n"



##########################
# TCP Method             #
##########################

def test_cxx_cxx_tcp():
    command = '''./$(find ../build/driver_cxx*) -mdi \"-role DRIVER -name driver -method TCP -port 8021 -out output\" &
./$(find ../build/engine_cxx*) -mdi \"-role ENGINE -name MM -method TCP -port 8021 -hostname localhost\" &
wait'''

    cmd_return = os.system( command )
    assert cmd_return == 0

    # read the output file
    output_file = open("output", "r")
    output = output_file.read()

    assert output == " Engine name: MM\n"

def test_cxx_f90_tcp():
    command = '''./$(find ../build/driver_cxx*) -mdi \"-role DRIVER -name driver -method TCP -port 8021 -out output\" &
./$(find ../build/engine_f90*) -mdi \"-role ENGINE -name MM -method TCP -port 8021 -hostname localhost\" &
wait'''

    cmd_return = os.system( command )
    assert cmd_return == 0

    # read the output file
    output_file = open("output", "r")
    output = output_file.read()

    assert output == " Engine name: MM\n"

def test_cxx_py_tcp():
    command = '''./$(find ../build/driver_cxx*) -mdi \"-role DRIVER -name driver -method TCP -port 8021 -out output\" &
python ../build/engine_py.py -mdi \"-role ENGINE -name MM -method TCP -port 8021 -hostname localhost\" &
wait'''

    cmd_return = os.system( command )
    assert cmd_return == 0

    # read the output file
    output_file = open("output", "r")
    output = output_file.read()

    assert output == " Engine name: MM\n"

def test_f90_cxx_tcp():
    command = '''./$(find ../build/driver_f90*) -mdi \"-role DRIVER -name driver -method TCP -port 8021 -out output\" &
./$(find ../build/engine_cxx*) -mdi \"-role ENGINE -name MM -method TCP -port 8021 -hostname localhost\" &
wait'''

    cmd_return = os.system( command )
    assert cmd_return == 0

    # read the output file
    output_file = open("output", "r")
    output = output_file.read()

    assert output == " Engine name: MM\n"

def test_f90_f90_tcp():
    command = '''./$(find ../build/driver_f90*) -mdi \"-role DRIVER -name driver -method TCP -port 8021 -out output\" &
./$(find ../build/engine_f90*) -mdi \"-role ENGINE -name MM -method TCP -port 8021 -hostname localhost\" &
wait'''

    cmd_return = os.system( command )
    assert cmd_return == 0

    # read the output file
    output_file = open("output", "r")
    output = output_file.read()

    assert output == " Engine name: MM\n"

def test_f90_py_tcp():
    command = '''./$(find ../build/driver_f90*) -mdi \"-role DRIVER -name driver -method TCP -port 8021 -out output\" &
python ../build/engine_py.py -mdi \"-role ENGINE -name MM -method TCP -port 8021 -hostname localhost\" &
wait'''

    cmd_return = os.system( command )
    assert cmd_return == 0

    # read the output file
    output_file = open("output", "r")
    output = output_file.read()

    assert output == " Engine name: MM\n"

def test_py_cxx_tcp():
    command = '''python ../build/driver_py.py -mdi \"-role DRIVER -name driver -method TCP -port 8021 -out output\" &
./$(find ../build/engine_cxx*) -mdi \"-role ENGINE -name MM -method TCP -port 8021 -hostname localhost\" &
wait'''

    cmd_return = os.system( command )
    assert cmd_return == 0

    # read the output file
    output_file = open("output", "r")
    output = output_file.read()

    assert output == " Engine name: MM\n"

def test_py_f90_tcp():
    command = '''python ../build/driver_py.py -mdi \"-role DRIVER -name driver -method TCP -port 8021 -out output\" &
./$(find ../build/engine_f90*) -mdi \"-role ENGINE -name MM -method TCP -port 8021 -hostname localhost\" &
wait'''

    cmd_return = os.system( command )
    assert cmd_return == 0

    # read the output file
    output_file = open("output", "r")
    output = output_file.read()

    assert output == " Engine name: MM\n"

def test_py_py_tcp():
    command = '''python ../build/driver_py.py -mdi \"-role DRIVER -name driver -method TCP -port 8021 -out output\" &
python ../build/engine_py.py -mdi \"-role ENGINE -name MM -method TCP -port 8021 -hostname localhost\" &
wait'''

    cmd_return = os.system( command )
    assert cmd_return == 0

    # read the output file
    output_file = open("output", "r")
    output = output_file.read()

    assert output == " Engine name: MM\n"
