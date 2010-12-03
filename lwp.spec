%define name lwp
%define version 2.5
%define release %mkrel 5
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
rm -rf $RPM_BUILD_ROOT
%makeinstall
chmod 755 $RPM_BUILD_ROOT%{_libdir}/liblwp.so.*

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -p /sbin/ldconfig -n %{libname}
%endif

%if %mdkversion < 200900
%postun -p /sbin/ldconfig -n %{libname}
%endif

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/liblwp.so.*

%files -n %{develname}
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS PORTING README
%{_libdir}/liblwp.a
%{_libdir}/liblwp.la
%{_libdir}/liblwp.so
%dir %{_includedir}/lwp
%{_includedir}/lwp/lock.h
%{_includedir}/lwp/lwp.h
%{_includedir}/lwp/timer.h
%{_libdir}/pkgconfig/lwp.pc
