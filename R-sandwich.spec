%bcond_with bootstrap
%global packname  sandwich
%global rlibdir  %{_libdir}/R/library

%define debug_package %{nil}

Name:             R-%{packname}
Version:          2.2.10
Release:          2
Summary:          Robust Covariance Matrix Estimators
Group:            Sciences/Mathematics
License:          GPL-2
URL:              https://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/sandwich_2.2-10.tar.gz
Requires:         R-stats R-zoo R-stats
%if %{with bootstrap}
Requires:         R-car R-lmtest R-survival R-MASS R-scatterplot3d
%else
Requires:         R-car R-lmtest R-strucchange R-AER R-survival R-MASS
Requires:         R-scatterplot3d
%endif
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-stats R-zoo
BuildRequires:    R-stats
%if %{with bootstrap}
BuildRequires:    R-car R-lmtest R-survival R-MASS R-scatterplot3d
%else
BuildRequires:    R-car R-lmtest R-strucchange R-AER R-survival R-MASS
BuildRequires:    R-scatterplot3d
%endif

%description
Model-robust standard error estimators for cross-sectional, time series
and longitudinal data.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%if %{without bootstrap}
%check
%{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help


%changelog
* Tue Feb 21 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.2_9-2
+ Revision: 778375
- Rebuild with proper dependencies

* Sun Feb 19 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.2_9-1
+ Revision: 777231
- Import R-sandwich
- Import R-sandwich


