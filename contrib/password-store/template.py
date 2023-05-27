pkgname = "password-store"
pkgver = "1.7.4"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_install_args = ["WITH_ALLCOMP=yes"]
make_check_target = "test"
hostmakedepends = ["gmake"]
depends = ["bash", "gnupg", "tree", "ugetopt", "chimerautils", "git"]
checkdepends = [*depends]
pkgdesc = "Standard unix password manager"
maintainer = "eater <=@eater.me>"
license = "GPL-2.0-or-later"
url = "https://www.passwordstore.org"
source = f"https://git.zx2c4.com/password-store/snapshot/password-store-{pkgver}.tar.xz"
sha256 = "cfa9faf659f2ed6b38e7a7c3fb43e177d00edbacc6265e6e32215ff40e3793c0"

def do_build(self):
    pass

def post_install(self):
    self.install_license("COPYING")