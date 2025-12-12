#                                               -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.

AC_PREREQ([2.71])
AC_INIT([CuraEngine], [5.4.0])
AM_INIT_AUTOMAKE([subdir-objects foreign])
AC_CONFIG_SRCDIR([src/Slice.cpp])
AC_CONFIG_HEADERS([config.h])
AC_CONFIG_MACRO_DIR([m4])

AC_ARG_WITH([arcus], AS_HELP_STRING([--without-arcus], [Build without support for libArcus]))

# Checks for programs.
AC_PROG_CXX
AC_PROG_CC
AC_LANG(C++)
AS_IF([test "x$with_arcus" != "xno"],[AC_PATH_PROG([PROTOC],[protoc],[no])]
[AS_IF([test "x${PROTOC}" == "xno"], [AC_MSG_ERROR([ProtoBuf compiler "protoc" not found.])])])
AC_SUBST([PROTOC])

# Checks for libraries.
AX_CXX_CHECK_LIB(polyclipping, [ClipperLib::ClipperOffset::Clear()],,AC_MSG_ERROR([Could not find required Angus Johnson's clipper library]))
AX_CXX_CHECK_LIB(spdlog, [spdlog::spdlog_ex::what() const],,AC_MSG_ERROR([Could not find required spdlog library]))

PKG_CHECK_MODULES(FMT, [fmt],,AC_MSG_ERROR([Could not find required fmt library]))
AC_SUBST([FMT_CFLAGS])
AC_SUBST([FMT_LIBS])
PKG_CHECK_MODULES(TBB, [tbb],,AC_MSG_ERROR([Could not find required tbb library]))
AC_SUBST([TBB_CFLAGS])
AC_SUBST([TBB_LIBS])

AS_IF([test "x$with_arcus" != "xno"],
[AX_CXX_CHECK_LIB(Arcus,[Arcus::Socket::getState() const],arcus=yes,AC_MSG_WARN([Could not find requested Arcus library: building without Arcus support]))]
[PKG_CHECK_MODULES(PROTOBUF, protobuf >= 2.4.0,,[AC_MSG_ERROR([cannot find protobuf library required when building with arcus])])])
AS_IF([test "x$arcus" = "xyes"],ARCUS_CPPFLAGS=-DARCUS)
AM_CONDITIONAL([ARCUS],[test "x$arcus" = "xyes"])
AC_SUBST([ARCUS_CPPFLAGS])
AC_SUBST(PROTOBUF_LIBS)
AC_SUBST(PROTOBUF_CFLAGS)

# Checks for header files.
AC_CHECK_HEADERS([arpa/inet.h netinet/in.h stdint.h sys/socket.h sys/time.h unistd.h])
AC_CHECK_HEADER(polyclipping/clipper.hpp,,AC_MSG_ERROR([Could not find Angus Johnson's clipper header]))
AC_CHECK_HEADER(rapidjson/rapidjson.h,,AC_MSG_ERROR([Could not find rapidjson header]))
AC_CHECK_HEADER(mapbox/geometry/wagyu/wagyu.hpp,,AC_MSG_ERROR([Could not find mapbox wagyu header]))
AC_CHECK_HEADER(stb/stb_image.h,,AC_MSG_ERROR([Could not find stb header]))
AC_CHECK_HEADER(spdlog/spdlog.h,,AC_MSG_ERROR([Could not find spdlog header]))
AC_CHECK_HEADER([fmt/format.h],,AC_MSG_ERROR([Could not find libfmt header]))
AC_CHECK_HEADER(range/v3/view/enumerate.hpp,,AC_MSG_ERROR([Could not find range-v3 header]))
AC_CHECK_HEADER(scripta/logger.h,,AC_MSG_ERROR([Could not find ultimaker scripta header]))

# Checks for typedefs, structures, and compiler characteristics.
AC_CHECK_HEADER_STDBOOL
AC_C_INLINE
AC_C_RESTRICT
AC_TYPE_INT16_T
AC_TYPE_INT32_T
AC_TYPE_INT64_T
AC_TYPE_PID_T
AC_TYPE_SIZE_T
AC_TYPE_UINT8_T
AC_TYPE_UINT16_T
AC_TYPE_UINT32_T
AC_TYPE_UINT64_T
AC_CHECK_TYPES([ptrdiff_t])

# Checks for library functions.
AC_FUNC_ERROR_AT_LINE
AC_FUNC_STRTOD
AC_FUNC_FORK
AC_CHECK_FUNCS([floor gettimeofday memset pow socket sqrt strrchr strstr strtol])

AC_CONFIG_FILES([
 Makefile
 src/Makefile
])

AC_OUTPUT
