
%define name	bsdiff
%define version	4.3
%define rel	3

%define release %mkrel %rel

Summary:	Binary diff/patch utility
Name:		%name
Version:	%version
Release:	%release
Group:		File tools
License:	BSD
URL:		http://www.daemonology.net/bsdiff/
Source:		http://www.daemonology.net/bsdiff/%name-%version.tar.gz
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	bzip2-devel

%description
bsdiff and bspatch are tools for building and applying patches to
binary files. By using suffix sorting (specifically, Larsson and
Sadakane's qsufsort) and taking advantage of how executable files
change, bsdiff routinely produces binary patches 50-80%% smaller
than those produced by Xdelta, and 15%% smaller than those produced
by .RTPatch.

These programs were originally named bdiff and bpatch, but the large
number of other programs using those names lead to confusion; I'm
not sure if the "bs" in refers to "binary software" (because bsdiff
produces exceptionally small patches for executable files) or
"bytewise subtraction" (which is the key to how well it performs).
Feel free to offer other suggestions.

%prep
%setup -q

%build
%__cc %optflags -lbz2 bsdiff.c -o bsdiff
%__cc %optflags -lbz2 bspatch.c -o bspatch

%install
rm -rf %{buildroot}

install -D -m755 bsdiff %{buildroot}%{_bindir}/bsdiff
install -D -m755 bspatch %{buildroot}%{_bindir}/bspatch

install -D -m644 bsdiff.1 %{buildroot}%{_mandir}/man1/bsdiff.1
install -D -m644 bspatch.1 %{buildroot}%{_mandir}/man1/bspatch.1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/bsdiff
%{_bindir}/bspatch
%{_mandir}/man1/bsdiff.1*
%{_mandir}/man1/bspatch.1*


