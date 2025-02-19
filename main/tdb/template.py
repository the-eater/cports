pkgname = "tdb"
pkgver = "1.4.7"
pkgrel = 0
build_style = "waf"
configure_script = "buildtools/bin/waf"
configure_args = [
    "--disable-rpath", "--disable-rpath-install",
    "--builtin-libraries=replace", "--bundled-libraries=NONE",
]
hostmakedepends = [
    "pkgconf", "python", "gettext-tiny", "docbook-xsl-nons", "xsltproc",
]
makedepends = [
    "python-devel", "gettext-tiny-devel"
]
pkgdesc = "Simple database API similar to gdbm"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-3.0-or-later"
url = "https://tdb.samba.org"
source = f"https://download.samba.org/pub/{pkgname}/{pkgname}-{pkgver}.tar.gz"
sha256 = "a4fb168def533f31ff2c07f7d9844bb3131e6799f094ebe77d0380adc987c20e"
# we don't want their makefile
env = {"PYTHONHASHSEED": "1", "WAF_MAKE": "1"}
# FIXME cfi
hardening = ["vis", "!cfi"]
options = ["!cross"]

@subpackage("tdb-devel")
def _devel(self):
    return self.default_devel()

@subpackage("tdb-progs")
def _devel(self):
    return self.default_progs()

@subpackage("tdb-python")
def _devel(self):
    self.pkgdesc = f"{pkgdesc} (Python bindings)"
    self.depends += ["python"]

    return ["usr/lib/python*"]
