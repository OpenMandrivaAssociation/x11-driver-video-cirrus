Name:		x11-driver-video-cirrus
Version:	1.5.1
Release:	2
Summary:	X.org driver for Cirrus Logic
Group:		System/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-cirrus-%{version}.tar.bz2

BuildRequires:	x11-proto-devel >= 1.0.0
BuildRequires:	x11-server-devel >= 1.0.1
BuildRequires:	x11-util-macros >= 1.0.1
Conflicts:	xorg-x11-server < 7.0

Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)

%description
x11-driver-video-cirrus is the X.org driver for Cirrus Logic.

%prep
%setup -qn xf86-video-cirrus-%{version}

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc COPYING
%{_libdir}/xorg/modules/drivers/cirrus_drv.so
%{_libdir}/xorg/modules/drivers/cirrus_laguna.so
%{_libdir}/xorg/modules/drivers/cirrus_alpine.so
%{_mandir}/man4/cirrus.*
