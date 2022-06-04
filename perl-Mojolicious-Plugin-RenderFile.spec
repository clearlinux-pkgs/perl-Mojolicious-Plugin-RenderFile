#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Mojolicious-Plugin-RenderFile
Version  : 0.12
Release  : 18
URL      : https://cpan.metacpan.org/authors/id/K/KO/KOORCHIK/Mojolicious-Plugin-RenderFile-0.12.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/K/KO/KOORCHIK/Mojolicious-Plugin-RenderFile-0.12.tar.gz
Summary  : unknown
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Mojolicious-Plugin-RenderFile-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Mojo::Base)
BuildRequires : perl(Mojolicious)

%description
=head1 NAME
Mojolicious::Plugin::RenderFile - "render_file" helper for Mojolicious

%package dev
Summary: dev components for the perl-Mojolicious-Plugin-RenderFile package.
Group: Development
Provides: perl-Mojolicious-Plugin-RenderFile-devel = %{version}-%{release}
Requires: perl-Mojolicious-Plugin-RenderFile = %{version}-%{release}

%description dev
dev components for the perl-Mojolicious-Plugin-RenderFile package.


%package perl
Summary: perl components for the perl-Mojolicious-Plugin-RenderFile package.
Group: Default
Requires: perl-Mojolicious-Plugin-RenderFile = %{version}-%{release}

%description perl
perl components for the perl-Mojolicious-Plugin-RenderFile package.


%prep
%setup -q -n Mojolicious-Plugin-RenderFile-0.12
cd %{_builddir}/Mojolicious-Plugin-RenderFile-0.12

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Mojolicious::Plugin::RenderFile.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
