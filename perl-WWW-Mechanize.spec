#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define		pdir	WWW
%define		pnam	Mechanize
Summary:	WWW::Mechanize - automate interaction with websites
Summary(pl.UTF-8):	WWW::Mechanize - automatyzacja interakcji ze stronami WWW
Name:		perl-WWW-Mechanize
Version:	2.15
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/WWW/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6e269687c5f5a9400fdf256e593756bc
URL:		https://metacpan.org/dist/WWW-Mechanize
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-Encode
BuildRequires:	perl-HTML-Form >= 1.00
BuildRequires:	perl-HTML-Parser >= 3.33
BuildRequires:	perl-HTML-Tree >= 5
BuildRequires:	perl-HTTP-Cookies
BuildRequires:	perl-HTTP-Daemon >= 6.12
BuildRequires:	perl-HTTP-Message >= 1.30
BuildRequires:	perl-HTTP-Server-Simple
BuildRequires:	perl-Path-Tiny
BuildRequires:	perl-Scalar-List-Utils >= 1.14
BuildRequires:	perl-Sub-Uplevel >= 0.13
BuildRequires:	perl-Test-Deep
BuildRequires:	perl-Test-Exception
BuildRequires:	perl-Test-Fatal
BuildRequires:	perl-Test-Memory-Cycle >= 1.06
BuildRequires:	perl-Test-NoWarnings >= 1.04
BuildRequires:	perl-Test-Output
BuildRequires:	perl-Test-Simple >= 0.96
BuildRequires:	perl-Test-Taint >= 1.08
BuildRequires:	perl-Test-Warn
BuildRequires:	perl-Test-Warnings
BuildRequires:	perl-URI
BuildRequires:	perl-libwww >= 6.45
%endif
Requires:	perl-Encode
Requires:	perl-libwww >= 6.45
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WWW::Mechanize, or Mech for short, was designed to help you automate
interaction with a website. It supports performing a sequence of page
fetches including following links and submitting forms. Each fetched
page is parsed and its links and forms are extracted. A link or a form
can be selected, form fields can be filled and the next page can be
fetched. Mech also stores a history of the URLs you've visited, which
can be queried and revisited.

%description -l pl.UTF-8
Moduł Perla WWW::Mechanize, w skrócie Mech, został zaprojektowany, aby
ułatwić automatyzację interakcji ze stronami WWW. Wspiera on
wykonywanie szeregu kolejnych pobrań stron, włączając w to podążanie
za odnośnikami i odsyłanie formularzy. Każda z pobranych stron jest
przetwarzana i wydzielane są z niej odnośniki i formularze. Można
wybrać odnośnik lub formularz, wypełnić pola formularza i pobrać
następną stronę. Mech przechowuje również historię odwiedzanych URL-i,
o które można odpytać i je ponownie odwiedzić.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
echo 'y' | %{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/WWW/Mechanize/{FAQ,Cookbook,Examples}.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%attr(755,root,root) %{_bindir}/mech-dump
%{perl_vendorlib}/WWW/Mechanize.pm
%dir %{perl_vendorlib}/WWW/Mechanize
%{perl_vendorlib}/WWW/Mechanize/*.pm
%{_mandir}/man1/mech-dump.1p*
%{_mandir}/man3/WWW::Mechanize*.3pm*
