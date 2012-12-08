%define name lwp
%define version 2.5
%define release %mkrel 6
%define major 2

%define libname %mklibname %name %major
%define develname %mklibname %name -d

Summary: LWP thread library
Name: %{name}
Version: %{version}
Release: %{release}
License: LGPLv2
Source: ftp://ftp.coda.cs.cmu.edu/pub/coda/src/%{name}-%{version}.tar.gz
URL: http://www.coda.cs.cmu.edu
Group: Development/Other
BuildRoot: %{_tmppath}/%{name}-%{version}
Buildrequires: gzip

%description
The LWP userspace threads library. The LWP threads library is used by the Coda
distributed filesystem, RVM (a persistent VM library), and RPC2/SFTP (remote
procedure call library).

%package -n %{libname}
Summary: LWP thread library development files
Group: Development/Other
Obsoletes: %{name}
Provides: %{name}
Provides: lib%{name} = %version-%release

%description -n %{libname}
The LWP userspace threads library. The LWP threads library is used by the Coda
distributed filesystem, RVM (a persistent VM library), and RPC2/SFTP (remote
procedure call library).

%package -n %{develname}
Summary: LWP thread library development files
Group: Development/Other
Requires: %{libname} = %{version}-%{release}
Obsoletes: %{name}-devel
Provides: lib%{name}-devel = %version-%release
Provides: %{name}-devel
Obsoletes: %{mklibname lwp 2 -d}

%description  -n %{develname}
Headers and static libraries for developing programs using the LWP userspace
threads library. The LWP threads library is used by the Coda distributed
filesystem, RVM (a persistent VM library), and RPC2/SFTP (a remote procedure
call library).

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall
chmod 755 %{buildroot}%{_libdir}/liblwp.so.*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/liblwp.so.*

%files -n %{develname}
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS PORTING README
%{_libdir}/liblwp.a
%{_libdir}/liblwp.so
%dir %{_includedir}/lwp
%{_includedir}/lwp/lock.h
%{_includedir}/lwp/lwp.h
%{_includedir}/lwp/timer.h
%{_libdir}/pkgconfig/lwp.pc


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 2.5-6mdv2011.0
+ Revision: 666108
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 2.5-5mdv2011.0
+ Revision: 606435
- rebuild

* Wed Jan 27 2010 Antoine Ginies <aginies@mandriva.com> 2.5-4mdv2010.1
+ Revision: 497087
- try to fix strange bug on BS (missing gunzip tool...)
- bump the release

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 2.5-2mdv2010.0
+ Revision: 426019
- rebuild

* Thu Mar 05 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.5-1mdv2009.1
+ Revision: 349361
- new version

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 2.3-4mdv2009.0
+ Revision: 223134
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 2.3-3mdv2008.1
+ Revision: 152886
- rebuild
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Jul 25 2007 Adam Williamson <awilliamson@mandriva.org> 2.3-1mdv2008.0
+ Revision: 55107
- rebuild for 2008
- new devel policy
- spec clean
- new release 2.3
- Import lwp



* Tue Aug  8 2006 Antoine Ginies <aginies@mandriva.com> 2.2-1mdv2007.0
- 2.2
- use mkrel

* Thu Feb 16 2006 Antoine Ginies <aginies@mandriva.com> 2.1-1mdk
- 2.1
- remove uneeded patch (amd64)

* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 1.9-6mdk
- Rebuild

* Sun Jun 05 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.9-5mdk
- Rebuild

* Fri Sep 26 2003 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.9-4mdk
- amd64 support

* Sun May 04 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.8-3mdk
- rebuild for rpm 4.2
- use %%mklibname

* Mon Nov 12 2001 Florin <florin@mandrakesoft.com> 1.8-2mdk
- 1.9
- lose the ChangeLog file

* Fri Aug 10 2001 Florin <florin@mandrakesoft.com> 1.8-1mdk
- 1.8

* Tue Jun 12 2001 Stefan van der Eijk <stefan@eijk.nu> 1.7-1mdk
- 1.7
- add Provides

* Mon Jan 08 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.5-3mdk
- fixes source tag

* Tue Nov 21 2000 Florin Grad <florin@mandrakesoft.com> 1.5-2mdk
- for some reason the srpm package was deleted

* Wed Nov 16 2000 Florin Grad <florin@mandrakesoft.com> 1.5-1mdk
- 1.5 
- added the pt files (different from the standard packages)
- lib split compliant

* Mon Sep 11 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.4-3mdk
- macros

* Tue Aug 29 2000 Florin Grad <florin@mandrakesoft.com> 1.4-2mdk
- udating the macros

* Fri Jul 7 2000 Florin Grad <florin@mandrakesoft.com> 1.4-1mdk
- First attempt.
