import os

from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMakeDeps, CMake, cmake_layout
from conan.tools import files
from conans import tools
from conan.errors import ConanInvalidConfiguration
from conans.errors import ConanException

required_conan_version = ">=1.47.0"


class CuraEngineConan(ConanFile):
    name = "curaengine"
    license = "AGPL-3.0"
    author = "Ultimaker B.V."
    url = "https://github.com/Ultimaker/CuraEngine"
    description = "Powerful, fast and robust engine for converting 3D models into g-code instructions for 3D printers. It is part of the larger open source project Cura."
    topics = ("cura", "protobuf", "gcode", "c++", "curaengine", "libarcus", "gcode-generation", "3D-printing")
    build_policy = "missing"
    exports = "LICENSE*"
    settings = "os", "compiler", "build_type", "arch"
    short_paths = True
    options = {
        "enable_arcus": [True, False],
        "enable_openmp": [True, False],
        "enable_testing": [True, False]
    }
    default_options = {
        "enable_arcus": True,
        "enable_openmp": True,
        "enable_testing": False
    }
    scm = {
        "type": "git",
        "subfolder": ".",
        "url": "auto",
        "revision": "auto"
    }

    @property
    def _conan_data_version(self):
        version = tools.Version(self.version)
        return f"{version.major}.{version.minor}.{version.patch}-{version.prerelease}"

    def config_options(self):
        if self.settings.os == "Macos":
            self.options.enable_openmp = False

    def configure(self):
        self.options["boost"].header_only = True
        self.options["*"].shared = True

    def validate(self):
        if self.settings.compiler.get_safe("cppstd"):
            tools.check_min_cppstd(self, 17)
        if self.version:
            if tools.Version(self.version) <= tools.Version("4"):
                raise ConanInvalidConfiguration("Only versions 5+ are support")

    def build_requirements(self):
        self.tool_requires("ninja/[>=1.10.0]")
        self.tool_requires("cmake/[>=3.23.0]")
        if self.options.enable_arcus:
            self.tool_requires("protobuf/3.17.1")
        if self.options.enable_testing:
            self.test_requires("gtest/[>=1.10.0]")

    def requirements(self):
        for req in self.conan_data["requirements"][self._conan_data_version]:
            self.requires(req)
        if self.options.enable_arcus:
            for req in self.conan_data["requirements_arcus"][self._conan_data_version]:
                self.requires(req)

    def generate(self):
        cmake = CMakeDeps(self)
        if self.options.enable_arcus:
            if len(cmake.build_context_activated) == 0:
                cmake.build_context_activated = ["protobuf"]
            else:
                cmake.build_context_activated.append("protobuf")
            cmake.build_context_suffix = {"protobuf": "_BUILD"}
            if len(cmake.build_context_activated) == 0:
                cmake.build_context_build_modules = ["protobuf"]
            else:
                cmake.build_context_build_modules.append("protobuf")

        if self.options.enable_testing:
            if len(cmake.build_context_build_modules) == 0:
                cmake.build_context_activated = ["gtest"]
            else:
                cmake.build_context_activated.append("gtest")
        cmake.generate()

        tc = CMakeToolchain(self, generator = "Ninja")

        tc.variables["ENABLE_ARCUS"] = self.options.enable_arcus
        tc.variables["BUILD_TESTING"] = self.options.enable_testing
        tc.variables["ENABLE_OPENMP"] = self.options.enable_openmp
        tc.variables["ALLOW_IN_SOURCE_BUILD"] = True

        # Don't use Visual Studio as the CMAKE_GENERATOR
        if self.settings.compiler == "Visual Studio":
            tc.blocks["generic_system"].values["generator_platform"] = None
            tc.blocks["generic_system"].values["toolset"] = None

        tc.generate()

    def layout(self):
        self.folders.source = "."
        try:
            build_type = str(self.settings.build_type)
        except ConanException:
            raise ConanException("'build_type' setting not defined, it is necessary")

        self.folders.build = f"cmake-build-{build_type.lower()}"
        self.folders.generators = os.path.join(self.folders.build, "conan")

        self.cpp.source.includedirs = ["src"]  # TODO: Seperate headers and cpp

        self.cpp.build.libdirs = ["."]
        self.cpp.build.bindirs = ["."]

        self.cpp.build.libs = ["_CuraEngine"]

        self.cpp.package.includedirs = ["include"]
        self.cpp.package.libdirs = ["lib"]
        self.cpp.package.bindirs = ['bin']

    def imports(self):
        if (self.settings.os == "Windows" or self.settings.os == "Macos") and not self.in_local_cache:
            self.copy("*.dll", dst=self.build_folder, src="@bindirs")
            self.copy("*.dylib", dst=self.build_folder, src="@bindirs")
        if self.options.enable_testing:
            if self.settings.os == "Windows" and not self.in_local_cache:
                dest = os.path.join(self.build_folder, "tests")
                self.copy("*.dll", dst=dest, src="@bindirs")
                self.copy("*.dylib", dst=dest, src="@bindirs")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        if self.options.enable_testing:
            cmake.test()

    def package(self):
        packager = files.AutoPackager(self)
        packager.run()

        files.rmdir(self, os.path.join(self.package_folder, "bin", "CMakeFiles"))
