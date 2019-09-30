mpiexec -n 1 ./$(find driver_f90*) -mdi "-role DRIVER -name driver -method MPI" : \
    -n 1 python engine_py.py -mdi "-role ENGINE -name MM -method MPI"
