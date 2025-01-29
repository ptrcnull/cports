pkgname = "gaypaste"
pkgver = "1.2.1"
pkgrel = 0
build_style = "go"
hostmakedepends = ["go"]
pkgdesc = "Paste"
maintainer = "Patrycja Rosa <chimera@ptrcnull.me>"
license = "BSD-2-Clause"
url = "https://git.ddd.rip/ptrcnull/gaypaste"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "ad81a9976e0601cb4dadcbc28c5cbe41ba8587f4753fd4e1712d5a5d4c6e7312"
# there are no tests lol
options = ["!check"]

def post_install(self):
    self.install_license("LICENCE")
