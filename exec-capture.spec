
Name:           exec-capture
Summary:        Utility to execute a command and capture its output to a given directory
Version:        0.4
Release:        1%{?org_tag}%{dist}
Source0:        %{name}-%{version}.tar.gz
License:        GPL
URL:            http://www.openfusion.net/
Group:          Applications/File
BuildRoot:      %{_tmppath}/%{name}-%{version}-buildroot
BuildArch:      noarch
BuildRequires:  perl(File::Path) >= 2.0
BuildRequires:  perl(File::SearchPath)
BuildRequires:  perl(Test::Files)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  /usr/bin/pod2man
Requires:       perl(File::SearchPath)

%description
A simple utility to execute a command and capture its output to a named file in
a directory. Really just a convenience wrapper for cron for handling optional
executables and standard output directories slightly more gracefully.

%prep
%setup
  
%build 
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%install
mkdir -p %{buildroot}%{_bindir} 
mkdir -p %{buildroot}%{_mandir}/man1
  
install -m0755 %{name} %{buildroot}%{_bindir}

pod2man %{name} > %{buildroot}%{_mandir}/man1/%{name}.1

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Tue May 22 2012 Gavin Carr <gavin@openfusion.com.au> 0.4-1
- Change from IPC::Run3 to qx() execution, to allow pipes etc.

* Wed May 09 2012 Gavin Carr <gavin@openfusion.com.au> 0.3-1
- Add --sub support, and change name to be --name|-N option.
- Add some initial perldocs.

* Wed Apr 11 2012 Gavin Carr <gavin@openfusion.com.au> 0.2-1
- Add support for quoted commands, commands with options, and --sort.

* Thu Mar 29 2012 Gavin Carr <gavin@openfusion.com.au> 0.1-1
- Initial version.

