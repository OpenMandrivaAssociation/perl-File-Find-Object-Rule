%define	modname	File-Find-Object-Rule
%define	modver	0.0312
%global debug_package %{nil}

Summary:	Perl module providing an alternative interface to File::Find::Object
Name:		perl-%{modname}
Version:	%{perl_convert_version %{modver}}
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/pod/File::Find::Object::Rule
Source0:	https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/File-Find-Object-Rule-%{modver}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Carp)
BuildRequires:	perl(Class::XSAccessor)
BuildRequires:	perl(Cwd)
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Find::Object)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Number::Compare)
BuildRequires:	perl(Text::Glob)
BuildRequires:	perl(File::Spec::Functions)
BuildRequires:	perl(File::Path)
BuildRequires:	perl(IO::Handle)
BuildRequires:	perl(IPC::Open3)
BuildRequires:	perl(Test::More)

%description
File::Find::Object::Rule is a friendlier interface to File::Find::Object.
It allows you to build rules which specify the desired files and directories.

%prep
%autosetup -n %{modname}-%{modver} -p1

%build
perl Build.PL INSTALLDIRS=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
mv %{buildroot}%{_prefix}/local/* %{buildroot}%{_prefix}
rmdir %{buildroot}%{_prefix}/local

%check
RELEASE_TESTING=1 ./Build test

%files
%{_bindir}/findorule
%{_datadir}/perl5/File/*
%{_mandir}/man1/*
%{_mandir}/man3/*
