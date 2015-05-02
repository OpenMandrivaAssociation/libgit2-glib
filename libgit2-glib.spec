%define major	0
%define api	1.0
%define libname	%mklibname git2-glib %{api} %{major}
%define devname	%mklibname -d git2-glib %{api}

%define url_ver	%(echo %{version} | cut -d. -f1,2)

Name:		libgit2-glib
Version:	0.0.24
Release:	%mkrel 1
Summary:	Git library for GLib
Group:		System/Libraries
License:	LGPLv2+
URL:		https://wiki.gnome.org/Libgit2-glib
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(libgit2)
BuildRequires:	pkgconfig(python3)
BuildRequires:	python3-gobject3
# (tv) for autoconf:
BuildRequires:	gnome-common
# Depend on python3-gobject for the python3 gi overrides directory.
# If we ever get a libgit2-glib consumer that does not depend on python3,
# it would probably make sense to split it to a separate subpackage.
Requires:	python3-gobject3

%description
libgit2-glib is a glib wrapper library around the libgit2 git access library.

%package -n %{libname}
Summary:	A glib wrapper library around the libgit2 git access library
Group:		System/Libraries

%description -n %{libname}
libgit2-glib is a glib wrapper library around the libgit2 git access library.


%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	%{_lib}%{name}-devel = %{version}-%{release}

%description -n %{devname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
autoreconf -vfi
%configure2_5x --disable-static
%make

%install
%makeinstall_std

# Remove unwanted la files
find %{buildroot} -name "*.la" -delete

%files -n %{libname}
%doc AUTHORS NEWS
%{_libdir}/libgit2-glib-%{api}.so.%{major}
%{_libdir}/libgit2-glib-%{api}.so.%{major}.*
%{_libdir}/girepository-1.0/Ggit-1.0.typelib
#%{python3_sitearch}/gi/overrides/*

%files -n %{devname}
%doc %{_datadir}/gtk-doc/
%{_includedir}/libgit2-glib-%{api}/
%{_libdir}/libgit2-glib-%{api}.so
%{_libdir}/pkgconfig/libgit2-glib-%{api}.pc
%{_datadir}/gir-1.0/Ggit-1.0.gir


%changelog
* Tue Nov 04 2014 ovitters <ovitters> 0.0.24-1.mga5
+ Revision: 795556
- new version 0.0.24

* Wed Oct 15 2014 umeabot <umeabot> 0.0.22-4.mga5
+ Revision: 746774
- Second Mageia 5 Mass Rebuild

* Tue Sep 16 2014 umeabot <umeabot> 0.0.22-3.mga5
+ Revision: 686709
- Rebuild to fix library dependencies
- Mageia 5 Mass Rebuild

* Tue Sep 16 2014 ovitters <ovitters> 0.0.22-1.mga5
+ Revision: 676965
- new version 0.0.22

* Thu Jul 24 2014 ovitters <ovitters> 0.0.20-1.mga5
+ Revision: 656358
- new version 0.0.20

* Mon Jun 30 2014 ovitters <ovitters> 0.0.18-1.mga5
+ Revision: 641585
- new version 0.0.18

* Sun Jun 22 2014 ovitters <ovitters> 0.0.16-1.mga5
+ Revision: 638752
- new version 0.0.16

* Sun Jun 22 2014 ovitters <ovitters> 0.0.14-1.mga5
+ Revision: 638699
- new version 0.0.14

* Sun Jun 15 2014 ovitters <ovitters> 0.0.12-2.mga5
+ Revision: 636453
- fix url

* Wed Mar 05 2014 ovitters <ovitters> 0.0.12-1.mga5
+ Revision: 599905
- new version 0.0.12

* Sat Mar 01 2014 wally <wally> 0.0.10-2.mga5
+ Revision: 598195
- drop unneeded python3-gobject3-devel BR
- convert BRs to pkgconfig style

* Tue Feb 04 2014 wally <wally> 0.0.10-1.mga5
+ Revision: 582101
- clean .spec

* Fri Jan 10 2014 tv <tv> 0.0.10-1.mga4
+ Revision: 566134
- imported package libgit2-glib


* Fri Jan 10 2014 Thierry Vignaud <tv@mageia.org> 0.0.10-1.mga4
- initial release
