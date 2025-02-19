pkgname = "byacc"
pkgver = "20221106"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--program-transform=s,^,b,"]
pkgdesc = "Berkeley yacc, a LALR(1) parser generator"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:byacc"
url = "http://invisible-island.net/byacc"
source = f"https://invisible-island.net/archives/{pkgname}/{pkgname}-{pkgver}.tgz"
sha256 = "a899be227bbcac9cf7700f7dbb5a8494688f1f9f0617b510762daeace47b9d12"
hardening = ["vis", "cfi"]

def post_install(self):
    self.install_license("README")
    self.install_license("LICENSE")
    self.install_link("byacc", "usr/bin/yacc")
    self.install_link("byacc.1", "usr/share/man/man1/yacc.1")
