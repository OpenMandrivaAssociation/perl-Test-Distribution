%define module  Test-Distribution
%define name	perl-%{module}
%define version 1.26
%define release %mkrel 2

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Summary: 	Perform tests on all modules of a distribution 
License: 	GPL or Artistic
Group: 		Development/Perl
Source: 	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Test/%{module}-%{version}.tar.bz2
Url:            http://search.cpan.org/dist/%{module}/
Buildrequires:	perl(Module::Build)
Buildrequires:	perl(Module::Signature)
Buildrequires:	perl(Module::CoreList)
requires:	perl(File::Find::Rule)
BuildArch: 	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}

%description
When using this module in a test script, it goes through all the modules in
your distribution, checks their POD, checks that they compile ok and checks
that they all define a $VERSION.

This module also performs a numer of test on the distribution itself. It checks
that your files match your SIGNATURE file if you have one. It checks that your
distribution isn't missing certain 'core' description files. It checks to see
you havent' missed out listing any pre-requisites in Makefile.PL.

It defines its own testing plan, so you usually don't use it in conjunction
with other Test::* modules in the same file. It's recommended that you just
create a one-line test script as shown in the SYNOPSIS above. However, there
are options...

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build
./Build test

%install
rm -rf %{buildroot}
./Build install destdir=%{buildroot}

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Test
%{_mandir}/*/*

