import os.path

from conans import ConanFile, CMake
from conans import tools


class Acme(ConanFile):
    name = "Acme"
    version = "5.2.1.0"
    requires = ("Boost/1.60.0@lasote/stable",)
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports = ["conanfile.py", "CMakeLists.txt", "target/*", "src/*"]

    def imports(self):
       self.copy("*.dll", "", "bin")
       self.copy("*.dylib", "", "lib")

    def build(self):
        root = self.conanfile_directory

        cmake = CMake(self.settings)
        self.run('cmake "%s" %s' % (self.conanfile_directory,
                                    cmake.command_line))
        self.run("cmake --build . %s" % cmake.build_config)
