pkgname = "guile"
pkgver = "3.0.9"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--disable-static"]
make_cmd = "gmake"
make_dir = "."
hostmakedepends = [
    "automake",
    "gettext-devel",
    "gmake",
    "gperf",
    "libtool",
    "pkgconf",
]
makedepends = [
    "gc-devel",
    "gmp-devel",
    "libffi-devel",
    "libunistring-devel",
    "readline-devel",
]
pkgdesc = "GNU implementation of the Scheme programming language"
maintainer = "miko <mikoxyzzz@gmail.com>"
license = "GPL-3.0-or-later AND LGPL-3.0-or-later"
url = "https://www.gnu.org/software/guile"
source = f"$(GNU_SITE)/guile/guile-{pkgver}.tar.gz"
sha256 = "18525079ad29a0d46d15c76581b5d91c8702301bfd821666d2e1d13726162811"


def do_prepare(self):
    for t in [
        "encoding-escapes.test",
        "encoding-iso88597.test",
        "i18n.test",
        "iconv.test",
        "r6rs-ports.test",
        "suspendable-ports.test",
        "time.test",
    ]:
        self.rm(f"test-suite/tests/{t}")

    self.do("find", ".", "-type", "d", "-exec", "chmod", "g-s", "{}", ";")
