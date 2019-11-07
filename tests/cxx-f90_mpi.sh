mpiexec -n 1 ./$(find driver_cxx*) -mdi "-role DRIVER -name driver -method MPI" : \
    -n 1 ./$(find engine_f90*) -mdi "-role ENGINE -name MM -method MPI"
