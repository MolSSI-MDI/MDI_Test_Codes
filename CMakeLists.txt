cmake_minimum_required(VERSION 3.5)

# mdi_path option

option(mdi_path "Path to the MDI Library")
if ( NOT mdi_path )
   set( mdi_path ${CMAKE_BINARY_DIR}/lib/mdi/MDI_Library/ )
   set( build_mdi ON )
else()
   set( build_mdi OFF )
endif()



# language option

option(language "language")

set(use_C "")
set(use_CXX "")
set(use_Fortran "")
set(use_Python "")

if( NOT language )
   # By default, compile for all languages
   set(use_C "C")
   set(use_CXX "CXX")
   set(use_Fortran "Fortran")
   set(use_Python "Python")
elseif( language STREQUAL "C" )
   set(use_C "C")
   set(use_CXX "CXX")
elseif( language STREQUAL "Fortran" )
   set(use_C "C")
   set(use_Fortran "Fortran")
elseif( language STREQUAL "Python" )
   set(use_C "C")
   set(use_Python "Python")
else()
   message( FATAL_ERROR "Language not supported.  Supported languages: C, Fortran, Python" )
endif()



project(MDI_Test_Codes
        LANGUAGES ${use_C} ${use_CXX} ${use_Fortran})

add_subdirectory(lib)
add_subdirectory(MDI_Test_Codes)
