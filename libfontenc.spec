#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libfontenc
Version  : 1.1.3
Release  : 4
URL      : http://xorg.freedesktop.org/releases/individual/lib/libfontenc-1.1.3.tar.gz
Source0  : http://xorg.freedesktop.org/releases/individual/lib/libfontenc-1.1.3.tar.gz
Summary  : The fontenc Library
Group    : Development/Tools
License  : MIT
Requires: libfontenc-lib
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xproto)
BuildRequires : pkgconfig(zlib)

%description
libfontenc - font encoding library
All questions regarding this software should be directed at the
Xorg mailing list:

%package dev
Summary: dev components for the libfontenc package.
Group: Development
Requires: libfontenc-lib

%description dev
dev components for the libfontenc package.


%package lib
Summary: lib components for the libfontenc package.
Group: Libraries

%description lib
lib components for the libfontenc package.


%prep
%setup -q -n libfontenc-1.1.3

%build
%configure --disable-static
make V=1 %{?_smp_mflags}

%check
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/X11/fonts/fontenc.h
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
