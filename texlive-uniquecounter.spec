Name:		texlive-uniquecounter
Version:	53162
Release:	2
Summary:	Provides unlimited unique counter
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/uniquecounter
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uniquecounter.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uniquecounter.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uniquecounter.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a kind of counter that provides unique
number values. Several counters can be created with different
names. The numeric values are not limited.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/uniquecounter
%{_texmfdistdir}/tex/generic/uniquecounter
%doc %{_texmfdistdir}/doc/latex/uniquecounter

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
