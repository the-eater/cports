pkgname = "pkgconf"
pkgver = "1.9.3"
pkgrel = 0
build_style = "gnu_configure"
checkdepends = ["kyua"]
provides = [f"pc:libpkgconf={pkgver}"]
pkgdesc = "Provides compiler and linker configuration"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "http://pkgconf.org"
source = f"https://distfiles.dereferenced.org/pkgconf/pkgconf-{pkgver}.tar.xz"
sha256 = "5fb355b487d54fb6d341e4f18d4e2f7e813a6622cf03a9e87affa6a40565699d"
hardening = ["!cfi"] # TODO
# checkdepends not available yet
options = ["bootstrap", "!check"]

def post_install(self):
    self.install_license("COPYING")

    self.install_link("pkgconf", "usr/bin/pkg-config")
    self.install_link("pkgconf.1", "usr/share/man/man1/pkg-config.1")

@subpackage("libpkgconf")
def _lib(self):
    self.pkgdesc += " (runtime library)"
    return self.default_libs()

@subpackage("pkgconf-devel")
def _devel(self):
    self.options = ["!scanpkgconf"]
    # pkg.m4 must remain in main package
    return [
        "usr/include",
        "usr/lib/pkgconfig",
        "usr/lib/*.so",
        "usr/lib/*.a",
    ]
