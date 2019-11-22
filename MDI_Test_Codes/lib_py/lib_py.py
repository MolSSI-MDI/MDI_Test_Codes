import sys
import time
try: # Check for installed package
    import mdi
except ImportError: # Check for local build
    try: # Python 3
        from lib.mdi import MDI_Library as mdi
    except ImportError: # Python 2
        sys.path.append('lib/mdi')
        import MDI_Library as mdi
try:
    import numpy
    use_numpy = True
except ImportError:
    use_numpy = False
try:
    from mpi4py import MPI
    use_mpi4py = True
except ImportError:
    use_mpi4py = False

# get the MPI communicator
if use_mpi4py:
    mpi_world = MPI.COMM_WORLD
else:
    mpi_world = None

######################################################################
# Engine code
######################################################################

exit_flag = False

def execute_command(command, comm):
    global exit_flag
    print("IN EXECUTE COMMAND")
    print("   COMMAND: " + str(command))

    if command == "EXIT":
        exit_flag = True
    elif command == "<NATOMS":
        print("SUCCESS")
        natoms = 123
        mdi.MDI_Send(natoms, 1, mdi.MDI_INT, comm)
    else:
        raise Exception("Error in engine_py.py: MDI command not recognized")

    return 0

def start_engine(mdi_options):
    global mpi_world
    # Initialize the MDI Library
    mdi.MDI_Init(mdi_options,mpi_world)
    if use_mpi4py:
        mpi_world = mdi.MDI_Get_Intra_Code_MPI_Comm()
        world_rank = mpi_world.Get_rank()
    else:
        world_rank = 0

    # Should NOT call MDI_Accept_Communicator() from the engine
    # Is there are way to confirm this?
    #print("Accepting communicator")
    #comm = mdi.MDI_Accept_Communicator()
    #print("Accepted communicator: " + str(comm))

    # Set the generic execute_command function
    print("Setting generic command")
    mdi.MDI_Set_Command_Func(execute_command)

    #while not exit_flag:
    #    if world_rank == 0:
    #        command = mdi.MDI_Recv_Command(comm)
    #    else:
    #        command = None
    #    if use_mpi4py:
    #        command = mpi_world.bcast(command, root=0)
    #
    #    execute_command( command, comm )


######################################################################
# Driver code
######################################################################

print("Start of driver")

# Initialize the MDI Library
mdi.MDI_Init(sys.argv[2],mpi_world)
if use_mpi4py:
    mpi_world = mdi.MDI_Get_Intra_Code_MPI_Comm()
    world_rank = mpi_world.Get_rank()
else:
    world_rank = 0

# Check if this connection uses the LIBRARY method
#method = MDI_Get_Method(comm)
method = mdi.MDI_LIB

if method == mdi.MDI_LIB:
    # Start the engine
    start_engine("-role ENGINE -name MM -method LIBRARY -driver_name driver")

# Connect to the driver
print("Accepting communicator")
comm = mdi.MDI_Accept_Communicator()
print("Accepted communicator: " + str(comm))

mdi.MDI_Send_Command("EXIT", comm)

mdi.MDI_Send_Command("<NATOMS", comm)
natoms = mdi.MDI_Recv(1, mdi.MDI_INT, comm)
print("NATOMS: " + str(natoms))

mdi.MDI_Send_Command("<NATOMS", comm)
natoms = mdi.MDI_Recv(1, mdi.MDI_INT, comm)
print("NATOMS: " + str(natoms))

mdi.MDI_Send_Command("<NAME", comm)
engine_name = mdi.MDI_Recv(mdi.MDI_NAME_LENGTH, mdi.MDI_CHAR, comm)
print("NAME: " + str(engine_name))
