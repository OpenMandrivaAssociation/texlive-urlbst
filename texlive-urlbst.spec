Name:		texlive-urlbst
Version:	65190
Release:	1
Summary:	Web support for BibTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/biblio/bibtex/contrib/urlbst
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/urlbst.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/urlbst.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/urlbst.source.r%{version}.tar.xz
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
%{_texmfdistdir}/bibtex/bst/urlbst
%{_texmfdistdir}/scripts/urlbst
%doc %{_texmfdistdir}/doc/bibtex/urlbst
#- source
%doc %{_texmfdistdir}/source/bibtex/urlbst

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -sf %{_texmfdistdir}/scripts/urlbst/urlbst urlbst
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
