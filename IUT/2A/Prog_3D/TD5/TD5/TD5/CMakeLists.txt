cmake_minimum_required(VERSION 2.8)

set(CMAKE_OSX_DEPLOYMENT_TARGET "10.15" CACHE STRING "Minimum OS X deployment version")
	SET( MY_PATH ${CMAKE_INCLUDE_PATH}
          $ENV{include}
          ${OPENGL_INCLUDE_DIR}
          /usr/include
          /usr/local/include)


PROJECT(exo_3D)


IF(APPLE)
	SET( OperatingSystem "Mac os X")


ENDIF (APPLE)

IF(${CMAKE_SYSTEM_NAME} MATCHES "Linux")
	SET(OperatingSystem "Linux")
	SET(LINUX TRUE)
	add_definitions(-DLINUX) 

ENDIF(${CMAKE_SYSTEM_NAME} MATCHES "Linux")


IF(WIN32)
	SET( OperatingSystem "Microsoft Windows")
	SET(WINDOWS TRUE)
        add_definitions(-DWINDOWS) 
ENDIF (WIN32)

MESSAGE(STATUS "Operating System is: ${OperatingSystem}")

if ("${CMAKE_CXX_COMPILER_ID}" STREQUAL "GNU" OR
    "${CMAKE_CXX_COMPILER_ID}" STREQUAL "Clang")
    set(warnings "-Wno-deprecated")
endif()

if (NOT CONFIGURED_ONCE)
    set(CMAKE_CXX_FLAGS "${warnings}"
        CACHE STRING "Flags used by the compiler during all build types." FORCE)
    set(CMAKE_C_FLAGS   "${warnings}"
        CACHE STRING "Flags used by the compiler during all build types." FORCE)
endif()



find_package(OpenGL REQUIRED)
include_directories( ${OPENGL_INCLUDE_DIRS}  )
set(MyLibraries ${OPENGL_LIBRARIES})


IF (WINDOWS OR LINUX)
	find_package(GLEW REQUIRED)
	if (GLEW_FOUND)
	    include_directories($(GLEW_INCLUDE_DIRS))
	    IF(WINDOWS)
	    set(GLEW_LIBRARY "-lglew32")
	    ENDIF(WINDOWS)
	    IF(OperatingSystem MATCHES "Linux")
		set(GLEW_LIBRARY "-lGLEW")
	    endif()
	endif()
	set(MyLibraries ${MyLibraries} ${GLEW_LIBRARY})
ENDIF ()


if(APPLE OR WINDOWS)
	find_package(GLUT QUIET)
	include_directories(   ${GLUT_INCLUDE_DIRS} )
	set(MyLibraries ${MyLibraries} ${GLUT_LIBRARY})
FIND_PATH(
		  GLM_INCLUDE_DIR glm/glm.hpp 
		  ${CMAKE_INCLUDE_PATH}
		  $ENV{include}
		  ${OPENGL_INCLUDE_DIR}
		  /usr/include
		  /usr/local/include
		)


endif()

if(LINUX)
	find_package(FREEGLUT QUIET)

	if(FREEGLUT_FOUND)
		include_directories(  ${FREEGLUT_INCLUDE_DIR})
		set(MyLibraries ${MyLibraries} ${FREEGLUT_LIBRARY})
	else(FREEGLUT_FOUND)

		FIND_PATH(
		  FREEGLUT_INCLUDE_DIR GL/freeglut.h GL/gl.h GL/glu.h GL/glew.h
		  ${CMAKE_INCLUDE_PATH}
		  $ENV{include}
		  ${OPENGL_INCLUDE_DIR}
		  /usr/include
		  /usr/local/include
		)

		SET(STORE_CMAKE_FIND_FRAMEWORK ${CMAKE_FIND_FRAMEWORK})
		SET(CMAKE_FIND_FRAMEWORK NEVER)

		FIND_LIBRARY(
		  FREEGLUT_LIBRARY
		  NAMES freeglut_static freeglut glut GL
		  PATH
		    /opt/local/lib
		    ${CMAKE_LIBRARY_PATH}
		    $ENV{lib}
		    /usr/lib
		    /usr/local/lib
		)

		SET(CMAKE_FIND_FRAMEWORK ${STORE_CMAKE_FIND_FRAMEWORK})

		IF (FREEGLUT_INCLUDE_DIR AND FREEGLUT_LIBRARY)
		   SET(FREEGLUT_FOUND TRUE)
		ENDIF (FREEGLUT_INCLUDE_DIR AND FREEGLUT_LIBRARY)

		IF (FREEGLUT_FOUND)

		      MESSAGE(STATUS "Found FREEGLUT: ${FREEGLUT_LIBRARY}")
			include_directories(   ${FREEGLUT_INCLUDE_DIR} -lGL -lGLU -lglut -lGLEW )		
			set(MyLibraries ${MyLibraries} ${FREEGLUT_LIBRARY})

		ELSE (FREEGLUT_FOUND)
		   IF (FREEGLUT_FIND_REQUIRED)
		      MESSAGE(FATAL_ERROR "Could not find FREEGLUT")
		ELSE(FREEGLUT_FIND_REQUIRED)
		find_package(GLUT QUIET)
		IF (GLUT_FOUND)
			MESSAGE(STATUS "Found GLUT instead of freeglut in linux: ${GLUT_LIBRARY}")
			include_directories(   ${GLUT_INCLUDE_DIRS} )
			set(MyLibraries ${MyLibraries} ${GLUT_LIBRARY})
		 ELSE(GLUT_FOUND)
		 	MESSAGE(STATUS "Do not found any GLUT  in this linux")
		 ENDIF(GLUT_FOUND)
		   ENDIF (FREEGLUT_FIND_REQUIRED)
			 ENDIF (FREEGLUT_FOUND)
	ENDIF (FREEGLUT_FOUND)
endif(LINUX)


IF (FREEGLUT_FOUND)
       add_definitions(-DFREEGLUT) 
ENDIF()



SET( USE_SYSTEM_GLM TRUE)
IF(USE_SYSTEM_GLM)
    
    IF(NOT APPLE)
	 FIND_PACKAGE(GLM QUIET) 
	ENDIF()
    IF(APPLE OR (NOT glm_found AND NOT GLM_FOUND))
        MESSAGE(WARNING "GLM Not directly found")
	FIND_PATH(
          GLM_INCLUDE_DIRS glm/glm.hpp
          ${MY_PATH})
 
	MESSAGE(WARNING "found:${GLM_INCLUDE_DIRS}" )
    ENDIF(NOT glm_found AND NOT GLM_FOUND)
    if (GLM_INCLUDE_DIRS)
     include_directories(${GLM_INCLUDE_DIRS})
	MESSAGE(WARNING "found:${GLM_INCLUDE_DIRS}" )
    else (GLM_INCLUDE_DIRS)
       message(FATAL_ERROR "GLM definitely not found")
    endif(GLM_INCLUDE_DIRS)
   
ENDIF(USE_SYSTEM_GLM)


SET(GCC_COVERAGE_COMPILE_FLAGS "-std=c++11 -Wno-deprecated-declarations")

SET(GCC_COVERAGE_LINK_FLAGS    "-lm")

SET( CMAKE_CXX_FLAGS  "${CMAKE_CXX_FLAGS} ${GCC_COVERAGE_COMPILE_FLAGS}" )
SET( CMAKE_EXE_LINKER_FLAGS  "${CMAKE_EXE_LINKER_FLAGS} ${GCC_COVERAGE_LINK_FLAGS}" )


SET(SHADERS ${CMAKE_CURRENT_SOURCE_DIR}/shaders/*)

file(GLOB SRC_LIST ${CMAKE_CURRENT_SOURCE_DIR}/*.cpp ${SHADERS})


add_executable(${PROJECT_NAME} ${SRC_LIST})

set (MY_SHADER_PATH ${CMAKE_CURRENT_SOURCE_DIR})
set (MY_MESHES_PATH ${CMAKE_CURRENT_SOURCE_DIR})


configure_file (
  "${PROJECT_SOURCE_DIR}/Config.h.in"
  "${PROJECT_BINARY_DIR}/Config.h"
  )

include_directories(${PROJECT_BINARY_DIR})


target_link_libraries(${PROJECT_NAME}  ${GCC_COVERAGE_LINK_FLAGS}  ${MyLibraries})

set(CONFIGURED_ONCE TRUE CACHE INTERNAL
    "A flag showing that CMake has configured at least once.")


# Add a test:
enable_testing()
add_test(SimpleTest ${PROJECT_NAME})

add_custom_target(check COMMAND ${CMAKE_CTEST_COMMAND}
                  DEPENDS ${PROJECT_NAME})


#GET_DIRECTORY_PROPERTY(output INCLUDE_DIRECTORIES)
#MESSAGE(WARNING ${output})

#set(USED_CMAKE_GENERATOR "${CMAKE_GENERATOR}" CACHE STRING "Expose CMAKE_GENERATOR" FORCE)
#MESSAGE(WARNING ${USED_CMAKE_GENERATOR})
