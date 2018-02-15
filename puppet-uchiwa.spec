%{!?upstream_version: %global upstream_version %{commit}}
%define upstream_name puppet-uchiwa
%global commit 92c7f71f864ecc2a1e747b1a48be69c737ec97a4
%global shortcommit %(c=%{commit}; echo ${c:0:7})
# DO NOT REMOVE ALPHATAG
%global alphatag .%{shortcommit}git


Name:           puppet-uchiwa
Version:        2.0.0
Release:        1%{?alphatag}%{?dist}
Summary:        Puppet module for installing Uchiwa
License:        ASL 2.0

URL:            https://github.com/yelp/puppet-uchiwa

Source0:        https://github.com/Yelp/%{upstream_name}/archive/%{commit}.tar.gz#/%{upstream_name}-%{shortcommit}.tar.gz

BuildArch:      noarch

#Requires:       puppet-apt
Requires:       puppet-stdlib
Requires:       puppet >= 2.7.0

%description
Puppet module for installing Uchiwa

%prep
%setup -q -n %{name}-%{upstream_version}

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
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/uchiwa/



%files
%{_datadir}/openstack-puppet/modules/uchiwa/


%changelog
* Thu Feb 15 2018 RDO <dev@lists.rdoproject.org> 2.0.0-1.92c7f71git
- Update to post 2.0.0 (92c7f71f864ecc2a1e747b1a48be69c737ec97a4)



