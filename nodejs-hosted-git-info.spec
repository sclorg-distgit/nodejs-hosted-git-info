%{?scl:%scl_package nodejs-hosted-git-info}
%{!?scl:%global pkg_name %{name}}

# spec file for package nodejs-nodejs-hosted-git-info

%global npm_name hosted-git-info
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:           %{?scl_prefix}nodejs-hosted-git-info
Version:        2.1.4
Release:        3%{?dist}
Summary:        Provides metadata and conversions from repository urls for Github, Bitbucket and Gitlab
Url:            https://github.com/npm/hosted-git-info
Source0:        https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:        ISC

BuildArch:	noarch
ExclusiveArch:	%{nodejs_arches} noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

%if 0%{?enable_tests}
#BuildRequires: %{?scl_prefix}npm(standard)
#missing dependency
BuildRequires: %{?scl_prefix}npm(tap)
%endif

%description
Provides metadata and conversions from repository urls for Github, Bitbucket and Gitlab

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json index.js git-host.js git-host-info.js \
	%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%if 0%{?enable_tests}

%check
%{nodejs_symlink_deps} --check
#standard && tap test/*.js
#commented out because of missing dependency
tap test/*.js
%endif

%files
%{nodejs_sitelib}/hosted-git-info

%doc README.md
%license LICENSE

%changelog
* Thu Nov 26 2015 Tomas Hrcka <thrcka@redhat.com> - 2.1.4-3
- Enable scl macros

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 22 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.1.4-1
- New upstream release with license

* Wed May 13 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.1.2-1
- Initial build
