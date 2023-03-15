pkgname = "libliftoff"
pkgver = "0.4.1"
pkgrel = 0
build_style = "meson"
configure_args = ["-Db_ndebug=false"]
hostmakedepends = ["meson", "pkgconf"]
makedepends = ["libdrm-devel"]
pkgdesc = "Lightweight KMS plane library"
maintainer = "eater <=@eater.me>"
license = "MIT"
url = "https://gitlab.freedesktop.org/emersion/libliftoff"
source = f"https://gitlab.freedesktop.org/emersion/libliftoff/-/archive/v{pkgver}/libliftoff-v{pkgver}.tar.gz"
sha256 = "44ec5cfdd0df040d1023d4d6a48b23c31f21ce61ee2347da9e1ca244fe24dd1c"


@subpackage("libliftoff-devel")
def _devel(self):
    return self.default_devel()
