Name:		texlive-makebarcode
Version:	15878
Release:	1
Summary:	Print various kinds 2/5 and Code 39 bar codes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/makebarcode
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/makebarcode.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/makebarcode.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package contains macros for printing various 2/5 bar codes
and Code 39 bar codes. The macros do not use fonts but create
the bar codes directly using vertical rules. It is therefore
possible to vary width to height ratio, ratio of thin and thick
bars. The package is therefore convenient for printing ITF bar
codes as well as bar codes for identification labels for HP
storage media.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/makebarcode/makebarcode.sty
%doc %{_texmfdistdir}/doc/latex/makebarcode/License.txt
%doc %{_texmfdistdir}/doc/latex/makebarcode/README
%doc %{_texmfdistdir}/doc/latex/makebarcode/makebarcode.pdf
%doc %{_texmfdistdir}/doc/latex/makebarcode/makebarcode.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
