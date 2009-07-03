Name: x11-driver-video-cirrus
Version: 1.3.1
Release: %mkrel 1
Summary: X.org driver for Cirrus Logic
Group: System/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/driver/xf86-video-cirrus-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1
Conflicts: xorg-x11-server < 7.0

%description
x11-driver-video-cirrus is the X.org driver for Cirrus Logic.

%prep
%setup -q -n xf86-video-cirrus-%{version}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING
%{_libdir}/xorg/modules/drivers/cirrus_drv.la
%{_libdir}/xorg/modules/drivers/cirrus_drv.so
%{_libdir}/xorg/modules/drivers/cirrus_laguna.la
%{_libdir}/xorg/modules/drivers/cirrus_laguna.so
%{_libdir}/xorg/modules/drivers/cirrus_alpine.la
%{_libdir}/xorg/modules/drivers/cirrus_alpine.so
%{_mandir}/man4/cirrus.*
