# Locate MPI

find_package(MPI)
if(MPI_FOUND)
   include_directories(${MPI_INCLUDE_PATH})
endif()



# Link to MDI

link_directories( ${mdi_path} )
include_directories( ${mdi_path} )



# Compile the engine

add_executable(engine_f90
               engine_f90.f90)
target_link_libraries(engine_f90 mdi
                      ${MPI_LIBRARIES})
set_target_properties(engine_f90 PROPERTIES
    RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}")



# Ensure that MPI is properly linked

if(NOT MPI_FOUND)
   target_include_directories(engine_f90 PRIVATE ${CMAKE_BINARY_DIR}/MDI_Test_Codes/STUBS_MPI)
endif()
if(MPI_COMPILE_FLAGS)
   set_target_properties(engine_f90 PROPERTIES
      COMPILE_FLAGS "${MPI_COMPILE_FLAGS}")
endif()
if(MPI_LINK_FLAGS)
   set_target_properties(engine_f90 PROPERTIES
      LINK_FLAGS "${MPI_LINK_FLAGS}")
endif()
