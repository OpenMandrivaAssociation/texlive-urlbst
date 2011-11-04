# revision 23262
# category Package
# catalog-ctan /biblio/bibtex/contrib/urlbst
# catalog-date 2011-07-21 09:04:20 +0200
# catalog-license gpl
# catalog-version 0.7
Name:		texlive-urlbst
Version:	0.7
Release:	1
Summary:	Web support for BibTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/biblio/bibtex/contrib/urlbst
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/urlbst.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/urlbst.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/urlbst.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Provides:	texlive-urlbst.bin = %{EVRD}
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Supports a new BibTeX 'webpage' entry type and 'url',
'lastchecked', and 'eprint' and 'DOI' fields. The Perl script
urlbst can be used to add this support to an arbitrary .bst
file which has a reasonably conventional structure. The result
is meant to be robust rather than pretty.

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
#- source
%doc %{_texmfdistdir}/source/bibtex/urlbst/configure
%doc %{_texmfdistdir}/source/bibtex/urlbst/configure.ac
%doc %{_tlpkgobjdir}/*.tlpobj

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
# remove bad "dependency" generation on @PERL@
rm -f texmf-dist/doc/bibtex/urlbst/urlbst.in
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
