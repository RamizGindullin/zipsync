from conan import ConanFile
from conan.tools.cmake import cmake_layout, CMake

class ZipsyncConan(ConanFile):
    name = "zipsync"
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeDeps", "CMakeToolchain"
    requires = [
        "zlib/1.3.1",
        "minizip/1.3.1",
        "libcurl/8.6.0",
        "doctest/2.4.11",
        "libb2/20190723",
        "taywee-args/6.4.6",
        "libmicrohttpd/0.9.77",
    ]

    def layout(self):
        cmake_layout(self)        

    def configure(self):
        self.options["minizip"].bzip2 = False
        self.options["libcurl"].with_ssl = False
        # SSE2 is x86/x86_64 only — ARM uses the reference implementation
        is_x86 = self.settings.arch in ["x86", "x86_64"]
        self.options["libb2"].use_sse = is_x86

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
