Summary:	A free graphical database management tool for PostgreSQL
Summary(pl):	Graficzne narzêdzie do obs³ugi baz danych PostgreSQL
Name:		pgaccess
Version:	0.98.8
Release:	2
Epoch:		1
License:	BSD
Group:		Applications/Databases
Source0:	http://www.pgaccess.org/download/%{name}-%{version}.tar.gz
# Source0-md5:	5f24281f206369d6bc9623a11ec325ab
Source1:	pgaccess.desktop
Source2:	pgaccess.png
Patch0:		%{name}-path.patch
Patch1:		%{name}-soname-workaround.patch
URL:		http://www.pgaccess.org/
Requires:	postgresql-tcl >= 7.3
Requires:	tcl >= 8.3
Requires:	tk >= 8.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A free graphical database management tool for PostgreSQL.

%description -l pl
Graficzne narzêdzie do obs³ugi baz danych PostgreSQL.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/pgaccess} \
	$RPM_BUILD_ROOT{%{_applnkdir}/System,%{_pixmapsdir}}

cp -Rf extra images lib pgaccess.tcl pgmonitor $RPM_BUILD_ROOT%{_datadir}/pgaccess
ln -sf %{_datadir}/pgaccess/pgaccess.tcl $RPM_BUILD_ROOT%{_bindir}/pgaccess

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/System
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README changelog copyright known_bugs todo demo doc/html
%attr(755,root,root) %{_bindir}/pgaccess
%dir %{_datadir}/pgaccess
%attr(755,root,root) %{_datadir}/pgaccess/pgaccess.tcl
%attr(755,root,root) %{_datadir}/pgaccess/pgmonitor
%{_datadir}/pgaccess/extra
%{_datadir}/pgaccess/images
%{_datadir}/pgaccess/lib
%{_applnkdir}/System/pgaccess.desktop
%{_pixmapsdir}/pgaccess.png
