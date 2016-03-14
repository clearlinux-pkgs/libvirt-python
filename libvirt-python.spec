#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libvirt-python
Version  : 1.3.2
Release  : 26
URL      : http://libvirt.org/sources/python/libvirt-python-1.3.2.tar.gz
Source0  : http://libvirt.org/sources/python/libvirt-python-1.3.2.tar.gz
Summary  : The libvirt virtualization API
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1 LGPL-2.1+
Requires: libvirt-python-python
BuildRequires : libvirt-dev
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
The libvirt-python package contains a module that permits applications
written in the Python programming language to use the interface
supplied by the libvirt library to use the virtualization capabilities
of recent versions of Linux (and other OSes).

%package python
Summary: python components for the libvirt-python package.
Group: Default

%description python
python components for the libvirt-python package.


%prep
%setup -q -n libvirt-python-1.3.2

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages py.test-2.7 --verbose || :
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
