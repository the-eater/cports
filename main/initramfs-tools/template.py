pkgname = "initramfs-tools"
pkgver = "0.142"
pkgrel = 0
build_style = "makefile"
depends = [
    "base-kernel", "klibc-kinit-standalone", "klibc-utils-standalone",
    "bsdtar", "zstd", "debianutils", "ugetopt", "console-setup", "awk"
]
pkgdesc = "Generic modular initramfs generator"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = f"https://salsa.debian.org/kernel-team/initramfs-tools"
source = f"{url}/-/archive/v{pkgver}/{pkgname}-v{pkgver}.tar.gz"
sha256 = "27a78cc25acc3ca3d9c78deca165bf001b09b260ce25a3f3756e47a0e7bc0554"
# no tests
options = ["!check"]

def post_install(self):
    for f in ["50-initramfs"]:
        self.install_file(
            self.files_path / (f + ".sh"), "etc/kernel.d",
            mode = 0o755
        )

    # hook for core userland
    self.install_file(
        self.files_path / "chimerautils.initramfs-tools",
        "usr/share/initramfs-tools/hooks",
        mode = 0o755, name = "chimerautils"
    )
