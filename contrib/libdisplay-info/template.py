pkgname = "libdisplay-info"
pkgver = "0.1.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson"]
makedepends = ["hwdata-devel", "pkgconf"]
pkgdesc = "EDID and DisplayID library"
maintainer = "eater <=@eater.me>"
license = "MIT"
url = "https://gitlab.freedesktop.org/emersion/libdisplay-info"
source = f"https://gitlab.freedesktop.org/emersion/libdisplay-info/-/archive/{pkgver}/libdisplay-info-{pkgver}.tar.gz"
sha256 = "a5aeef57817916286526292ec816a5338c4d3c0094ce91e584fc82b57070a44f"
# requires edid-decode, and can't be bothered right now
options = ["!check"]


@subpackage("libdisplay-info-devel")
def _devel(self):
    return self.default_devel()
