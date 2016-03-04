Name:           puppet-uchiwa
Epoch:          1
Version:        XXX
Release:        XXX
Summary:        Puppet module for installing Uchiwa
License:        Apache 2.0

URL:            https://github.com/yelp/puppet-uchiwa

Source0:        https://github.com/Yelp/puppet-uchiwa/archive/%{version}.tar.gz

BuildArch:      noarch

Requires:       puppet-apt
Requires:       puppet-stdlib
Requires:       puppet >= 2.7.0

%description
Puppet module for installing Uchiwa

%prep
%setup -q -n %{name}-%{version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/uchiwa/
cp -r %{buildroot}/%{_datadir}/openstack-puppet/modules/uchiwa/



%files
%{_datadir}/openstack-puppet/modules/uchiwa/


%changelog

