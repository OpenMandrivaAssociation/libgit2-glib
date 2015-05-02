%define major	0
%define api	1.0
%define libname	%mklibname git2-glib %{api} %{major}
%define devname	%mklibname -d git2-glib %{api}

%define url_ver	%(echo %{version} | cut -d. -f1,2)

Name:		libgit2-glib
Version:	0.22.8
Release:	1
Summary:	Git library for GLib
Group:		System/Libraries
License:	LGPLv2+
URL:		https://wiki.gnome.org/Libgit2-glib
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(libgit2)
BuildRequires:	pkgconfig(python3)
BuildRequires:	python-gi
# (tv) for autoconf:
BuildRequires:	gnome-common
# Depend on python3-gobject for the python3 gi overrides directory.
# If we ever get a libgit2-glib consumer that does not depend on python3,
# it would probably make sense to split it to a separate subpackage.
Requires:	python-gi

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
%configure
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
%{python3_sitearch}/gi/overrides/*

%files -n %{devname}
%doc %{_datadir}/gtk-doc/
%{_includedir}/libgit2-glib-%{api}/
%{_libdir}/libgit2-glib-%{api}.so
%{_libdir}/pkgconfig/libgit2-glib-%{api}.pc
%{_datadir}/gir-1.0/Ggit-1.0.gir

