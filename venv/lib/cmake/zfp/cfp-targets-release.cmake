#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "zfp::cfp" for configuration "Release"
set_property(TARGET zfp::cfp APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(zfp::cfp PROPERTIES
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libcfp.so.1.0.1"
  IMPORTED_SONAME_RELEASE "libcfp.so.1"
  )

list(APPEND _cmake_import_check_targets zfp::cfp )
list(APPEND _cmake_import_check_files_for_zfp::cfp "${_IMPORT_PREFIX}/lib/libcfp.so.1.0.1" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
