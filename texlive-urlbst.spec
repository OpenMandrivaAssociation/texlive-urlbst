# revision 29803
# category Package
# catalog-ctan /biblio/bibtex/contrib/urlbst
# catalog-date 2011-11-15 11:50:22 +0100
# catalog-license gpl
# catalog-version 0.7
Name:		texlive-urlbst
Version:	0.7
Release:	12
Summary:	Web support for BibTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/biblio/bibtex/contrib/urlbst
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/urlbst.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/urlbst.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/urlbst.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-urlbst.bin = %{EVRD}

%description
Supports a new BibTeX 'webpage' entry type and 'url',
'lastchecked', and 'eprint' and 'DOI' fields. The Perl script
urlbst can be used to add this support to an arbitrary .bst
file which has a reasonably conventional structure. The result
is meant to be robust rather than pretty.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/urlbst
%{_texmfdistdir}/bibtex/bst/urlbst/abbrvurl.bst
%{_texmfdistdir}/bibtex/bst/urlbst/alphaurl.bst
%{_texmfdistdir}/bibtex/bst/urlbst/plainurl.bst
%{_texmfdistdir}/bibtex/bst/urlbst/unsrturl.bst
%{_texmfdistdir}/scripts/urlbst/urlbst
%doc %{_texmfdistdir}/doc/bibtex/urlbst/Makefile.in
%doc %{_texmfdistdir}/doc/bibtex/urlbst/README
%doc %{_texmfdistdir}/doc/bibtex/urlbst/VERSION
%doc %{_texmfdistdir}/doc/bibtex/urlbst/urlbst.bib
%doc %{_texmfdistdir}/doc/bibtex/urlbst/urlbst.html
%doc %{_texmfdistdir}/doc/bibtex/urlbst/urlbst.html.in
%doc %{_texmfdistdir}/doc/bibtex/urlbst/urlbst.in
%doc %{_texmfdistdir}/doc/bibtex/urlbst/urlbst.pdf
%doc %{_texmfdistdir}/doc/bibtex/urlbst/urlbst.tex
%doc %{_texmfdistdir}/doc/bibtex/urlbst/urlbst.tex.in
#- source
%doc %{_texmfdistdir}/source/bibtex/urlbst/configure
%doc %{_texmfdistdir}/source/bibtex/urlbst/configure.ac

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/urlbst/urlbst urlbst
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
