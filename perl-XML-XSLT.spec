%define upstream_name	 XML-XSLT
%define upstream_version 0.48

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	XML::XSLT - A perl module for processing XSLT
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://www.cpan.org/
Source0:	http://search.cpan.org/CPAN/authors/id/J/JS/JSTOWE/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl-XML-Parser
BuildRequires:	perl-XML-DOM
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
%setup -q -n %{upstream_name}-%{upstream_version}
# (tv) fix doc permissions:
chmod 755 examples

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
%makeinstall_std

%files
%doc ChangeLog MANIFEST README examples
%{_bindir}/*
%{_mandir}/*/*
%{perl_vendorlib}/XML


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.480.0-4mdv2012.0
+ Revision: 765870
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.480.0-2
+ Revision: 667465
- mass rebuild

* Tue Jul 28 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.480.0-1mdv2011.0
+ Revision: 401811
- rebuild using %%perl_convert_version
- fixed license field

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.48-6mdv2009.0
+ Revision: 224678
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 0.48-5mdv2008.1
+ Revision: 180665
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Mon Nov 06 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.48-4mdv2007.0
+ Revision: 76920
- Import perl-XML-XSLT

* Mon Nov 06 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.48-4mdv2007.1
- fix doc perms

* Sun Jul 31 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.48-3mdk
- Fix BuildRequires

* Tue Jun 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.48-2mdk
- fix deps (rgs)
- misc spec file fixes

* Sat Apr 24 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.48-1mdk
- 0.48

