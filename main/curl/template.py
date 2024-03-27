pkgname = "curl"
pkgver = "8.7.1"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-optimize",
    "--enable-ipv6",
    "--enable-threaded-resolver",
    "--enable-threads",
    "--with-ca-bundle=/etc/ssl/certs/ca-certificates.crt",
    "--with-libidn2",
    "--with-libpsl",
    "--with-libssh2",
    "--with-nghttp2",
    "--with-nghttp3",
    "--with-openssl-quic",
    "--with-ssl",
    "--with-zlib",
    "--with-zstd",
    "ac_cv_path_NROFF=/usr/bin/mandoc",
    "ac_cv_sizeof_off_t=8",
]
hostmakedepends = ["pkgconf", "perl", "mandoc"]
makedepends = [
    "libidn2-devel",
    "libpsl-devel",
    "libssh2-devel",
    "nghttp2-devel",
    "nghttp3-devel",
    "openssl-devel",
    "zlib-devel",
    "zstd-devel",
]
checkdepends = ["python", "nghttp2"]
depends = ["ca-certificates"]
pkgdesc = "Command line tool for transferring data with URL syntax"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://curl.haxx.se"
source = f"{url}/download/{pkgname}-{pkgver}.tar.xz"
sha256 = "6fea2aac6a4610fbd0400afb0bcddbe7258a64c63f1f68e5855ebc0c659710cd"
# FIXME cfi
hardening = ["vis", "!cfi"]
# missing some checkdepends
options = ["!check"]


def post_install(self):
    self.install_license("COPYING")

    # patch curl-config for cross
    if not self.profile().cross:
        return

    with open(self.destdir / "usr/bin/curl-config") as inf:
        with open(self.destdir / "usr/bin/curl-config.new", "w") as outf:
            for ln in inf:
                ln = ln.replace(f"-L{self.profile().sysroot / 'usr/lib'} ", "")
                ln = ln.replace(f"{self.profile().triplet}-", "")
                outf.write(ln)

    self.rm(self.destdir / "usr/bin/curl-config")
    self.mv(
        self.destdir / "usr/bin/curl-config.new",
        self.destdir / "usr/bin/curl-config",
    )
    self.chmod(self.destdir / "usr/bin/curl-config", 0o755)


@subpackage("libcurl")
def _libcurl(self):
    self.pkgdesc = "Multiprotocol file transfer library"

    return self.default_libs()


@subpackage("libcurl-devel")
def _devel(self):
    self.depends += makedepends
    self.pkgdesc = "Multiprotocol file transfer library (development files)"

    return self.default_devel()


configure_gen = []
