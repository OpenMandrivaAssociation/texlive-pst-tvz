# revision 23451
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-tvz
# catalog-date 2011-06-14 17:30:27 +0200
# catalog-license lppl1.3
# catalog-version 1.01
Name:		texlive-pst-tvz
Version:	1.01
Release:	1
Summary:	Draw trees with more than on root node, using PSTricks
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-tvz
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-tvz.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-tvz.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-tvz.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package uses PSTricks to draw trees with more than one root
node. It is similar to pst-tree, though it uses a different
placement algorithm.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
