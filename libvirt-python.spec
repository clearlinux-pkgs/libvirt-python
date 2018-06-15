#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libvirt-python
Version  : 3.10.0
Release  : 46
URL      : http://libvirt.org/sources/python/libvirt-python-3.10.0.tar.gz
Source0  : http://libvirt.org/sources/python/libvirt-python-3.10.0.tar.gz
Summary  : The libvirt virtualization API python binding
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1 LGPL-2.1+
Requires: libvirt-python-python3
Requires: libvirt-python-python
BuildRequires : libvirt-dev
BuildRequires : pbr
BuildRequires : pip

BuildRequires : python3-dev
BuildRequires : setuptools

%description
written in the Python programming language to call the interface
        supplied by the libvirt library, to manage the virtualization capabilities
        of recent versions of Linux (and other OSes).

%package python
Summary: python components for the libvirt-python package.
Group: Default
Requires: libvirt-python-python3

%description python
python components for the libvirt-python package.


%package python3
Summary: python3 components for the libvirt-python package.
Group: Default
Requires: python3-core

%description python3
python3 components for the libvirt-python package.


%prep
%setup -q -n libvirt-python-3.10.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523291444
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages py.test-2.7 --verbose || :
%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
