pkgname = "zig"
pkgver = "0.10.1"
pkgrel = 0
build_style = "cmake"
configure_args = [
    # zig defaults to Debug: https://github.com/ziglang/zig/blob/master/CMakeLists.txt#L3
    "-DCMAKE_BUILD_TYPE=None",
    "-DZIG_SHARED_LLVM=ON",
    # if not given it will use the equivalent of "-march=native"
    "-DZIG_TARGET_MCPU=baseline"
]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["lld-devel", "llvm-devel", "clang-devel", "zlib-devel", "ncurses-devel", "linux-headers"]
pkgdesc = "Programming language designed for robustness, optimality, and clarity"
maintainer = "eater <=@eater.me"
license = "MIT"
url = "https://ziglang.org"
source = f"https://ziglang.org/download/{pkgver}/zig-{pkgver}.tar.xz"
sha256 = "69459bc804333df077d441ef052ffa143d53012b655a51f04cfef1414c04168c"


def do_check(self):
    # taken from https://github.com/archlinux/svntogit-community/blob/packages/zig/trunk/PKGBUILD#L36
    # PR is in the works for a test target, however currently not available, nor can we access zig stage 3
    # since zig stage 3 is only available "cached"
    self.make.install(default_args=False, args_use_env=True, env={"DESTDIR": "./checkdest"})
    self.do("./checkdest/usr/bin/zig", "build", "test", "-Dconfig_h=build/config.h", "-Dstatic-llvm=false",
            "-Denable-llvm=true", "-Dskip-non-native=true")
