Summary:	The kconfig backend for CompizConfig
Summary(pl.UTF-8):	Backend kconfig dla CompizConfiga
Name:		compizconfig-backend-kconfig
Version:	0.8.4
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://releases.compiz.org/%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	a96a30aba5e5faf7aa7db440fe4891ca
URL:		http://www.compiz.org/
Patch0:		%{name}-am.patch
Patch1:		kde-ac260-lt.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kde4-kde3support-devel
BuildRequires:	libcompizconfig-devel >= %{version}
BuildRequires:	pkgconfig
BuildRequires:	qt-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The kconfig backend for CompizConfig. It uses the KDE configuration
system to store the compiz configuration and provides integration into
the KDE desktop environment.

%description -l pl.UTF-8
Backend kconfig dla CompizConfiga. Używa systemu konfiguracji KDE do
przechowywania konfiguracji compiza i zapewnia integrację ze
środowiskiem KDE.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--includedir=%{_includedir}/kde3
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/compizconfig/backends/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/compizconfig/backends/libkconfig.so
