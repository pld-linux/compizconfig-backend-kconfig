Summary:	The kconfig backend for CompizConfig.
Summary(pl.UTF-8):	Backend kconfig dla CompizConfig.
Name:		compizconfig-backend-kconfig
Version:	0.5.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://releases.compiz-fusion.org/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	e95ced3432cc95850f9bfd28013dc70f
Patch0:		%{name}-am.patch
URL:		http://forum.compiz-fusion.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel
BuildRequires:	libcompizconfig-devel >= %{version}
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The kconfig backend for CompizConfig. It uses the KDE configuration
system to store the compiz configuration and provides integration
into the KDE desktop environment.

%description -l pl.UTF-8
Backend kconfig dla CompizConfig. Używa systemu konfiguracji KDE do
przechowywania konfiguracji compiza i zapewnia intergrację ze
środowiskiem KDE.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_libdir}/compizconfig/backends/libkconfig{,.so}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/compizconfig/backends/*.so
