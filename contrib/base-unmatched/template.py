pkgname = "base-unmatched"
pkgver = "0.1"
pkgrel = 0
archs = ["riscv64"]
depends = ["u-boot-sifive_unmatched", "u-boot-menu"]
pkgdesc = "Chimera base package for HiFive Unmatched"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:none"
url = "https://chimera-linux.org"

def do_install(self):
    # u-boot-menu
    self.install_file(self.files_path / "u-boot-cmdline", "etc/default")
    self.install_file(self.files_path / "u-boot-fdt", "etc/default")
    # agetty service
    self.install_service(self.files_path / "agetty-ttySIF0", enable = True)
