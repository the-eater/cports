pkgname = "base-pbp"
pkgver = "0.1"
pkgrel = 0
archs = ["aarch64"]
depends = [
    "firmware-ap6256", "firmware-linux-rockchip",
    "u-boot-pinebook-pro-rk3399", "u-boot-menu",
]
pkgdesc = "Chimera base package for Pinebook Pro"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:none"
url = "https://chimera-linux.org"

def do_install(self):
    self.install_file(
        self.files_path / "60-pinebookpro.rules", "usr/lib/udev/rules.d"
    )
    self.install_file(
        self.files_path / "10-pinebookpro.hwdb", "usr/lib/udev/hwdb.d"
    )
    self.install_file(self.files_path / "asound.state", "var/lib/alsa")
    # u-boot-menu
    self.install_file(self.files_path / "u-boot-cmdline", "etc/default")
    self.install_file(self.files_path / "u-boot-fdt", "etc/default")
    # agetty service
    self.install_service(self.files_path / "agetty-ttyS2", enable = True)
