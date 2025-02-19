pkgname = "librsvg"
pkgver = "2.54.5"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--enable-introspection", "--enable-vala", "--disable-static",
    "--disable-gtk-doc",
]
make_cmd = "gmake"
hostmakedepends = [
    "gmake", "pkgconf", "cargo", "python", "gobject-introspection",
    "glib-devel", "gdk-pixbuf-devel", "vala", "python-docutils",
]
makedepends = [
    "rust", "vala-devel", "cairo-devel", "pango-devel", "freetype-devel",
    "gdk-pixbuf-devel", "libglib-devel", "libxml2-devel",
]
provides = [f"gdk-pixbuf-loader-svg={pkgver}-r{pkgrel}"]
pkgdesc = "SVG library for GNOME"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND LGPL-2.0-or-later"
url = "https://wiki.gnome.org/Projects/LibRsvg"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "4f03190f45324d1fa1f52a79dfcded1f64eaf49b3ae2f88eedab0c07617cae6e"
# sample files may differ based on pango/freetype/harfbuzz version
options = ["!check", "!cross"]

def post_patch(self):
    from cbuild.util import cargo

    # needed mainly for cross builds
    with open(self.cwd / ".cargo/config", "a") as cf:
        cf.write(f"""
[target.{self.profile().triplet}]
linker = "{self.get_tool("CC")}"
""")

    cargo.clear_vendor_checksums(self, "system-deps")

@subpackage("librsvg-devel")
def _devel(self):
    return self.default_devel()

@subpackage("librsvg-progs")
def _progs(self):
    return self.default_progs()
