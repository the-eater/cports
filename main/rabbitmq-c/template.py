pkgname = "rabbitmq-c"
pkgver = "0.11.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_STATIC_LIBS=ON", "-DBUILD_SHARED_LIBS=ON",
    "-DENABLE_SSL_SUPPORT=ON", "-DBUILD_TESTS=ON", "-DBUILD_TOOLS=ON"
]
hostmakedepends = ["cmake", "ninja", "pkgconf", "doxygen", "xmlto"]
makedepends = ["openssl-devel", "popt-devel"]
pkgdesc = "RabbitMQ C client"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://github.com/alanxz/rabbitmq-c"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "437d45e0e35c18cf3e59bcfe5dfe37566547eb121e69fca64b98f5d2c1c2d424"
hardening = ["vis", "cfi"]

def post_install(self):
    self.install_license("LICENSE-MIT")

@subpackage("rabbitmq-c-devel")
def _devel(self):
    return self.default_devel()

@subpackage("rabbitmq-c-progs")
def _progs(self):
    return self.default_progs()
