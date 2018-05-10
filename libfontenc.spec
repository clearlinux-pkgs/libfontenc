#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xCFDF148828C642A7 (alanc@freedesktop.org)
#
Name     : libfontenc
Version  : 1.1.3
Release  : 13
URL      : http://xorg.freedesktop.org/releases/individual/lib/libfontenc-1.1.3.tar.gz
Source0  : http://xorg.freedesktop.org/releases/individual/lib/libfontenc-1.1.3.tar.gz
Source99 : http://xorg.freedesktop.org/releases/individual/lib/libfontenc-1.1.3.tar.gz.sig
Summary  : The fontenc Library
Group    : Development/Tools
License  : MIT
Requires: libfontenc-lib
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : pkgconfig(32fontutil)
BuildRequires : pkgconfig(32xorg-macros)
BuildRequires : pkgconfig(32xproto)
BuildRequires : pkgconfig(fontutil)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xproto)
BuildRequires : zlib-dev
BuildRequires : zlib-dev32

%description
libfontenc - font encoding library
All questions regarding this software should be directed at the
Xorg mailing list:

%package dev
Summary: dev components for the libfontenc package.
Group: Development
Requires: libfontenc-lib
Provides: libfontenc-devel

%description dev
dev components for the libfontenc package.


%package dev32
Summary: dev32 components for the libfontenc package.
Group: Default
Requires: libfontenc-lib32
Requires: libfontenc-dev

%description dev32
dev32 components for the libfontenc package.


%package lib
Summary: lib components for the libfontenc package.
Group: Libraries

%description lib
lib components for the libfontenc package.


%package lib32
Summary: lib32 components for the libfontenc package.
Group: Default

%description lib32
lib32 components for the libfontenc package.


%prep
%setup -q -n libfontenc-1.1.3
pushd ..
cp -a libfontenc-1.1.3 build32
popd

%build
export LANG=C
export SOURCE_DATE_EPOCH=1484421098
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-semantic-interposition "
%configure --disable-static
make V=1  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make V=1  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1484421098
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/X11/fonts/fontenc.h
/usr/lib64/libfontenc.so
/usr/lib64/pkgconfig/fontenc.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libfontenc.so
/usr/lib32/pkgconfig/32fontenc.pc
/usr/lib32/pkgconfig/fontenc.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libfontenc.so.1
/usr/lib64/libfontenc.so.1.0.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libfontenc.so.1
/usr/lib32/libfontenc.so.1.0.0
