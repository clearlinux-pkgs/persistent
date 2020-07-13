#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : persistent
Version  : 4.6.4
Release  : 40
URL      : https://files.pythonhosted.org/packages/d3/bc/3a732d5089a470eb340bc4222dc101666319a04ffa09f7593b246104850c/persistent-4.6.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/d3/bc/3a732d5089a470eb340bc4222dc101666319a04ffa09f7593b246104850c/persistent-4.6.4.tar.gz
Summary  : Translucent persistent objects
Group    : Development/Tools
License  : ZPL-2.1
Requires: persistent-license = %{version}-%{release}
Requires: persistent-python = %{version}-%{release}
Requires: persistent-python3 = %{version}-%{release}
Requires: cffi
Requires: zope.interface
BuildRequires : buildreq-distutils3
BuildRequires : cffi
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : python3-dev
BuildRequires : tox
BuildRequires : virtualenv
BuildRequires : zope.interface

%description
``persistent``:  automatic persistence for Python objects
=========================================================

%package dev
Summary: dev components for the persistent package.
Group: Development
Provides: persistent-devel = %{version}-%{release}
Requires: persistent = %{version}-%{release}
Requires: persistent = %{version}-%{release}

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
Requires: persistent-python3 = %{version}-%{release}

%description python
python components for the persistent package.


%package python3
Summary: python3 components for the persistent package.
Group: Default
Requires: python3-core
Provides: pypi(persistent)
Requires: pypi(cffi)
Requires: pypi(zope.interface)

%description python3
python3 components for the persistent package.


%prep
%setup -q -n persistent-4.6.4
cd %{_builddir}/persistent-4.6.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1585267524
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/persistent
cp %{_builddir}/persistent-4.6.4/LICENSE.txt %{buildroot}/usr/share/package-licenses/persistent/a0b53f43aab58b46bf79ba756c50771c605ab4c5
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/python3.8/persistent/cPersistence.h
/usr/include/python3.8/persistent/ring.h

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/persistent/a0b53f43aab58b46bf79ba756c50771c605ab4c5

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
