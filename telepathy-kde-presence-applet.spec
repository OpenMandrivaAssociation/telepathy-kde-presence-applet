%define srcname ktp-presence-applet

Summary:	Plasma applet for managing the user's Telepathy account presence
Name:		telepathy-kde-presence-applet
Version:	0.5.1
Release:	2
Url:		https://projects.kde.org/projects/playground/network/telepathy/telepathy-presence-applet
Source0:	ftp://ftp.gtlib.cc.gatech.edu/pub/kde/unstable/telepathy-kde/%version/src/%srcname-%version.tar.bz2
License:	GPLv2+
Group:		Networking/Instant messaging

BuildRequires:	telepathy-kde-common-internals-devel >= %{version}
Requires:	telepathy-kde-contact-list
Suggests:	telepathy-kde-contact-applet
# Package rename 
# Added on cauldron for the 0.2 switch (Mageia 2)
Obsoletes:	telepathy-presence-applet < 0.2.0-0
# Telepathy kde presence dataengine is not ported to telepathy qt 0.9 for the 0.3 releas
# so i'm obsoleting it in the presence applet
Obsoletes:	telepathy-kde-presence-dataengine < 0.3.0-0

%description
A Plasma applet for managing the user's
Telepathy account presence.

%files -f plasma_applet_ktp_presence.lang
%_kde_libdir/kde4/plasma_applet_ktp_presence.so
%_kde_datadir/kde4/services/plasma_applet_ktp_presence.desktop

#--------------------------------------------------------------------

%prep
%setup -q -n %{srcname}-%{version}
%autopatch -p1

%build
%cmake_kde4

%install
%makeinstall_std -C build
%find_lang plasma_applet_ktp_presence
