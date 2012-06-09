# TODO:
#	- do something sane with temporary dir (rm but save test results/logs)
#	- resolve problems (Can't take log of 0 at /usr/lib/unixbench/Run line 926) with
#	  short/long/int/float/double/arithoh tests)
#	- do something with missing programs: 3dinfo + runlevel
#
%bcond_without	x11		# build graphics test
#
%define		relname		UnixBench
Summary:	Unix Bench
Summary(pl.UTF-8):	Unix Bench
Name:		unixbench
Version:	5.1.3
Release:	0.10
License:	GPL v2
Group:		Applications/System
Source0:	http://byte-unixbench.googlecode.com/files/%{relname}%{version}.tgz
# Source0-md5:	21edc4a9e41ad1f9b0297d7b6d45c99a
Source1:	%{name}.sh
Patch0:		%{name}-dirs.patch
URL:		http://code.google.com/p/byte-unixbench/
%{?with_x11:BuildRequires:	OpenGL-devel}
%{?with_x11:BuildRequires:	xorg-lib-libX11-devel}
%{?with_x11:BuildRequires:	xorg-lib-libXext-devel}
Requires:	mktemp
Requires:	perl(Time::HiRes)
# grep test
Suggests:	grep
# C test
Suggests:	gcc
Suggests:	glibc-devel
# dc test
Suggests:	bc
# graphics test
Suggests:	xorg-app-x11perf
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

%{__make} -j 1 %{?with_x11:GRAPHIC_TESTS=1}
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
%{?with_x11:%attr(755,root,root) %{_libdir}/unixbench/ubgears}
%{_libdir}/unixbench/cctest.c
%{_libdir}/unixbench/dc.dat
%{_libdir}/unixbench/index.[ab]*
%{_libdir}/unixbench/sort.src
%{_libdir}/unixbench/unixbench.logo
