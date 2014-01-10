# Copyright 1999-2013 Gentoo Foundation
# Distributed under the terms of the GNU General Public License v2
# $Header: /var/cvsroot/gentoo-x86/dev-util/ninja/ninja-1.3.3.ebuild,v 1.1 2013/05/28 03:51:35 floppym Exp $

EAPI=5

PYTHON_COMPAT=( python2_7 )

inherit bash-completion-r1 python-any-r1 toolchain-funcs git-2

EGIT_REPO_URI="git://github.com/martine/ninja.git http://github.com/martine/ninja.git"
KEYWORDS="~amd64 ~arm ~x86"

DESCRIPTION="A small build system similar to make."
HOMEPAGE="http://github.com/martine/ninja"

LICENSE="Apache-2.0"
SLOT="0"

IUSE=""

DEPEND="${PYTHON_DEPS}
        dev-util/re2c"

RDEPEND="!<net-irc/ninja-1.5.9_pre14-r1"

src_compile() {
	# If somebody wants to cross-compile, we will probably need to do 2 builds.
	tc-export CXX

	"${PYTHON}" bootstrap.py --verbose || die
}

src_install() {
	dodoc README HACKING.md
	dobin ninja

	newbashcomp misc/bash-completion "${PN}"
}

