pkgname = "wlroots"
pkgver = "0.16.2"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dxwayland=enabled", "-Drenderers=vulkan,gles2", "-Dbackends=libinput,drm,x11",
                  "-Dxcb-errors=enabled"]
hostmakedepends = ["meson", "wayland-protocols", "wayland-progs", "pkgconf", "cmake", "glslang-progs"]
makedepends = ["wayland-devel", "libdrm-devel", "libegl", "libgbm-devel", "libseat-devel", "vulkan-headers",
               "vulkan-loader", "hwdata-devel", "libliftoff-devel", "libdisplay-info-devel", "pixman-devel",
               "udev-devel", "libinput-devel", "libxkbcommon-devel", "mesa-devel", "libxcb-devel", "xwayland",
               "vulkan-loader", "xcb-util-wm-devel", "glslang-devel", "xcb-util-renderutil-devel",
               "xcb-util-errors-devel"]
pkgdesc = "Simple package"
maintainer = "eater <=@eater.me>"
license = "BSD-3-Clause"
url = "https://gitlab.freedesktop.org/wlroots/wlroots"
source = f"https://gitlab.freedesktop.org/wlroots/wlroots/-/archive/{pkgver}/wlroots-{pkgver}.tar.gz"
sha256 = "f502959db8bc029e32f10a837b37257bb8c5ed269bceddf9492f0bb381bebf76"
# lots of unused stuff
tool_flags = {"CFLAGS": ["-Wno-unused-but-set-variable", "-Wno-unused-variable", "-Wno-unused-function"]}


@subpackage("wlroots-devel")
def _devel(self):
    return self.default_devel()
