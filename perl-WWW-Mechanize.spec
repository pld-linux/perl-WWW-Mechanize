
# Conditional build:
# tests require internet connection
%bcond_with	tests	# perform "make test"

%include	/usr/lib/rpm/macros.perl
%define	pdir	WWW
%define	pnam	Mechanize
Summary:	WWW::Mechanize - automate interaction with websites
Summary(pl):	WWW::Mechanize - automatyzacja interakcji ze stronami WWW
Name:		perl-WWW-Mechanize
Version:	1.02
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	81dba4c03fe003ce3f715e6432bdb1aa
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6.1
%if %{with tests}
BuildRequires:	perl-libwww >= 5.76
BuildRequires:	perl-URI
BuildRequires:	perl-HTML-Parser >= 3.33
BuildRequires:	perl(Test::More) >= 0.34
BuildRequires:	perl-Test-Pod >= 1.00
%endif
Requires:	perl-libwww >= 5.76
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
Modu� Perla WWW::Mechanize, w skr�cie Mech, zosta� zaprojektowany, aby
u�atwi� automatyzacj� interakcji ze stronami WWW. Wspiera on
wykonywanie szeregu kolejnych pobra� stron, w��czaj�c w to pod��anie
za odno�nikami i odsy�anie formularzy. Ka�da z pobranych stron jest
przetwarzana i wydzielane s� z niej odno�niki i formularze. Mo�na
wybra� odno�nik lub formularz, wype�ni� pola formularza i pobra�
nast�pn� stron�. Mech przechowuje r�wnie� histori� odwiedzanych URL-i,
o kt�re mo�na odpyta� i je ponownie odwiedzi�.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
echo "y" | %{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/%{pdir}/%{pnam}.pm
%dir %{perl_vendorlib}/%{pdir}/%{pnam}
%{perl_vendorlib}/%{pdir}/%{pnam}/*.pm
%{_mandir}/man?/*
