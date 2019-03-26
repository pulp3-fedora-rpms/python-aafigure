# Created by pyp2rpm-3.3.2
%global pypi_name aafigure

Name:           python-%{pypi_name}
Version:        0.6
Release:        1%{?dist}
Summary:        ASCII art to image converter

License:        BSD
URL:            http://launchpad.net/aafigure
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)
# Manually added build dependencies.
# Requires PIL or pillow. pillow is in Fedora already.
BuildRequires:  python3dist(pillow)
BuildRequires:  python3dist(reportlab)

%description
This package provides a module aafigure, that can be used from other programs,
and a command line tool aafigure.Example, test.txt:: +--+ ^ | | | >+ +o> | | |
+--+ VCommand:: aafigure test.txt -t svg -o test.svgPlease see documentation
for examples.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
This package provides a module aafigure, that can be used from other programs,
and a command line tool aafigure.Example, test.txt:: +--+ ^ | | | >+ +o> | | |
+--+ VCommand:: aafigure test.txt -t svg -o test.svgPlease see documentation
for examples.

%package -n python-%{pypi_name}-doc
Summary:        aafigure documentation
%description -n python-%{pypi_name}-doc
Documentation for aafigure

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
# generate html docs 
PYTHONPATH=${PWD} sphinx-build-3 documentation html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc examples/README-EXAMPLES.txt README.rst
%{_bindir}/aafigure
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE.txt

%changelog
* Tue Mar 26 2019 Mike DePaulo <mikedep333@redhat.com> - 0.6-1
- Initial package.
