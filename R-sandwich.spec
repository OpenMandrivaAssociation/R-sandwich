%bcond_without bootstrap
%global packname  sandwich
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          2.2_9
Release:          1
Summary:          Robust Covariance Matrix Estimators
Group:            Sciences/Mathematics
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.2-9.tar.gz
Requires:         R-stats R-zoo 
Requires:         R-stats 
%if %{with bootstrap}
Requires:         R-car R-lmtest R-survival R-MASS R-scatterplot3d 
%else
Requires:         R-car R-lmtest R-strucchange R-AER R-survival R-MASS R-scatterplot3d 
%endif
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-stats R-zoo
BuildRequires:    R-stats 
%if %{with bootstrap}
BuildRequires:    R-car R-lmtest R-survival R-MASS R-scatterplot3d 
%else
BuildRequires:    R-car R-lmtest R-strucchange R-AER R-survival R-MASS R-scatterplot3d 
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
