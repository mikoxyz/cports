pkgname = "dopewars-gtk3"
pkgver = "1.6.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--localstatedir=/var/lib/dopewars", "--without-esd"]
hostmakedepends = [
    "automake",
    "gettext",
    "libtool",
    "pkgconf",
]
makedepends = [
    "glib-devel",
    "gtk+3-devel",
    "libcurl-devel",
    "ncurses-devel",
    "sdl-devel",
]
provides = [f"dopewars={pkgver}"]
provider_priority = 10
pkgdesc = "Game simulating the life of a drug dealer in New York"
maintainer = "miko <mikoxyzzz@gmail.com>"
license = "GPL-2.0-only"
url = "https://dopewars.sourceforge.io"
source = (
    f"https://github.com/benmwebb/dopewars/archive/refs/tags/v{pkgver}.tar.gz"
)
sha256 = "c548a642ff5f8caedf9d1e5b6a1ba66f335087f0fa7e6c8ec8c9ac6b14eac447"
file_modes = {
    "usr/bin/dopewars": ("root", "_dopewars", 0o2755),
    "var/lib/dopewars/dopewars.sco": ("root", "_dopewars", 0o0660),
}
# no tests
options = ["!check"]
system_groups = ["_dopewars"]


def post_install(self):
    self.install_service(self.files_path / "dopewars")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
