Summary:	Control paper size in applications
Summary(pl.UTF-8):	Zarządzanie rozmiarem papieru w aplikacjach
Name:		libpaper
Version:	1.1.21
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://ftp.debian.org/debian/pool/main/libp/libpaper/%{name}_%{version}.tar.gz
# Source0-md5:	6397f8d60a157119c1de5d19e4d82436
URL:		http://packages.debian.org/unstable/source/libpaper
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 1.316
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libpaper and accompanying files are intended to provide a simple way
for applications to take actions based on a system- or user-specified
paper size.

%description -l pl.UTF-8
libpaper wraz z towarzyszącymi plikami pozwalają aplikacjom w prosty
sposób podejmować akcje oparte na określonym przez system lub
użytkownika rozmiarze papieru.

%package devel
Summary:	Header files for libpaper library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libpaper
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libpaper library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libpaper.

%package static
Summary:	Static libpaper library
Summary(pl.UTF-8):	Statyczna biblioteka libpaper
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libpaper library.

%description static -l pl.UTF-8
Statyczna biblioteka libpaper.

%prep
%setup -q

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
install -d $RPM_BUILD_ROOT/etc/env.d

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

echo 'a4' > $RPM_BUILD_ROOT/etc/papersize
echo '#PAPERSIZE=a4' > $RPM_BUILD_ROOT/etc/env.d/PAPERSIZE

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%env_update

%postun	-p /sbin/ldconfig
%env_update

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%config(noreplace,missingok) %verify(not md5 mtime size) /etc/env.d/*
%config(noreplace,missingok) %verify(not md5 mtime size) /etc/papersize
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_mandir}/man[1358]/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/paper.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
