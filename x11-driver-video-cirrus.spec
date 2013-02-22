Name:		x11-driver-video-cirrus
Version:	1.5.1
Release:	3
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
autoreconf -fiv

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

%changelog
* Mon Jul 23 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.5.1-1
+ Revision: 810714
- version update 1.5.1

* Fri Jul 06 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.5.0-1
+ Revision: 808297
- version update 1.5.0

* Tue Mar 27 2012 Bernhard Rosenkraenzer <bero@bero.eu> 1.4.0-2
+ Revision: 787196
- Build for x11-server 1.12

* Sun Mar 25 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.4.0-1
+ Revision: 786707
- version update 1.4.0

* Sat Dec 31 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.3.2-7
+ Revision: 748387
- rebuild cleaned up spec

* Sat Oct 08 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1.3.2-6
+ Revision: 703687
- rebuild for new x11-server

* Thu Jun 09 2011 Eugeni Dodonov <eugeni@mandriva.com> 1.3.2-5
+ Revision: 683790
- Rebuild for new x11-server

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3.2-4
+ Revision: 671143
- mass rebuild

* Wed Nov 10 2010 Thierry Vignaud <tv@mandriva.org> 1.3.2-3mdv2011.0
+ Revision: 595738
- require xorg server with proper ABI

* Sun Oct 10 2010 Thierry Vignaud <tv@mandriva.org> 1.3.2-2mdv2011.0
+ Revision: 584626
- bump release before rebuilding for xserver 1.9

* Thu Jul 30 2009 Frederik Himpe <fhimpe@mandriva.org> 1.3.2-1mdv2010.0
+ Revision: 404801
- update to new version 1.3.2

* Fri Jul 03 2009 Ander Conselvan de Oliveira <ander@mandriva.com> 1.3.1-1mdv2010.0
+ Revision: 391880
- update to version 1.3.1

* Thu May 07 2009 Ander Conselvan de Oliveira <ander@mandriva.com> 1.3.0-1mdv2010.0
+ Revision: 372970
- New version 1.3.0

* Tue Dec 30 2008 Colin Guthrie <cguthrie@mandriva.org> 1.2.1-4mdv2009.1
+ Revision: 321381
- Rebuild for new xserver

* Sat Nov 29 2008 Adam Williamson <awilliamson@mandriva.org> 1.2.1-3mdv2009.1
+ Revision: 308165
- rebuild for new X server

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.2.1-2mdv2009.0
+ Revision: 265904
- rebuild early 2009.0 package (before pixel changes)
- improved description
- fix group
- add missing dot at end of description
- improved summary

* Tue May 27 2008 Colin Guthrie <cguthrie@mandriva.org> 1.2.1-1mdv2009.0
+ Revision: 211781
- New version

* Tue Apr 15 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.2.0-1mdv2009.0
+ Revision: 194211
- Update to version 1.2.0.

* Mon Feb 11 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.1.0-9mdv2008.1
+ Revision: 165531
- Revert to use upstream tarball and remove local patches.

* Tue Jan 22 2008 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.1.0-8mdv2008.1
+ Revision: 156601
- re-enable rpm debug packages support

* Fri Jan 18 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.1.0-7mdv2008.1
+ Revision: 154869
- Updated BuildRequires and resubmit package.
- Remove -devel package as it isn't really required as it provides only 2 files
  that aren't even header files; still don't install the .la files.
  All dependency files should be stored in the x11-util-modular package as they
  are only required for the "modular" build.
  Also fix typo in @mandriva tag versioning 1.1.1, as the package version
  is really 1.1.0.
- Move .la files to new -devel package, and also add .deps files to -devel package.
- Note local tag xf86-video-cirrus-1.1.1@mandriva suggested on upstream
  Tag at git checkout 6d114041dc22763aa89ef6a4f4af3246de3e3b1b
- Update for new policy of hidden symbols and common macros.
- Noop patch as at first all modules will have public symbols. But this patch
  makes sure the symbols used by different modules are being explicitly exported.

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 15 2007 Ademar de Souza Reis Jr <ademar@mandriva.com.br> 1.1.0-5mdv2008.1
+ Revision: 98688
- minor spec cleanup
- build against new xserver (1.4)

* Wed Sep 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.1.0-4mdv2008.0
+ Revision: 90358
- rebuild

* Thu Aug 30 2007 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-3mdv2008.0
+ Revision: 75756
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - fix man pages

