pkgname = "glib"
pkgver = "2.74.6"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dgtk_doc=false", "-Dman=true", "-Dselinux=disabled",
]
make_check_wrapper = ["dbus-run-session"]
hostmakedepends = [
    "meson", "gettext-tiny", "pkgconf", "docbook-xsl-nons", "xsltproc",
]
makedepends = [
    "zlib-devel", "pcre2-devel", "libffi-devel", "dbus-devel",
    "elftoolchain-devel", "libmount-devel",
]
checkdepends = [
    "desktop-file-utils", "shared-mime-info", "dbus", "python-pytest"
]
triggers = ["/usr/share/glib-2.0/schemas", "/usr/lib/gio/modules"]
pkgdesc = "GLib library of C routines"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://wiki.gnome.org/Projects/GLib"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "069cf7e51cd261eb163aaf06c8d1754c6835f31252180aff5814e5afc7757fbc"
# FIXME int - e.g. g_ascii_strtoll fails
hardening = ["!int"]
# cyclic with desktop-file-utils
options = ["!check"]

def post_install(self):
    from cbuild.util import python

    self.install_license("COPYING")

    python.precompile(self, "usr/share/glib-2.0/codegen")
    python.precompile(self, "usr/share/glib-2.0/gdb")

@subpackage("libglib-devel")
def _libdevel(self):
    self.pkgdesc = f"{pkgdesc} (library development files)"

    return [
        "usr/include",
        "usr/lib/glib-2.0",
        "usr/lib/pkgconfig",
        "usr/lib/*.so",
    ]

@subpackage("glib-devel")
def _devel(self):
    self.depends += [f"libglib-devel={pkgver}-r{pkgrel}"]

    return self.default_devel(extra = [
        "usr/bin/glib-compile-resources",
        "usr/bin/glib-genmarshal",
        "usr/bin/glib-gettextize",
        "usr/bin/glib-mkenums",
        "usr/bin/gtester",
        "usr/bin/gtester-report",
        "usr/bin/gdbus-codegen",
        "usr/share/man/man1/glib-compile-resources.1",
        "usr/share/man/man1/glib-genmarshal.1",
        "usr/share/man/man1/glib-gettextize.1",
        "usr/share/man/man1/glib-mkenums.1",
        "usr/share/man/man1/gtester.1",
        "usr/share/man/man1/gtester-report.1",
        "usr/share/man/man1/gdbus-codegen.1",
        "usr/share/glib-2.0",
        "usr/share/gdb",
    ])
