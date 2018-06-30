#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xF2A968348913D1D8 (tseaver@palladion.com)
#
Name     : persistent
Version  : 4.2.4
Release  : 12
URL      : http://pypi.debian.net/persistent/persistent-4.2.4.tar.gz
Source0  : http://pypi.debian.net/persistent/persistent-4.2.4.tar.gz
Source99 : http://pypi.debian.net/persistent/persistent-4.2.4.tar.gz.asc
Summary  : Translucent persistent objects
Group    : Development/Tools
License  : ZPL-2.1
Requires: persistent-python3
Requires: persistent-license
Requires: persistent-python
Requires: Sphinx
Requires: coverage
Requires: nose
Requires: zope.interface
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : tox
BuildRequires : virtualenv
BuildRequires : zope.interface

%description
=========================================================

%package dev
Summary: dev components for the persistent package.
Group: Development
Provides: persistent-devel

%description dev
dev components for the persistent package.


%package license
Summary: license components for the persistent package.
Group: Default

%description license
license components for the persistent package.


%package python
Summary: python components for the persistent package.
Group: Default
Requires: persistent-python3

%description python
python components for the persistent package.


%package python3
Summary: python3 components for the persistent package.
Group: Default
Requires: python3-core

%description python3
python3 components for the persistent package.


%prep
%setup -q -n persistent-4.2.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530328794
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test || :
%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/persistent
cp LICENSE.txt %{buildroot}/usr/share/doc/persistent/LICENSE.txt
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/python3.7m/persistent/cPersistence.h
/usr/include/python3.7m/persistent/ring.h

%files license
%defattr(-,root,root,-)
/usr/share/doc/persistent/LICENSE.txt

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
