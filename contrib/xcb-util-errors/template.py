pkgname = "xcb-util-errors"
pkgver = "1.0.1"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = ["pkgconf"]
makedepends = ["libxcb-devel"]
pkgdesc = "XCB errors library"
maintainer = "eater <=@eater.me>"
license = "MIT"
url = "https://xcb.freedesktop.org"
source = f"https://xcb.freedesktop.org/dist/xcb-util-errors-{pkgver}.tar.xz"
sha256 = "5628c87b984259ad927bacd8a42958319c36bdf4b065887803c9d820fb80f357"


@subpackage("xcb-util-errors-devel")
def _devel(self):
    return self.default_devel()
