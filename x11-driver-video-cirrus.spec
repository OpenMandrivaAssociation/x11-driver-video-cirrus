Summary:	X.org driver for Cirrus Logic
Name:		x11-driver-video-cirrus
Version:	1.5.3
Release:	6
Group:		System/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-cirrus-%{version}.tar.bz2
BuildRequires:	pkgconfig(xproto)
BuildRequires:	pkgconfig(xorg-server)
BuildRequires:	pkgconfig(xorg-macros)
Requires:	x11-server-common %(xserver-sdk-abi-requires videodrv)

%description
x11-driver-video-cirrus is the X.org driver for Cirrus Logic.

%prep
%setup -qn xf86-video-cirrus-%{version}
%apply_patches
autoreconf -fiv

%build
%configure
%make

%install
%makeinstall_std

%files
%doc COPYING
%{_libdir}/xorg/modules/drivers/cirrus_drv.so
%{_libdir}/xorg/modules/drivers/cirrus_laguna.so
%{_libdir}/xorg/modules/drivers/cirrus_alpine.so
%{_mandir}/man4/cirrus.*
