# Copyright 1999-2013 Gentoo Foundation
# Distributed under the terms of the GNU General Public License v2
# $Header: $

EAPI=4

inherit git-2

DESCRIPTION="Low level runtime library for the D programming language"
HOMEPAGE="http://dlang.org/"
EGIT_REPO_URI="https://github.com/D-Programming-Language/druntime.git"
SRC_URI=""

LICENSE="GPL"
SLOT="2"
KEYWORDS="~x86 amd64"

DEPEND="dev-lang/dmd"

RDEPEND="${DEPEND}"

src_compile() {
	emake -f posix.mak || die "emake failed"
}

src_install() {
	dolib "${S}/lib/libdruntime-linuxdefault.a" || die "Install failed"
	dolib "${S}/lib/libdruntime-linuxdefaultso.a" || die "Install failed"

	dodir /usr/include/druntime/import/
	mv "${S}/import"/* "${D}/usr/include/druntime/import" || die "Install failed"
}

