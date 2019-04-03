#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x597240FE94E60165 (rbtcollins@hp.com)
#
Name     : deprecated-funcsigs
Version  : 1.0.2
Release  : 44
URL      : http://pypi.debian.net/funcsigs/funcsigs-1.0.2.tar.gz
Source0  : http://pypi.debian.net/funcsigs/funcsigs-1.0.2.tar.gz
Source99 : http://pypi.debian.net/funcsigs/funcsigs-1.0.2.tar.gz.asc
Summary  : Python function signatures from PEP362 for Python 2.6, 2.7 and 3.2+
Group    : Development/Tools
License  : Apache-2.0
Requires: deprecated-funcsigs-license = %{version}-%{release}
Requires: deprecated-funcsigs-python = %{version}-%{release}
Requires: ordereddict
BuildRequires : buildreq-distutils
BuildRequires : buildreq-distutils3
BuildRequires : linecache2
BuildRequires : setuptools
BuildRequires : setuptools-legacypython
BuildRequires : six
BuildRequires : traceback2
BuildRequires : unittest2

%description
.. funcsigs documentation master file, created by
sphinx-quickstart on Fri Apr 20 20:27:52 2012.
You can adapt this file completely to your liking, but it should at least
contain the root `toctree` directive.

%package legacypython
Summary: legacypython components for the deprecated-funcsigs package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the deprecated-funcsigs package.


%package license
Summary: license components for the deprecated-funcsigs package.
Group: Default

%description license
license components for the deprecated-funcsigs package.


%package python
Summary: python components for the deprecated-funcsigs package.
Group: Default

%description python
python components for the deprecated-funcsigs package.


%prep
%setup -q -n funcsigs-1.0.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1554319883
export MAKEFLAGS=%{?_smp_mflags}
python2 setup.py build -b py2

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/deprecated-funcsigs
cp LICENSE %{buildroot}/usr/share/package-licenses/deprecated-funcsigs/LICENSE
python2 -tt setup.py build -b py2 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/deprecated-funcsigs/LICENSE

%files python
%defattr(-,root,root,-)
