#
# Conditional build:
# _with_tests - perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	WWW
%define	pnam	Mechanize
Summary:	WWW::Mechanize - automate interaction with websites
Name:		perl-WWW-Mechanize
Version:	0.59
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	817bd6da487525f914c7c57554df237d
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WWW::Mechanize - automate interaction with websites.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
echo "y" | %{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?_with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{_bindir}/*
%{perl_vendorlib}/WWW/Mechanize.pm
%dir %{perl_vendorlib}/WWW/Mechanize
%{perl_vendorlib}/WWW/Mechanize/*.pm
%{_mandir}/man?/*
