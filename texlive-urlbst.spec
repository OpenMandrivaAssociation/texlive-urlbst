%global tl_name urlbst
%global tl_revision 76790

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.9.1
Release:	%{tl_revision}.1
Summary:	Web support for BibTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/biblio/bibtex/contrib/urlbst
License:	gpl2 lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/urlbst.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/urlbst.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/urlbst.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(urlbst.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Supports a new BibTeX 'webpage' entry type and 'url', 'lastchecked', and
'eprint' and 'DOI' fields. The Perl script urlbst can be used to add
this support to an arbitrary .bst file which has a reasonably
conventional structure. The result is meant to be robust rather than
pretty.

