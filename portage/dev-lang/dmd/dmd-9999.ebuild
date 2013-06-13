# Copyright 1999-2013 Gentoo Foundation
# Distributed under the terms of the GNU General Public License v2
# $Header: $

EAPI=4

inherit git-2

DESCRIPTION="Reference compiler for the D programming language"
HOMEPAGE="http://dlang.org/"
EGIT_REPO_URI="https://github.com/D-Programming-Language/dmd.git"
SRC_URI=""

LICENSE="GPL"
SLOT="2"
KEYWORDS="~x86 amd64"

DEPEND="sys-apps/findutils
        !dev-lang/dmd-bin:2
        app-arch/unzip"

RDEPEND="${DEPEND}"

PDEPEND="dev-libs/druntime
         dev-libs/phobos"


src_compile() {
	emake -f posix.mak || die "emake failed"
}

src_install() {
	emake INSTALL_DIR="${D}" -f posix.mak install || die "emake install failed"

	cat > dmd.conf << EOF
[Environment]
DFLAGS=-I/usr/include/phobos2 -I/usr/include/druntime/import -L--export-dynamic -L-lrt
EOF
	insinto /etc
	doins dmd.conf

	dobin ${D}bin/dmd

	doman ${D}man/man1/dmd.1
	doman ${D}man/man1/dmd.conf.5
}

