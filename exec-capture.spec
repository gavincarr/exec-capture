
Name:           exec-capture
Summary:        Utility to execute a command and capture its output to a given directory
Version:        0.2
Release:        1%{?org_tag}%{dist}
Source0:        %{name}-%{version}.tar.gz
License:        GPL
URL:            http://www.openfusion.net/
Group:          Applications/File
BuildRoot:      %{_tmppath}/%{name}-%{version}-buildroot
BuildArch:      noarch
BuildRequires:  perl(File::Path) >= 2.0
BuildRequires:  perl(File::SearchPath)
BuildRequires:  perl(IPC::Run3)
BuildRequires:  perl(Test::Files)
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(File::SearchPath)
Requires:       perl(IPC::Run3)

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
  
install -m0755 %{name} %{buildroot}%{_bindir}

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/*

%changelog
* Wed Apr 11 2012 Gavin Carr <gavin@openfusion.com.au> 0.2-1
- Add support for quoted commands, commands with options, and --sort.

* Thu Mar 29 2012 Gavin Carr <gavin@openfusion.com.au> 0.1-1
- Initial version.

