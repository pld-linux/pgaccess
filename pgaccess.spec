Summary:	A free graphical database management tool for PostgreSQL
Summary(pl.UTF-8):	Graficzne narzędzie do obsługi baz danych PostgreSQL
Name:		pgaccess
Version:	0.99.0.20040219
%define	fver	%(echo %{version} | tr . _)
Release:	3
Epoch:		1
License:	BSD
Group:		Applications/Databases
Source0:	http://dl.sourceforge.net/pgaccess/%{name}-%{fver}.tgz
# Source0-md5:	5440a130da909368a7274ac6f4578039
Source1:	pgaccess.desktop
Source2:	pgaccess.png
Patch0:		%{name}-path.patch
Patch1:		%{name}-soname-workaround.patch
URL:		http://www.pgaccess.org/
Requires:	tcl-libpgtcl
Requires:	tcl >= 8.3
Requires:	tk >= 8.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A free graphical database management tool for PostgreSQL.

%description -l pl.UTF-8
Graficzne narzędzie do obsługi baz danych PostgreSQL.

%prep
%setup -q -n %{name}-%{fver}
%patch0 -p1
%patch1 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/pgaccess} \
	$RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

cp -Rf extra images lib pgaccess.tcl pgmonitor $RPM_BUILD_ROOT%{_datadir}/pgaccess
ln -sf %{_datadir}/pgaccess/pgaccess.tcl $RPM_BUILD_ROOT%{_bindir}/pgaccess

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
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
%{_desktopdir}/pgaccess.desktop
%{_pixmapsdir}/pgaccess.png
