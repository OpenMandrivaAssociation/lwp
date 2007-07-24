%define name lwp
%define version 2.2
%define release %mkrel 1
%define major 2

%define libname %mklibname %name %major

Summary: LWP thread library
Name: %{name}
Version: %{version}
Release: %{release}
Source: ftp://ftp.coda.cs.cmu.edu/pub/coda/src/%{name}-%{version}.tar.bz2
Patch0: lwp-1.9-amd64.patch.bz2
License: LGPL
URL:http://www.coda.cs.cmu.edu
BuildRoot: %{_tmppath}/%{name}-buildroot
Group: Development/Other

%description
The LWP userspace threads library. The LWP threads library is used by the Coda
distributed filesystem, RVM (a persistent VM library), and RPC2/SFTP (remote
procedure call library)

%package -n %{libname}
Summary: LWP thread library development files
Group: Development/Other
Obsoletes: %{name}
Provides: %{name}
Provides: lib%{name} = %version-%release

%description -n %{libname}
The LWP userspace threads library. The LWP threads library is used by the Coda
distributed filesystem, RVM (a persistent VM library), and RPC2/SFTP (remote
procedure call library)

%package -n %{libname}-devel
Summary: LWP thread library development files
Group: Development/Other
Requires: %{libname} = %{version}-%{release}
Obsoletes: %{name}-devel
Provides: lib%{name}-devel = %version-%release
Provides: %{name}-devel

%description  -n %{libname}-devel
Headers and static libraries for developing programs using the LWP userspace
threads library. The LWP threads library is used by the Coda distributed
filesystem, RVM (a persistent VM library), and RPC2/SFTP (a remote procedure
call library)

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q
#%patch0 -p1 -b .amd64

%build
%configure2_5x
%make

%install
%makeinstall
chmod 755 $RPM_BUILD_ROOT%{_libdir}/liblwp.so.*

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig -n %{libname}

%postun -p /sbin/ldconfig -n %{libname}

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS COPYING INSTALL NEWS PORTING README
%{_libdir}/liblwp.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%{_libdir}/liblwp.a
%{_libdir}/liblwp.la
%{_libdir}/liblwp.so
%dir %{_includedir}/lwp
%{_includedir}/lwp/lock.h
%{_includedir}/lwp/lwp.h
%{_includedir}/lwp/timer.h
