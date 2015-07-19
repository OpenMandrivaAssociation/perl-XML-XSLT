%define modname	XML-XSLT
%define modver	0.48

Summary:	XML::XSLT - A perl module for processing XSLT
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	15
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://www.cpan.org/
Source0:	http://search.cpan.org/CPAN/authors/id/J/JS/JSTOWE/%{modname}-%{modver}.tar.bz2
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl-XML-Parser
BuildRequires:	perl-XML-DOM

%description
This module implements the W3C's XSLT specification. The goal is
full implementation of this spec, but we have not yet achieved
that. However, it already works well. See XML::XSLT Commands for
the current status of each command.

XML::XSLT makes use of XML::DOM and LWP::Simple, while XML::DOM
uses XML::Parser.  Therefore XML::Parser, XML::DOM and LWP::Simple
have to be installed properly for XML::XSLT to run.

%prep
%setup -qn %{modname}-%{modver}
# (tv) fix doc permissions:
chmod 755 examples

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc ChangeLog MANIFEST README examples
%{_bindir}/*
%{perl_vendorlib}/XML
%{_mandir}/man1/*
%{_mandir}/man3/*

