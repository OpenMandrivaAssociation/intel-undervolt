%undefine _debugsource_packages

Name:           intel-undervolt
Version:        1.7
Release:        1
Summary:        Intel CPU undervolting and throttling configuration tool
Group:          System/Kernel and hardware
License:        GPLv3
URL:            https://github.com/kitsunyan/intel-undervolt
Source0:        https://github.com/kitsunyan/intel-undervolt/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires: pkgconfig(libsystemd)

%description
intel-undervolt is a tool for undervolting and throttling limits alteration for Intel CPUs.
Undervolting works on Haswell and newer CPUs and based on the content of this article.
Disclaimer
This tool may damage your hardware since it uses reverse engineered methods of MSR usage. Use it on your own risk.

%prep
%autosetup -p1

%configure --enable-systemd
%make_build

%install
%make_install

%files
%doc README*
%license COPYING
%{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_unitdir}/%{name}*.service
