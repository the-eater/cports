pkgname = "gvfs"
pkgver = "1.50.2"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dsystemduserunitdir=no", "-Dtmpfilesdir=no", "-Dlogind=true",
    "-Dman=true",
    "-Dgoogle=false", # TODO libgdata
]
hostmakedepends = [
    "meson", "pkgconf", "glib-devel", "xsltproc", "openssh", "polkit-devel",
    "docbook-xsl-nons", "gettext-tiny",
]
makedepends = [
    "dbus-devel", "libglib-devel", "fuse-devel", "libarchive-devel",
    "bluez-devel", "libbluray-devel", "libcap-devel", "gcr-devel",
    "libcdio-paranoia-devel", "libgcrypt-devel", "libgphoto2-devel",
    "libgudev-devel", "libsecret-devel", "libxml2-devel", "polkit-devel",
    "udisks-devel", "gsettings-desktop-schemas-devel", "elogind-devel",
    "libusb-devel", "gnome-online-accounts-devel", "libsmbclient-devel",
    "avahi-glib-devel", "libplist-devel", "libimobiledevice-devel",
    "libsoup-devel", "libmtp-devel", "libnfs-devel",
]
# some shared libs that modules depend on
provides = ["so:libgvfscommon.so=0", "so:libgvfsdaemon.so=0"]
pkgdesc = "GNOME virtual file system"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.0-or-later"
url = "https://wiki.gnome.org/Projects/gvfs"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "03d72b8c15ef438110f0cf457b5655266c8b515d0412b30f4d55cfa0da06ac5e"

@subpackage("gvfs-devel")
def _devel(self):
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]

    return self.default_devel()

@subpackage("gvfs-afc")
def _afc(self):
    self.pkgdesc = f"{pkgdesc} (Apple mobile device backend)"
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"]

    return [
        "usr/libexec/gvfsd-afc*",
        "usr/libexec/gvfs-afc-volume-monitor",
        "usr/share/dbus-1/services/org.gtk.vfs.AfcVolumeMonitor.service",
        "usr/share/gvfs/remote-volume-monitors/afc.monitor",
    ]

@subpackage("gvfs-afp")
def _afp(self):
    self.pkgdesc = f"{pkgdesc} (Apple Filing Protocol backend)"
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"]

    return [
        "usr/libexec/gvfsd-afp*",
        "usr/share/gvfs/mounts/afp*",
    ]

@subpackage("gvfs-cdda")
def _afp(self):
    self.pkgdesc = f"{pkgdesc} (CD-ROM backend)"
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"]

    return [
        "usr/libexec/gvfsd-cd*",
        "usr/share/gvfs/mounts/cd*",
    ]

@subpackage("gvfs-goa")
def _afp(self):
    self.pkgdesc = f"{pkgdesc} (Gnome Online Accounts backend)"
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"]

    return [
        "usr/libexec/gvfs-goa*",
        #"usr/libexec/gvfsd-google", TODO: for libgdata
        #"usr/share/gvfs/mounts/google.mount",
        "usr/share/dbus-1/services/org.gtk.vfs.GoaVolumeMonitor.service",
        "usr/share/gvfs/remote-volume-monitors/goa.monitor",
    ]

@subpackage("gvfs-gphoto2")
def _afp(self):
    self.pkgdesc = f"{pkgdesc} (gphoto2 backend)"
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"]

    return [
        "usr/libexec/gvfs*-gphoto*",
        "usr/share/dbus-1/services/org.gtk.vfs.GPhoto2VolumeMonitor.service",
        "usr/share/gvfs/remote-volume-monitors/gphoto2.monitor",
    ]

@subpackage("gvfs-mtp")
def _mtp(self):
    self.pkgdesc = f"{pkgdesc} (MTP backend)"
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"]

    return [
        "usr/libexec/gvfs*-mtp*",
        "usr/share/dbus-1/services/org.gtk.vfs.MTPVolumeMonitor.service",
        "usr/share/gvfs/remote-volume-monitors/mtp.monitor",
        "usr/share/gvfs/mounts/mtp.mount",
    ]

@subpackage("gvfs-smb")
def _smb(self):
    self.pkgdesc = f"{pkgdesc} (SMB/CIFS backend)"
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"]

    return [
        "usr/libexec/gvfs*-smb*",
        "usr/share/GConf/gsettings/gvfs-smb.convert",
        "usr/share/glib-2.0/schemas/org.gnome.system.smb.gschema.xml",
        "usr/share/gvfs/mounts/smb*.mount",
    ]
