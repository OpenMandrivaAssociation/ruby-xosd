%define rname xosd
%define name ruby-%{rname}
%define version 1.1.0
%define release 2mdk

Summary: Ruby bindings for xosd
Name: %{name}
Version: %{version}
Release: %{release}
URL: http://djur.desperance.net/ruby/
Source0: %{name}-%{version}.tar.bz2
License: Historical Permission Notice and Disclaimer
Group: Development/Other
BuildRoot: %{_tmppath}/%{name}-buildroot
Requires: ruby 
BuildRequires: ruby-devel xosd-devel

%define ruby_archdir %(ruby -rrbconfig -e 'puts Config::CONFIG["sitearchdir"]')

%description
ruby-xosd is a simple binding to the xosd library for the Ruby programming 
language that allows displaying of arbitrary notifications in X11.
It is useful for on-screen notifications; in addition to single or multi-line
text displays, xosd also provides "slider" and "progress bar" style displays,
which can be mixed and matched with text in the same display.

An xosd window is a shaped, unmanaged window on top of all others. It lasts
as long as its parent process is running or until it is hidden or destroyed.

%prep
%setup -q
sed -i 's|/lib|/%{_lib}|g' extconf.rb

%build
ruby extconf.rb
make

%install
rm -rf %buildroot
%makeinstall

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%{ruby_archdir}/*.so
%doc COPYING TODO

