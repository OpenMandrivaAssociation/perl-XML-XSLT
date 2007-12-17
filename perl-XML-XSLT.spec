%define module	XML-XSLT
%define	name	perl-%{module}
%define version 0.48
%define release %mkrel 4

Summary:	XML::XSLT - A perl module for processing XSLT
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://www.cpan.org/
Source0:	http://search.cpan.org/CPAN/authors/id/J/JS/JSTOWE/%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:	perl-XML-Parser
BuildRequires:  perl-XML-DOM
BuildArch:	noarch

%description
This module implements the W3C's XSLT specification. The goal is
full implementation of this spec, but we have not yet achieved
that. However, it already works well. See XML::XSLT Commands for
the current status of each command.

XML::XSLT makes use of XML::DOM and LWP::Simple, while XML::DOM
uses XML::Parser.  Therefore XML::Parser, XML::DOM and LWP::Simple
have to be installed properly for XML::XSLT to run.

%prep

%setup -q -n %{module}-%{version}
# (tv) fix doc permissions:
chmod 755 examples

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%clean 
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%files
%defattr(-,root,root)
%doc ChangeLog MANIFEST README examples
#%doc %attr(644,root,-) ChangeLog MANIFEST README examples
%{_bindir}/*
%{_mandir}/*/*
%{perl_vendorlib}/XML


