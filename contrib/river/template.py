pkgname = "river"
pkgver = "0.2.4"
pkgrel = 0
build_style = "zig"
hostmakedepends = ["zig", "pkgconf", "wayland-progs", "wayland-protocols"]
makedepends = ["wayland-devel", "wlroots-devel"]
pkgdesc = "Dynamic tiling Wayland compositor"
maintainer = "eater <=@eater.me>"
license = "BSD-3-Clause"
url = "https://github.com/riverwm/river"
source = f"https://github.com/riverwm/river/releases/download/v{pkgver}/river-{pkgver}.tar.gz"
sha256 = "26c1c41a65ce3804069afad6988410515cf478d2b76303ebc699766d3d4dc69f"
