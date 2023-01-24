Summary:	VirtualPostgres driver for SQLite DBMS
Summary(pl.UTF-8):	Sterownik VirtualPostgres dla systemu baz danych SQLite
Name:		virtualpg
Version:	2.0.1
Release:	1
License:	MPL v1.1 or GPL v2+ or LGPL v2.1+
Group:		Libraries
Source0:	http://www.gaia-gis.it/gaia-sins/virtualpg-sources/%{name}-%{version}.tar.gz
# Source0-md5:	c90fc631ba99a64a6f225b31172d6b5d
URL:		https://www.gaia-gis.it/fossil/virtualpg
BuildRequires:	postgresql-devel
BuildRequires:	sqlite3-devel >= 3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
virtualpg is a dynamic extension for the SQLite DBMS. It implements
the VirtualPostgres driver, allowing to directly exchange data between
SQLite and PostgreSQL; if SpatiaLite is available even PostGIS
geometries can ben exchanged from one Spatial DBMS and the other.

%description -l pl.UTF-8
virtualpg to dynamiczne rozszerzenie dla systemu baz danych SQLite.
Implementuje sterownik VirtualPostgres, pozwalający bezpośrednio
wymieniać dane między bazami SQLite a PostgreSQL; jeśli dostępne jest
SpatiaLite, można wymieniać także geometrie PostGIS-a.

%package devel
Summary:	Header file for VirtualPG library
Summary(pl.UTF-8):	Plik nagłówkowy biblioteki VirtualPG
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	postgresql-devel

%description devel
Header file for VirtualPG library.

%description devel -l pl.UTF-8
Plik nagłówkowy biblioteki VirtualPG.

%package static
Summary:	Static VirtualPG library
Summary(pl.UTF-8):	Statyczna biblioteka VirtualPG
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static VirtualPG library.

%description static -l pl.UTF-8
Statyczna biblioteka VirtualPG.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libvirtualpg.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/mod_virtualpg.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/libvirtualpg.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvirtualpg.so.0
%attr(755,root,root) %{_libdir}/mod_virtualpg.so*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvirtualpg.so
%{_includedir}/virtualpg.h
%{_pkgconfigdir}/virtualpg.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libvirtualpg.a
