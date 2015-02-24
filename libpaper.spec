Summary:	Control paper size in applications
Summary(pl.UTF-8):	Zarządzanie rozmiarem papieru w aplikacjach
Name:		libpaper
Version:	1.1.24
Release:	2
License:	GPL v2+
Group:		Libraries
Source0:	http://ftp.debian.org/debian/pool/main/libp/libpaper/%{name}_%{version}.tar.gz
# Source0-md5:	5bc87d494ba470aba54f6d2d51471834
URL:		http://packages.debian.org/unstable/source/libpaper
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 1.316
Requires(post,postun):	/sbin/ldconfig
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

echo 'a4' > $RPM_BUILD_ROOT%{_sysconfdir}/papersize
echo '#PAPERSIZE=a4' > $RPM_BUILD_ROOT/etc/env.d/PAPERSIZE

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%env_update

%postun
/sbin/ldconfig
%env_update

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%config(noreplace,missingok) %verify(not md5 mtime size) /etc/env.d/*
%config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/papersize
%attr(755,root,root) %{_bindir}/paperconf
%attr(755,root,root) %{_sbindir}/paperconfig
%attr(755,root,root) %{_libdir}/libpaper.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpaper.so.1
%{_mandir}/man1/paperconf.1*
%{_mandir}/man5/papersize.5*
%{_mandir}/man8/paperconfig.8*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpaper.so
%{_libdir}/libpaper.la
%{_includedir}/paper.h
%{_mandir}/man3/defaultpaper*.3*
%{_mandir}/man3/paper*.3*
%{_mandir}/man3/systempaper*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libpaper.a
