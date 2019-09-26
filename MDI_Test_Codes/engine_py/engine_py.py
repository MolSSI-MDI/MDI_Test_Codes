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

# Initialize the MDI Library
mdi.MDI_Init(sys.argv[2],mpi_world)
if use_mpi4py:
    mpi_world = mdi.MDI_Get_Intra_Code_MPI_Comm()
    world_rank = mpi_world.Get_rank()
else:
    world_rank = 0

# Connect to the driver
comm = mdi.MDI_Accept_Communicator()

while True:
    if world_rank == 0:
        command = mdi.MDI_Recv_Command(comm)
    else:
        command = None
    if use_mpi4py:
        command = mpi_world.bcast(command, root=0)

    if command == "EXIT":
        break
    else:
        raise Exception("Error in engine_py.py: MDI command not recognized")
