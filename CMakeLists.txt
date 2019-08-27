cmake_minimum_required(VERSION 3.5)

option(mdi_path "Path to the MDI Library")
if ( NOT mdi_path )
   set( mdi_path ${CMAKE_BINARY_DIR}/lib/mdi/MDI_Library/ )
endif()

project(MDI_Test_Codes
        LANGUAGES C CXX Fortran)

add_subdirectory(lib)
add_subdirectory(MDI_Test_Codes)
