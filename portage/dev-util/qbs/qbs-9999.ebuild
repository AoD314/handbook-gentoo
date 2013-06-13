# Copyright 1999-2012 Gentoo Foundation
# Distributed under the terms of the GNU General Public License v2
# $Header: $

EAPI=4

EGIT_REPO_URI="git://gitorious.org/qt-labs/qbs.git"

inherit qt4-r2 git-2

DESCRIPTION="Qt Build System"
HOMEPAGE="http://qt.gitorious.org/qt-labs/qbs"
SRC_URI=""

LICENSE="LGPL-2.1"
SLOT="0"
KEYWORDS=""
IUSE=""

DEPEND="
	dev-qt/qtcore
	dev-qt/qtscript"
RDEPEND="${DEPEND}"

src_install(){
	dobin bin/qbs*
	insinto /usr
	doins -r share plugins
	dodoc -r doc
}

pkg_postinst() {
	einfo "Remember to run 'qbs platforms probe' before using qbs for the first time"
}
