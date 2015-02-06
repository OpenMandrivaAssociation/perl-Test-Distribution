%define module	Test-Distribution
%define upstream_version 2.00

Name:		perl-%{module}
Version: 	%perl_convert_version %{upstream_version}
Release: 	3
Summary: 	Perform tests on all modules of a distribution 
License: 	GPLv2 or Artistic
Group: 		Development/Perl
Url:        http://search.cpan.org/dist/%{module}/
Source: 	http://www.cpan.org/modules/by-module/Test/Test-Distribution-%{upstream_version}.tar.gz
Buildrequires:	perl(Module::Build)
Buildrequires:	perl(Module::Signature)
Buildrequires:	perl(Module::CoreList)
requires:	perl(File::Find::Rule)
BuildArch: 	noarch

%description
When using this module in a test script, it goes through all the modules in
your distribution, checks their POD, checks that they compile OK and checks
that they all define a $VERSION.

This module also performs a number of test on the distribution itself. 
It checks that your files match your SIGNATURE file if you have one. It 
checks that your distribution isn't missing certain 'core' description 
files. It checks to see you haven't missed out listing any prerequisites 
in Makefile.PL.

It defines its own testing plan, so you usually don't use it in conjunction
with other Test::* modules in the same file. It's recommended that you just
create a one-line test script as shown in the SYNOPSIS above. However, there
are options...

%prep
%setup -q -n %{module}-%{upstream_version}

%build
%{__perl} Build.PL installdirs=vendor
./Build
./Build test

%install
./Build install destdir=%{buildroot}

%files
%doc Changes.pod README
%{perl_vendorlib}/Test
%{_mandir}/*/*



%changelog
* Mon Apr 30 2012 Crispin Boylan <crisb@mandriva.org> 2.00-6
+ Revision: 794547
- Rebuild

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 2.00-5mdv2010.0
+ Revision: 430593
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 2.00-4mdv2009.0
+ Revision: 258512
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 2.00-3mdv2009.0
+ Revision: 246532
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sat Nov 17 2007 Funda Wang <fwang@mandriva.org> 2.00-1mdv2008.1
+ Revision: 109317
- New version 2.00

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - update to new version 1.29

* Thu Nov 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.27-1mdv2008.1
+ Revision: 104456
- update to new version 1.27
- fix doc files

* Mon Jul 02 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.26-2mdv2008.0
+ Revision: 47042
- rebuild


