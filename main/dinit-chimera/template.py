pkgname = "dinit-chimera"
_commit = "c732fdba60559a11c4b3ff2d511839a7dc6e3110"
pkgver = "0.11"
pkgrel = 0
build_style = "makefile"
makedepends = ["linux-headers"]
depends = [
    "dinit", "tzdata",
    "virtual:cmd:mkdir!chimerautils",
    "virtual:cmd:grep!chimerautils",
    "virtual:cmd:sed!chimerautils",
    "virtual:cmd:install!chimerautils",
    "virtual:cmd:awk!awk",
    "virtual:cmd:kmod!kmod",
    "virtual:cmd:modprobe!kmod",
    "virtual:cmd:fsck!mount",
    "virtual:cmd:findmnt!mount",
    "virtual:cmd:mount!mount",
    "virtual:cmd:mountpoint!mount",
    "virtual:cmd:swapon!mount",
    "virtual:cmd:sysctl!procps",
    "virtual:cmd:udevadm!udev",
]
pkgdesc = "Chimera core services suite"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-2-Clause"
url = f"https://github.com/chimera-linux/dinit-chimera"
source = f"https://github.com/chimera-linux/dinit-chimera/archive/{_commit}.tar.gz"
sha256 = "f8a457821eeff2c33bf475cb1299ab7386332ab84e3a939581f7945f419005f3"
hardening = ["vis", "cfi"]
# no tests
options = ["!check", "brokenlinks"]

def post_install(self):
    self.install_file(self.files_path / "hostname", "etc")
    self.install_file(self.files_path / "locale.conf", "etc")
    # init symlink
    self.install_dir("usr/bin")
    self.install_link("dinit", "usr/bin/init")
    # x11 support
    self.install_dir("etc/X11/Xsession.d")
    self.install_file(
        self.files_path / "01dinit-env", "etc/X11/Xsession.d", mode = 0o755
    )
    # to be removed upstream later
    for f in (self.destdir / "usr/lib/dinit.d/boot.d").glob("agetty-*"):
        f.unlink()
    for f in (self.destdir / "etc/dinit.d").glob("agetty-*"):
        f.unlink()

@subpackage("dinit-chimera-x11")
def _x11(self):
    self.pkgdesc = f"{pkgdesc} (X11 support)"
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}", "xinit"]
    return [
        "etc/X11/Xsession.d",
    ]
