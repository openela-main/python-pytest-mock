%bcond_without python3

%global pypi_name pytest-mock
%global file_name pytest_mock
%global desc This plugin installs a mocker fixture which is a thin-wrapper around the \
patching API provided by the mock package, but with the benefit of not having \
to worry about undoing patches at the end of a test.


Name:           python-%{pypi_name}
Version:        1.9.0
Release:        4%{?dist}
Summary:        Thin-wrapper around the mock package for easier use with py.test

License:        MIT
URL:            https://pypi.python.org/pypi/pytest-mock
Source0:        https://files.pythonhosted.org/packages/53/92/ed98ceca37fe779b4277382c7dd501936bac9d54bc3a19c32ae876701c81/pytest-mock-1.9.0.tar.gz
BuildArch:      noarch

%description
%{desc}


%package -n     python2-%{pypi_name}
BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python2-pytest >= 2.7
BuildRequires:  python2-mock
BuildRequires:  python2-setuptools_scm
Requires:       python2-pytest >= 2.7
Requires:       python2-mock
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
%{desc}


%if %{with python3}
%package -n     python3-%{pypi_name}
Summary:        %{summary}
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest >= 2.7
BuildRequires:  python3-setuptools_scm
Requires:       python3-pytest >= 2.7
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{desc}

%endif

%prep
%setup -qn %{pypi_name}-%{version}
rm -rf *.egg-info

# Correct end of line encoding for README
sed -i 's/\r$//' README.rst


%build
%py2_build
%if %{with python3}
%py3_build
%endif

%install
%if %{with python3}
%py3_install
%endif
%py2_install


%check
PYTHONPATH="$(pwd)" py.test-%{python2_version} test_pytest_mock.py
%if %{with python3}
PYTHONPATH="$(pwd)" py.test-%{python3_version} test_pytest_mock.py
%endif

%files -n python2-%{pypi_name}
%doc README.rst
%license LICENSE
%{python2_sitelib}/%{file_name}-%{version}-py%{python2_version}.egg-info/
%{python2_sitelib}/%{file_name}.py*
%{python2_sitelib}/_pytest_mock_version.py*


%if %{with python3}
%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{file_name}-%{version}-py%{python3_version}.egg-info/
%{python3_sitelib}/%{file_name}.py*
%{python3_sitelib}/__pycache__/%{file_name}*.py*
%{python3_sitelib}/_pytest_mock_version.py*
%{python3_sitelib}/__pycache__/_pytest_mock_version.cpython*
%endif


%changelog
* Thu Apr 25 2019 Tomas Orsava <torsava@redhat.com> - 1.9.0-4
- Bumping due to problems with modular RPM upgrade path
- Resolves: rhbz#1695587

* Tue Jul 31 2018 Lumír Balhar <lbalhar@redhat.com> - 1.9.0-2
- Make possible to disable python3 subpackage

* Mon Jul 16 2018 Lumír Balhar <lbalhar@redhat.com> - 1.9.0-2
- First version for python27 module
