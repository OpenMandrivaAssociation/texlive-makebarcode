%global tl_name makebarcode
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Print various kinds 2/5 and Code 39 bar codes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/makebarcode
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/makebarcode.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/makebarcode.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package contains macros for printing various 2/5 bar codes and Code
39 bar codes. The macros do not use fonts but create the bar codes
directly using vertical rules. It is therefore possible to vary width to
height ratio, ratio of thin and thick bars. The package is therefore
convenient for printing ITF bar codes as well as bar codes for
identification labels for HP storage media.

