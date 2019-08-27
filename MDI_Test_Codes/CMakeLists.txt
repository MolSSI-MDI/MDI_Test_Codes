add_subdirectory(STUBS_MPI)

if ( use_C )
   add_subdirectory(driver_cxx)
   add_subdirectory(engine_cxx)
endif()

if ( use_Fortran )
   add_subdirectory(driver_f90)
   add_subdirectory(engine_f90)
endif()

if ( use_Python )
   add_subdirectory(driver_py)
   add_subdirectory(engine_py)
endif()
