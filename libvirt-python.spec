#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libvirt-python
Version  : 8.9.0
Release  : 101
URL      : https://github.com/libvirt/libvirt-python/archive/v8.9.0/libvirt-python-8.9.0.tar.gz
Source0  : https://github.com/libvirt/libvirt-python/archive/v8.9.0/libvirt-python-8.9.0.tar.gz
Summary  : The libvirt virtualization API python binding
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: libvirt-python-filemap = %{version}-%{release}
Requires: libvirt-python-lib = %{version}-%{release}
Requires: libvirt-python-license = %{version}-%{release}
Requires: libvirt-python-python = %{version}-%{release}
Requires: libvirt-python-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : libvirt-dev
BuildRequires : pypi(py)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
=============================
This package provides a python binding to the libvirt.so,
libvirt-qemu.so and libvirt-lxc.so library APIs.

%package filemap
Summary: filemap components for the libvirt-python package.
Group: Default

%description filemap
filemap components for the libvirt-python package.


%package lib
Summary: lib components for the libvirt-python package.
Group: Libraries
Requires: libvirt-python-license = %{version}-%{release}
Requires: libvirt-python-filemap = %{version}-%{release}

%description lib
lib components for the libvirt-python package.


%package license
Summary: license components for the libvirt-python package.
Group: Default

%description license
license components for the libvirt-python package.


%package python
Summary: python components for the libvirt-python package.
Group: Default
Requires: libvirt-python-python3 = %{version}-%{release}

%description python
python components for the libvirt-python package.


%package python3
Summary: python3 components for the libvirt-python package.
Group: Default
Requires: libvirt-python-filemap = %{version}-%{release}
Requires: python3-core
Provides: pypi(libvirt_python)

%description python3
python3 components for the libvirt-python package.


%prep
%setup -q -n libvirt-python-8.9.0
cd %{_builddir}/libvirt-python-8.9.0
pushd ..
cp -a libvirt-python-8.9.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1667325158
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libvirt-python
cp %{_builddir}/libvirt-python-%{version}/COPYING %{buildroot}/usr/share/package-licenses/libvirt-python/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/libvirt-python-%{version}/COPYING.LESSER %{buildroot}/usr/share/package-licenses/libvirt-python/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-libvirt-python

%files lib
%defattr(-,root,root,-)
/usr/share/clear/optimized-elf/other*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libvirt-python/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/libvirt-python/4cc77b90af91e615a64ae04893fdffa7939db84c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
