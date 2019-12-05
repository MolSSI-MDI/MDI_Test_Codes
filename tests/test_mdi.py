import os
import sys
import glob
import subprocess

build_dir = "../build"

sys.path.append(build_dir) 

# Includes flags to prevent warning messages
mpiexec_general = "mpiexec "
mpiexec_mca = "mpiexec --mca btl_base_warn_component_unused 0 "

def format_return(input_string):
    my_string = input_string.decode('utf-8')

    # remove any \r special characters, which sometimes are added on Windows
    my_string = my_string.replace('\r','')

    return my_string

##########################
# LIBRARY Method         #
##########################

def test_cxx_cxx_lib():
    # get the name of the driver code, which includes a .exe extension on Windows
    driver_name = glob.glob("../build/driver_lib_cxx*")[0]

    try:
        # run the calculation
        driver_proc = subprocess.Popen([driver_name, "-mdi", "-role DRIVER -name driver -method LIBRARY"],
                                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        driver_tup = driver_proc.communicate()

        # convert the driver's output into a string
        driver_out = format_return(driver_tup[0])
        driver_err = format_return(driver_tup[1])

        assert driver_err == ""
        assert driver_out == " Engine name: MM\n"

    except AssertionError: # MCA case
        # run the calculation
        driver_proc = subprocess.Popen(["mpiexec","--mca btl_base_warn_component_unused","0","-n","1",driver_name, "-mdi", "-role DRIVER -name driver -method LIBRARY"],
                                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        driver_tup = driver_proc.communicate()

        # convert the driver's output into a string
        driver_out = format_return(driver_tup[0])
        driver_err = format_return(driver_tup[1])

        assert driver_err == ""
        assert driver_out == " Engine name: MM\n"

def test_py_py_lib():
    # run the calculation
    driver_proc = subprocess.Popen([sys.executable, "../build/lib_py.py", "-mdi", "-role DRIVER -name driver -method LIBRARY"],
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    driver_tup = driver_proc.communicate()

    # convert the driver's output into a string
    driver_out = format_return(driver_tup[0])
    driver_err = format_return(driver_tup[1])

    expected = '''Start of driver
Setting generic command
SUCCESS
NATOMS: 123
'''

    assert driver_err == ""
    assert driver_out == expected



##########################
# MPI Method             #
##########################

def test_cxx_cxx_mpi():
    command_suffix = '''-n 1 ./$(find ../build/driver_cxx*) -mdi \"-role DRIVER -name driver -method MPI -out output\" : \\
    -n 1 ./$(find ../build/engine_cxx*) -mdi \"-role ENGINE -name MM -method MPI\"'''

    command = "cd " + build_dir + "\n" + mpiexec_general + command_suffix
    cmd_return = os.system( command )
    assert cmd_return == 0
    #try:
    #    command = "cd " + build_dir + "\n" + mpiexec_general + command_suffix
    #    cmd_return = os.system( command )
    #    assert cmd_return == 0
    #except AssertionError: # MCA
    #    command = "cd " + build_dir + "\n" + mpiexec_mca + command_suffix
    #    cmd_return = os.system( command )
    #    assert cmd_return == 1

    # read the output file
    output_file = open(build_dir + "/output", "r")
    output = output_file.read()

    assert output == " Engine name: MM\n"

def test_cxx_f90_mpi():
    command_suffix = '''-n 1 ./$(find ../build/driver_cxx*) -mdi \"-role DRIVER -name driver -method MPI -out output\" : \\
    -n 1 ./$(find ../build/engine_f90*) -mdi \"-role ENGINE -name MM -method MPI\"'''

    try:
        command = "cd " + build_dir + "\n" + mpiexec_general + command_suffix
        cmd_return = os.system( command )
        assert cmd_return == 0
    except AssertionError: # MCA
        command = "cd " + build_dir + "\n" + mpiexec_mca + command_suffix
        cmd_return = os.system( command )
        assert cmd_return == 1

    # read the output file
    output_file = open(build_dir + "/output", "r")
    output = output_file.read()

    assert output == " Engine name: MM\n"

def test_cxx_py_mpi():
    command_suffix = '''-n 1 ./$(find ../build/driver_cxx*) -mdi \"-role DRIVER -name driver -method MPI -out output\" : \\
    -n 1 python ../build/engine_py.py -mdi \"-role ENGINE -name MM -method MPI\"'''

    try:
        command = "cd " + build_dir + "\n" + mpiexec_general + command_suffix
        cmd_return = os.system( command )
        assert cmd_return == 0
    except AssertionError: # MCA
        command = "cd " + build_dir + "\n" + mpiexec_mca + command_suffix
        cmd_return = os.system( command )
        assert cmd_return == 1

    # read the output file
    output_file = open(build_dir + "/output", "r")
    output = output_file.read()

    assert output == " Engine name: MM\n"

def test_f90_cxx_mpi():
    command_suffix = '''-n 1 ./$(find ../build/driver_f90*) -mdi \"-role DRIVER -name driver -method MPI -out output\" : \\
    -n 1 ./$(find ../build/engine_cxx*) -mdi \"-role ENGINE -name MM -method MPI\"''' 

    try:
        command = "cd " + build_dir + "\n" + mpiexec_general + command_suffix
        cmd_return = os.system( command )
        assert cmd_return == 0
    except AssertionError: # MCA
        command = "cd " + build_dir + "\n" + mpiexec_mca + command_suffix
        cmd_return = os.system( command )
        assert cmd_return == 1

    # read the output file
    output_file = open(build_dir + "/output", "r")
    output = output_file.read()

    assert output == " Engine name: MM\n"

def test_f90_f90_mpi():
    command_suffix = '''-n 1 ./$(find ../build/driver_f90*) -mdi \"-role DRIVER -name driver -method MPI -out output\" : \\
    -n 1 ./$(find ../build/engine_f90*) -mdi \"-role ENGINE -name MM -method MPI\"'''

    try:
        command = "cd " + build_dir + "\n" + mpiexec_general + command_suffix
        cmd_return = os.system( command )
        assert cmd_return == 0
    except AssertionError: # MCA
        command = "cd " + build_dir + "\n" + mpiexec_mca + command_suffix
        cmd_return = os.system( command )
        assert cmd_return == 1

    # read the output file
    output_file = open(build_dir + "/output", "r")
    output = output_file.read()

    assert output == " Engine name: MM\n"

def test_f90_py_mpi():
    command_suffix = '''-n 1 ./$(find ../build/driver_f90*) -mdi \"-role DRIVER -name driver -method MPI -out output\" : \\
    -n 1 python ../build/engine_py.py -mdi \"-role ENGINE -name MM -method MPI\"'''

    try:
        command = "cd " + build_dir + "\n" + mpiexec_general + command_suffix
        cmd_return = os.system( command )
        assert cmd_return == 0
    except AssertionError: # MCA
        command = "cd " + build_dir + "\n" + mpiexec_mca + command_suffix
        cmd_return = os.system( command )
        assert cmd_return == 1

    # read the output file
    output_file = open(build_dir + "/output", "r")
    output = output_file.read()

    assert output == " Engine name: MM\n"

def test_py_cxx_mpi():
    command_suffix = '''-n 1 python ../build/driver_py.py -mdi \"-role DRIVER -name driver -method MPI -out output\" : \\
    -n 1 ./$(find ../build/engine_cxx*) -mdi \"-role ENGINE -name MM -method MPI\"'''

    try:
        command = "cd " + build_dir + "\n" + mpiexec_general + command_suffix
        cmd_return = os.system( command )
        assert cmd_return == 0
    except AssertionError: # MCA
        command = "cd " + build_dir + "\n" + mpiexec_mca + command_suffix
        cmd_return = os.system( command )
        assert cmd_return == 1

    # read the output file
    output_file = open(build_dir + "/output", "r")
    output = output_file.read()

    assert output == " Engine name: MM\n"

def test_py_f90_mpi():
    command_suffix = '''mpiexec -n 1 python ../build/driver_py.py -mdi \"-role DRIVER -name driver -method MPI -out output\" : \\
    -n 1 ./$(find ../build/engine_f90*) -mdi \"-role ENGINE -name MM -method MPI\"'''

    try:
        command = "cd " + build_dir + "\n" + mpiexec_general + command_suffix
        cmd_return = os.system( command )
        assert cmd_return == 0
    except AssertionError: # MCA
        command = "cd " + build_dir + "\n" + mpiexec_mca + command_suffix
        cmd_return = os.system( command )
        assert cmd_return == 1

    # read the output file
    output_file = open(build_dir + "/output", "r")
    output = output_file.read()

    assert output == " Engine name: MM\n"

def test_py_py_mpi():
    command_suffix = '''-n 1 python ../build/driver_py.py -mdi \"-role DRIVER -name driver -method MPI -out output\" : \\
    -n 1 python ../build/engine_py.py -mdi \"-role ENGINE -name MM -method MPI\"'''

    try:
        command = "cd " + build_dir + "\n" + mpiexec_general + command_suffix
        cmd_return = os.system( command )
        assert cmd_return == 0
    except AssertionError: # MCA
        command = "cd " + build_dir + "\n" + mpiexec_mca + command_suffix
        cmd_return = os.system( command )
        assert cmd_return == 1

    # read the output file
    output_file = open(build_dir + "/output", "r")
    output = output_file.read()

    assert output == " Engine name: MM\n"



##########################
# TCP Method             #
##########################

def test_cxx_cxx_tcp():
    # get the names of the driver and engine codes, which include a .exe extension on Windows
    driver_name = glob.glob("../build/driver_cxx*")[0]
    engine_name = glob.glob("../build/engine_cxx*")[0]

    # run the calculation
    driver_proc = subprocess.Popen([driver_name, "-mdi", "-role DRIVER -name driver -method TCP -port 8021"],
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    engine_proc = subprocess.Popen([engine_name, "-mdi", "-role ENGINE -name MM -method TCP -port 8021 -hostname localhost"])
    driver_tup = driver_proc.communicate()
    engine_proc.communicate()

    # convert the driver's output into a string
    driver_out = format_return(driver_tup[0])
    driver_err = format_return(driver_tup[1])

    assert driver_err == ""
    assert driver_out == " Engine name: MM\n"

def test_cxx_f90_tcp():
    # get the names of the driver and engine codes, which include a .exe extension on Windows
    driver_name = glob.glob("../build/driver_cxx*")[0]
    engine_name = glob.glob("../build/engine_f90*")[0]

    # run the calculation
    driver_proc = subprocess.Popen([driver_name, "-mdi", "-role DRIVER -name driver -method TCP -port 8021"],
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    engine_proc = subprocess.Popen([engine_name, "-mdi", "-role ENGINE -name MM -method TCP -port 8021 -hostname localhost"])
    driver_tup = driver_proc.communicate()
    engine_proc.communicate()

    # convert the driver's output into a string
    driver_out = format_return(driver_tup[0])
    driver_err = format_return(driver_tup[1])

    assert driver_err == ""
    assert driver_out == " Engine name: MM\n"

def test_cxx_py_tcp():
    # get the name of the driver code, which includes a .exe extension on Windows
    driver_name = glob.glob("../build/driver_cxx*")[0]

    # run the calculation
    driver_proc = subprocess.Popen([driver_name, "-mdi", "-role DRIVER -name driver -method TCP -port 8021"],
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    engine_proc = subprocess.Popen([sys.executable, "../build/engine_py.py", "-mdi", "-role ENGINE -name MM -method TCP -port 8021 -hostname localhost"], 
                                   cwd=build_dir)
    driver_tup = driver_proc.communicate()
    engine_proc.communicate()

    # convert the driver's output into a string
    driver_out = format_return(driver_tup[0])
    driver_err = format_return(driver_tup[1])

    assert driver_err == ""
    assert driver_out == " Engine name: MM\n"

def test_f90_cxx_tcp():
    # get the names of the driver and engine codes, which include a .exe extension on Windows
    driver_name = glob.glob("../build/driver_f90*")[0]
    engine_name = glob.glob("../build/engine_cxx*")[0]

    # run the calculation
    driver_proc = subprocess.Popen([driver_name, "-mdi", "-role DRIVER -name driver -method TCP -port 8021"],
                                   stdout=subprocess.PIPE,  stderr=subprocess.PIPE)
    engine_proc = subprocess.Popen([engine_name, "-mdi", "-role ENGINE -name MM -method TCP -port 8021 -hostname localhost"])
    driver_tup = driver_proc.communicate()
    engine_proc.communicate()

    # convert the driver's output into a string
    driver_out = format_return(driver_tup[0])
    driver_err = format_return(driver_tup[1])

    assert driver_err == ""
    assert driver_out == " Engine name: MM\n"

def test_f90_f90_tcp():
    # get the names of the driver and engine codes, which include a .exe extension on Windows
    driver_name = glob.glob("../build/driver_f90*")[0]
    engine_name = glob.glob("../build/engine_f90*")[0]

    # run the calculation
    driver_proc = subprocess.Popen([driver_name, "-mdi", "-role DRIVER -name driver -method TCP -port 8021"],
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    engine_proc = subprocess.Popen([engine_name, "-mdi", "-role ENGINE -name MM -method TCP -port 8021 -hostname localhost"])
    driver_tup = driver_proc.communicate()
    engine_proc.communicate()

    # convert the driver's output into a string
    driver_out = format_return(driver_tup[0])
    driver_err = format_return(driver_tup[1])

    assert driver_err == ""
    assert driver_out == " Engine name: MM\n"

def test_f90_py_tcp():
    # get the name of the driver code, which includes a .exe extension on Windows
    driver_name = glob.glob("../build/driver_f90*")[0]

    # run the calculation
    driver_proc = subprocess.Popen([driver_name, "-mdi", "-role DRIVER -name driver -method TCP -port 8021"],
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    engine_proc = subprocess.Popen([sys.executable, "../build/engine_py.py", "-mdi", "-role ENGINE -name MM -method TCP -port 8021 -hostname localhost"],
                                   cwd=build_dir)
    driver_tup = driver_proc.communicate()
    engine_proc.communicate()

    # convert the driver's output into a string
    driver_out = format_return(driver_tup[0])
    driver_err = format_return(driver_tup[1])

    assert driver_err == ""
    assert driver_out == " Engine name: MM\n"

def test_py_cxx_tcp():
    # get the name of the engine code, which includes a .exe extension on Windows
    engine_name = glob.glob("../build/engine_cxx*")[0]

    # run the calculation
    driver_proc = subprocess.Popen([sys.executable, "../build/driver_py.py", "-mdi", "-role DRIVER -name driver -method TCP -port 8021"],
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=build_dir)
    engine_proc = subprocess.Popen([engine_name, "-mdi", "-role ENGINE -name MM -method TCP -port 8021 -hostname localhost"])
    driver_tup = driver_proc.communicate()
    engine_proc.communicate()

    # convert the driver's output into a string
    driver_out = format_return(driver_tup[0])
    driver_err = format_return(driver_tup[1])

    assert driver_err == ""
    assert driver_out == " Engine name: MM\n"

def test_py_f90_tcp():
    # get the name of the engine code, which includes a .exe extension on Windows
    engine_name = glob.glob("../build/engine_f90*")[0]

    # run the calculation
    driver_proc = subprocess.Popen([sys.executable, "../build/driver_py.py", "-mdi", "-role DRIVER -name driver -method TCP -port 8021"],
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=build_dir)
    engine_proc = subprocess.Popen([engine_name, "-mdi", "-role ENGINE -name MM -method TCP -port 8021 -hostname localhost"])
    driver_tup = driver_proc.communicate()
    engine_proc.communicate()

    # convert the driver's output into a string
    driver_out = format_return(driver_tup[0])
    driver_err = format_return(driver_tup[1])

    assert driver_err == ""
    assert driver_out == " Engine name: MM\n"

def test_py_py_tcp():
    # run the calculation
    driver_proc = subprocess.Popen([sys.executable, "../build/driver_py.py", "-mdi", "-role DRIVER -name driver -method TCP -port 8021"],
                                   stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=build_dir)
    engine_proc = subprocess.Popen([sys.executable, "../build/engine_py.py", "-mdi", "-role ENGINE -name MM -method TCP -port 8021 -hostname localhost"],
                                   cwd=build_dir)
    driver_tup = driver_proc.communicate()
    engine_proc.communicate()

    # convert the driver's output into a string
    driver_out = format_return(driver_tup[0])
    driver_err = format_return(driver_tup[1])

    assert driver_err == ""
    assert driver_out == " Engine name: MM\n"
