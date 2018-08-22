#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : persistent
Version  : 4.4.0
Release  : 21
URL      : https://files.pythonhosted.org/packages/ec/cf/2d9aed78f3f5a17f3ededb733bbadfaccf02c081ee405103db4f497123c7/persistent-4.4.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/ec/cf/2d9aed78f3f5a17f3ededb733bbadfaccf02c081ee405103db4f497123c7/persistent-4.4.0.tar.gz
Summary  : Translucent persistent objects
Group    : Development/Tools
License  : ZPL-2.1
Requires: persistent-python3
Requires: persistent-license
Requires: persistent-python
Requires: Sphinx
Requires: cffi
Requires: zope.interface
Requires: zope.testrunner
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python3-dev
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
%setup -q -n persistent-4.4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1534947275
python3 setup.py build -b py3

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
