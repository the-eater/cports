pkgname = "ccache"
pkgver = "4.7.3"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DENABLE_TESTING=OFF", "-DREDIS_STORAGE_BACKEND=OFF"]
make_check_target = "check"
hostmakedepends = ["cmake", "ninja", "perl"]
makedepends = ["libzstd-devel", "zlib-devel"]
checkdepends = ["bash"]
pkgdesc = "Fast C/C++ compiler cache"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://ccache.samba.org"
source = f"https://github.com/ccache/ccache/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "65c53e8fd85956238670278854c02574094e61aecb09c4bf8a0d42657f8f0a6d"
hardening = ["vis", "cfi"]
# not properly set up
options = ["!check"]

def post_install(self):
    self.install_dir("usr/lib/ccache/bin")
    self.install_link("../../../bin/ccache", "usr/lib/ccache/bin/clang")
    self.install_link("../../../bin/ccache", "usr/lib/ccache/bin/clang++")
    self.install_link("../../../bin/ccache", "usr/lib/ccache/bin/cc")
    self.install_link("../../../bin/ccache", "usr/lib/ccache/bin/c++")
