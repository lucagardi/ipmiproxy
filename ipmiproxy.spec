Name:      ipmiproxy
Version:   19.10.4
Release:   1%{?dist}
Summary:   Python wrapper around ipmitool
Vendor:    CERN
License:   GPL
Group:     System Environment/Base
URL:       https://gitlab.cern.ch/hw/ipmiproxy
Source:    %{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

AutoReq: no
BuildRequires:  python-devel
BuildRequires:  python-setuptools
Requires:       python >= 2.7
Requires:       ipmitool

%description
Python wrapper around ipmitool

%prep
%setup -q

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --skip-build --root %{buildroot}

# Install executable
mkdir -p %{buildroot}%{_bindir}
install -m 755 bin/ipmiproxy  %{buildroot}%{_bindir}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/ipmiproxy
%{python_sitelib}/*
%doc AUTHORS CHANGELOG COPYING

%changelog
* Wed Oct 30 2019 - Luca Gardi <luca.gardi@cern.ch> - 19.10.4-1
- Initial release
