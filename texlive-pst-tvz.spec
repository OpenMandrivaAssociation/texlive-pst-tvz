Name:		texlive-pst-tvz
Version:	23451
Release:	1
Summary:	Draw trees with more than on root node, using PSTricks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-tvz
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-tvz.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-tvz.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-tvz.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package uses PSTricks to draw trees with more than one root
node. It is similar to pst-tree, though it uses a different
placement algorithm.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/pst-tvz/pst-tvz.tex
%{_texmfdistdir}/tex/latex/pst-tvz/pst-tvz.sty
%doc %{_texmfdistdir}/doc/generic/pst-tvz/Changes
%doc %{_texmfdistdir}/doc/generic/pst-tvz/README
%doc %{_texmfdistdir}/doc/generic/pst-tvz/pst-tvz-doc.bib
%doc %{_texmfdistdir}/doc/generic/pst-tvz/pst-tvz-doc.pdf
%doc %{_texmfdistdir}/doc/generic/pst-tvz/pst-tvz-doc.tex
#- source
%doc %{_texmfdistdir}/source/generic/pst-tvz/Makefile

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
