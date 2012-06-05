# TODO:
#	- review Requires/Suggests for default/optional tests
#
%define		relname		UnixBench
Summary:	Unix Bench
Summary(pl.UTF-8):	Unix Bench
Name:		unixbench
Version:	5.1.3
Release:	0.9
License:	GPL v2
Group:		Applications/System
Source0:	http://byte-unixbench.googlecode.com/files/%{relname}%{version}.tgz
# Source0-md5:	21edc4a9e41ad1f9b0297d7b6d45c99a
Source1:	%{name}.sh
Patch0:		%{name}-dirs.patch
URL:		http://code.google.com/p/byte-unixbench/
Requires:	bc
Requires:	ed
Requires:	file
Requires:	fileutils
Requires:	gcc
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
%setup -q -n %{relname}
install %{SOURCE1} unixbench.sh
%patch0 -p1
%{__sed} -i "/export.UB_BINDIR/s@=.*@=%{_libdir}/unixbench@" unixbench.sh

%build
rm -f pgms/select
%{__make} -j 1
%{__make} pgms/{poll,select}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/unixbench}

install pgms/* $RPM_BUILD_ROOT%{_libdir}/unixbench
install testdir/* $RPM_BUILD_ROOT%{_libdir}/unixbench
install Run $RPM_BUILD_ROOT%{_libdir}/unixbench
install unixbench.sh $RPM_BUILD_ROOT%{_bindir}/unixbench

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README USAGE
%attr(755,root,root) %{_bindir}/unixbench
%dir %{_libdir}/unixbench
%attr(755,root,root) %{_libdir}/unixbench/[ae-hl-rtw]*
%attr(755,root,root) %{_libdir}/unixbench/c[lo]*
%attr(755,root,root) %{_libdir}/unixbench/d[ho]*
%attr(755,root,root) %{_libdir}/unixbench/int
%attr(755,root,root) %{_libdir}/unixbench/Run
%attr(755,root,root) %{_libdir}/unixbench/s[ehpy]*
%{_libdir}/unixbench/cctest.c
%{_libdir}/unixbench/dc.dat
%{_libdir}/unixbench/index.[ab]*
%{_libdir}/unixbench/sort.src
%{_libdir}/unixbench/unixbench.logo
