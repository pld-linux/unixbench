Summary:	Unix Bench
Summary(pl.UTF-8):	Unix Bench
Name:		unixbench
Version:	4.1.0
Release:	6
License:	unknown ("for usage of Linux community")
Group:		Applications/System
Source0:	ftp://ftp.tux.org/pub/tux/benchmarks/System/unixbench/%{name}-%{version}.tgz
# Source0-md5:	3561ae1f067f9dfb9707c062f536acac
Patch0:		%{name}-dirs.patch
Patch1:		%{name}-lib64.patch
URL:		http://www.tux.org/pub/tux/benchmarks/System/unixbench/
Requires:	bc
Requires:	ed
Requires:	file
Requires:	fileutils
Requires:	gcc
Requires:	glibc-devel
Requires:	make
Requires:	mawk
Requires:	mktemp
Requires:	sed
Requires:	sh-utils
Requires:	textutils
Requires:	time
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Unix Bench - based on the Byte Magazine Unix Benchmark.

%description -l pl.UTF-8
Unix Bench, bazowany na Unix Benchmark z Byte Magazine.

%prep
%setup -q
%patch0 -p1
%if "%{_lib}" == "lib64"
%patch1 -p1
%endif

%build
rm -f pgms/select
%{__make}
%{__make} pgms/{poll,select}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/unixbench}

install pgms/* $RPM_BUILD_ROOT%{_libdir}/unixbench
install testdir/* $RPM_BUILD_ROOT%{_libdir}/unixbench
install Run $RPM_BUILD_ROOT%{_bindir}/unixbench

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
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
