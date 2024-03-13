#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "hpp-fcl::hpp-fcl" for configuration "Release"
set_property(TARGET hpp-fcl::hpp-fcl APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(hpp-fcl::hpp-fcl PROPERTIES
  IMPORTED_LINK_DEPENDENT_LIBRARIES_RELEASE "Qhull::qhull_r"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libhpp-fcl.dylib"
  IMPORTED_SONAME_RELEASE "@rpath/libhpp-fcl.dylib"
  )

list(APPEND _cmake_import_check_targets hpp-fcl::hpp-fcl )
list(APPEND _cmake_import_check_files_for_hpp-fcl::hpp-fcl "${_IMPORT_PREFIX}/lib/libhpp-fcl.dylib" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
