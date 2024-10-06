# NOTE: due to src2man spawning txt2man process per each man page, requires ulimit -u >= ~768
Summary:	Library to simplify accessing persistent memory on remote hosts over RDMA
Summary(pl.UTF-8):	Biblioteka upraszczająca dostęp do pamięci nieulotnej na maszynach zdalnych po RDMA
Name:		rpma
Version:	1.3.0
Release:	1
License:	BSD
Group:		Libraries
#Source0Download: https://github.com/pmem/rpma/releases
Source0:	https://github.com/pmem/rpma/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	ce62672b43fe8dabd536dfd40132886b
URL:		https://github.com/pmem/rpma
BuildRequires:	cmake >= 3.3
BuildRequires:	cmocka-devel >= 1.1.5
BuildRequires:	libibverbs-devel
BuildRequires:	librdmacm-devel
BuildRequires:	pkgconfig
BuildRequires:	txt2man >= 1.7.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Remote Persistent Memory Access (RPMA) Library is a C library to
simplify accessing persistent memory on remote hosts over Remote
Direct Memory Access (RDMA).

%description -l pl.UTF-8
Biblioteka RPMA (Remote Persistent Memory Access) to biblioteka C
upraszczająca dostęp do pamięci nieulotnej na maszynach zdalnych
poprzez RDMA (Remote Direct Memory Access).

%package devel
Summary:	Header files for RPMA library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki RPMA
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libibverbs-devel
Requires:	librdmacm-devel

%description devel
Header files for RPMA library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki RPMA.

%prep
%setup -q

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_INSTALL_INCLUDEDIR=include \
	-DCMAKE_INSTALL_LIBDIR=%{_lib}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md ROADMAP.md THREAD_SAFETY.md
%attr(755,root,root) %{_libdir}/librpma.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/librpma.so
%{_includedir}/librpma.h
%{_pkgconfigdir}/librpma.pc
%dir %{_libdir}/librpma
%{_libdir}/librpma/cmake
%{_mandir}/man3/rpma_*.3*
%{_mandir}/man7/librpma.7*
