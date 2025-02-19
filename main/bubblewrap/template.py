pkgname = "bubblewrap"
pkgver = "0.7.0"
pkgrel = 0
build_style = "gnu_configure"
make_check_args = ["-j1"]
hostmakedepends = ["pkgconf", "xsltproc", "docbook-xsl-nons"]
makedepends = ["libcap-devel"]
checkdepends = ["bash", "libcap-progs"]
pkgdesc = "Unprivileged sandboxing tool"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.0-or-later"
url = "https://github.com/containers/bubblewrap"
source = f"https://github.com/containers/{pkgname}/releases/download/v{pkgver}/{pkgname}-{pkgver}.tar.xz"
sha256 = "764ab7100bd037ea53d440d362e099d7a425966bc62d1f00ab26b8fbb882a9dc"
tool_flags = {"CFLAGS": ["-Wno-error,-Wformat-nonliteral"]}
hardening = ["vis", "cfi"]
