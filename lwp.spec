%define major 2
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:	LWP thread library
Name:		lwp
Version:	2.8
Release:	2
License:	LGPLv2
Group:		Development/Other
Url:		http://www.coda.cs.cmu.edu
Source0:	ftp://ftp.coda.cs.cmu.edu/pub/coda/src/%{name}-%{version}.tar.gz
Buildrequires:	gzip

%description
The LWP userspace threads library. The LWP threads library is used by the Coda
distributed filesystem, RVM (a persistent VM library), and RPC2/SFTP (remote
procedure call library).

%package -n %{libname}
Summary:	LWP thread library development files
Group:		Development/Other
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
The LWP userspace threads library. The LWP threads library is used by the Coda
distributed filesystem, RVM (a persistent VM library), and RPC2/SFTP (remote
procedure call library).

%package -n %{devname}
Summary:	LWP thread library development files
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description  -n %{devname}
This package includes the development files for %{name}.

%prep
%setup -q

%build
%configure --disable-static
%make

%install
%makeinstall
chmod 755 %{buildroot}%{_libdir}/liblwp.so.*

%files -n %{libname}
%{_libdir}/liblwp.so.%{major}*

%files -n %{devname}
%doc AUTHORS COPYING NEWS PORTING README
%{_libdir}/liblwp.so
%dir %{_includedir}/lwp
%{_includedir}/lwp/lock.h
%{_includedir}/lwp/lwp.h
%{_includedir}/lwp/timer.h
%{_libdir}/pkgconfig/lwp.pc

