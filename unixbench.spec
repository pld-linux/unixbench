Summary:	Unix Bench
Summary(pl):	Unix Bench
Name:		unixbench
Version:	4.1.0
Release:	1
License:	unknown ("for usage of Linux community")
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	ftp://ftp.tux.org/pub/tux/benchmarks/System/unixbench/%{name}-%{version}.tgz
Patch0:		%{name}-dirs.patch
URL:		http://www.tux.org/pub/tux/benchmarks/System/unixbench/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	mawk fileutils textutils sh-utils bc ed sed mktemp make gcc glibc-devel

%description
Unix Bench - based on the Byte Magazine Unix Benchmark.

%description -l pl
Unix Bench, bazowany na Unix Benchmark z Byte Magazine.

%prep
%setup -q
%patch -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/unixbench}

install pgms/* $RPM_BUILD_ROOT%{_libdir}/unixbench
install testdir/* $RPM_BUILD_ROOT%{_libdir}/unixbench
install Run $RPM_BUILD_ROOT%{_bindir}/unixbench

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/unixbench
%dir %{_libdir}/unixbench
%attr(755,root,root) %{_libdir}/unixbench/[ae-hl-rtw]*
%attr(755,root,root) %{_libdir}/unixbench/c[lo]*
%attr(755,root,root) %{_libdir}/unixbench/d[ho]*
%attr(755,root,root) %{_libdir}/unixbench/index.sh
%attr(755,root,root) %{_libdir}/unixbench/s[ehpy]*
%{_libdir}/unixbench/cctest.c
%{_libdir}/unixbench/dc.dat
%{_libdir}/unixbench/index.[ab]*
%{_libdir}/unixbench/sort.src
%{_libdir}/unixbench/unixbench.logo
