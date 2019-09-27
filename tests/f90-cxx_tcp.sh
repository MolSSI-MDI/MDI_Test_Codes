#./$(find driver_f90*) -mdi "-role DRIVER -name driver -method TCP -port 8021" &
#./$(find engine_cxx*) -mdi "-role ENGINE -name MM -method TCP -port 8021 -hostname localhost" &
#wait
#./$(find driver_f90*) -mdi "-role DRIVER -name driver -method TCP -port 8021"
mpirun -n 1 ./$(find driver_f90*) -mdi "-role DRIVER -name driver -method TCP -port 8021"
