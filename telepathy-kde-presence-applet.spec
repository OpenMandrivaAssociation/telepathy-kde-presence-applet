%define rel 1

Summary:	Plasma applet for managing the user's Telepathy account presence
Name:		telepathy-kde-presence-applet
Version:	0.2.0
Release:	%mkrel %rel
Url:		https://projects.kde.org/projects/playground/network/telepathy/telepathy-presence-applet
Source0:	ftp://ftp.gtlib.cc.gatech.edu/pub/kde/unstable/telepathy-kde/%version/src/%name-%version.tar.bz2
License:	GPLv2+
Group:		Graphical desktop/KDE
BuildRequires:	kdelibs4-devel
Requires:	telepathy-presence-dataengine
Requires:       telepathy-contact-list
# Package rename 
# Added on cauldron for the 0.2 switch (Mageia 2)
Provides:       telepathy-presence-applet = %version-%release
Obsoletes:      telepathy-presence-applet < 0.2.0-0

#Needed for Jabber
Requires: telepathy-gabble
# Spell check support
Requires: iso-codes
# needed by MSN
Suggests: telepathy-butterfly
# various protocol provided by libpurple
Suggests: telepathy-haze
# needed for local XMPP
Suggests: telepathy-salut
# needed for irc
Suggests: telepathy-idle
# needed for voip
Suggests: gstreamer0.10-farsight2


%description
A Plasma applet for managing the user's Telepathy account presence.

%files
%_kde_appsdir/plasma/plasmoids/org.kde.telepathy-presence
%_kde_datadir/kde4/services/plasma-applet-telepathy-presence.desktop

#--------------------------------------------------------------------

%prep
%setup -q 

%build
%cmake_kde4

%install
%makeinstall_std -C build



