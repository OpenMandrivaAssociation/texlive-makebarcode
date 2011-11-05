# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/makebarcode
# catalog-date 2008-08-22 15:19:59 +0200
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-makebarcode
Version:	1.0
Release:	1
Summary:	Print various kinds 2/5 and Code 39 bar codes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/makebarcode
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/makebarcode.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/makebarcode.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package contains macros for printing various 2/5 bar codes
and Code 39 bar codes. The macros do not use fonts but create
the bar codes directly using vertical rules. It is therefore
possible to vary width to height ratio, ratio of thin and thick
bars. The package is therefore convenient for printing ITF bar
codes as well as bar codes for identification labels for HP
storage media.

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
%{_texmfdistdir}/tex/latex/makebarcode/makebarcode.sty
%doc %{_texmfdistdir}/doc/latex/makebarcode/License.txt
%doc %{_texmfdistdir}/doc/latex/makebarcode/README
%doc %{_texmfdistdir}/doc/latex/makebarcode/makebarcode.pdf
%doc %{_texmfdistdir}/doc/latex/makebarcode/makebarcode.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
