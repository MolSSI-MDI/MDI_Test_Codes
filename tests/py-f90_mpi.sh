mpiexec -n 1 python driver_py.py -mdi "-role DRIVER -name driver -method MPI" : \
    -n 1 ./$(find engine_f90*) -mdi "-role ENGINE -name MM -method MPI"