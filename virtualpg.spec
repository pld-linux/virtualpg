Summary:	VirtualPostgres driver for SQLite DBMS
Summary(pl.UTF-8):	Sterownik VirtualPostgres dla systemu baz danych SQLite
Name:		virtualpg
Version:	1.0.1
Release:	1
License:	MPL v1.1 or GPL v2+ or LGPL v2.1+
Group:		Libraries
Source0:	http://www.gaia-gis.it/gaia-sins/virtualpg-sources/%{name}-%{version}.tar.gz
# Source0-md5:	17a02d93e6a089083cb884553c90a7c8
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

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/mod_virtualpg.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libdir}/mod_virtualpg.so*
