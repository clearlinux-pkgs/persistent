#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : persistent
Version  : 4.5.1
Release  : 33
URL      : https://files.pythonhosted.org/packages/da/4d/2ec9bf8f6b4089ca575be54f160959aca3d3b6985bc04d9c33b5747a3096/persistent-4.5.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/da/4d/2ec9bf8f6b4089ca575be54f160959aca3d3b6985bc04d9c33b5747a3096/persistent-4.5.1.tar.gz
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
=========================================================

%package dev
Summary: dev components for the persistent package.
Group: Development
Provides: persistent-devel = %{version}-%{release}
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

%description python3
python3 components for the persistent package.


%prep
%setup -q -n persistent-4.5.1
cd %{_builddir}/persistent-4.5.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1574289515
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
cp %{_builddir}/persistent-4.5.1/LICENSE.txt %{buildroot}/usr/share/package-licenses/persistent/a0b53f43aab58b46bf79ba756c50771c605ab4c5
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
