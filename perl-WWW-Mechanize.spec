#
# Conditional build:
# _with_tests - perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	WWW
%define	pnam	Mechanize
Summary:	WWW::Mechanize - automate interaction with websites
Summary(pl):	WWW::Mechanize - automatyzacja interakcji ze stronami WWW
Name:		perl-WWW-Mechanize
Version:	0.59
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	817bd6da487525f914c7c57554df237d
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6.1
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

%description -l pl
Modu³ Perla WWW::Mechanize, w skrócie Mech, zosta³ zaprojektowany, aby
u³atwiæ automatyzacjê interakcji ze stronami WWW. Wspiera on
wykonywanie szeregu kolejnych pobrañ stron, w³±czaj±c w to pod±¿anie
za odno¶nikami i odsy³anie formularzy. Ka¿da z pobranych stron jest
przetwarzana i wydzielane s± z niej odno¶niki i formularze. Mo¿na
wybraæ odno¶nik lub formularz, wype³niæ pola formularza i pobraæ
nastêpn± stronê. Mech przechowuje równie¿ historiê odwiedzanych URL-i,
o które mo¿na odpytaæ i je ponownie odwiedziæ.

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
