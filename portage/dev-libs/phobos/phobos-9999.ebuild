# Copyright 1999-2013 Gentoo Foundation
# Distributed under the terms of the GNU General Public License v2
# $Header: $

EAPI=4

inherit git-2 eutils

DESCRIPTION="The standard library of the D programming language"
HOMEPAGE="http://dlang.org/"
EGIT_REPO_URI="https://github.com/D-Programming-Language/phobos.git"
SRC_URI=""

LICENSE="GPL"
SLOT="2"
KEYWORDS="~x86 amd64"

PDEPEND="dev-lang/dmd
         dev-libs/druntime"

src_prepare() {
	cd "${S}"
	epatch "${FILESDIR}"/phobos-9999.patch
}

src_compile() {
	DMD="/usr/bin/dmd" emake DRUNTIME_PATH="/usr/include/druntime/" -f posix.mak || die "emake failed"
}

src_install() {
	dolib.a "${S}/generated/linux/release/default/libphobos2.a"

	dodir /usr/include/phobos2
	dodir /usr/include/phobos2/std
	cp "${S}"/*.d "${D}/usr/include/phobos2/"
	cp -R "${S}"/std/ "${D}/usr/include/phobos2/"
}

