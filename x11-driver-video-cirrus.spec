Summary:	X.org driver for Cirrus Logic
Name:		x11-driver-video-cirrus
Version:	1.6.0
Release:	2
Group:		System/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-cirrus-%{version}.tar.xz
BuildRequires:	pkgconfig(xproto)
BuildRequires:	pkgconfig(xorg-server)
BuildRequires:	pkgconfig(xorg-macros)
Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)

%description
x11-driver-video-cirrus is the X.org driver for Cirrus Logic.

%prep
%setup -qn xf86-video-cirrus-%{version}
%autopatch -p1
autoreconf -fiv

%build
%configure
%make_build

%install
%make_install

%files
%doc COPYING
%{_libdir}/xorg/modules/drivers/cirrus_drv.so
%{_mandir}/man4/cirrus.*
