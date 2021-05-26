%undefine _disable_source_fetch
Name: bob
Version: 2.0.0
Release: 0
License: Apache-2.0
Summary: Better Object Builder for IBM i
Url: https://github.com/edmundreinhardt/Bob/


BuildRequires: make-gnu
BuildRequires: tar-gnu
BuildRequires: gzip
Requires: bash
Requires: coreutils-gnu
Requires: jq
Requires: sed-gnu
Requires: grep-gnu
Requires: gawk
Requires: make-gnu

Source0: https://github.com/edmundreinhardt/Bob/archive/refs/tags/v%{version}.tar.gz
Source1: https://github.com/BrianGarland/CRTFRMSTMF/archive/16db76aba5c94243396297f022a0dfc39dd4f8ee.tar.gz

%description
Better Object Builder, or Bob, is a free and open source build system for the IBM i platform that is used to build native "QSYS" objects. 
Here's what makes Bob different.
- Speed. Bob only compiles objects that need recompiling, like from new or changed source code.
- Reliability. Bob understands the relationships between your objects, so if an item changes, then it and everything depending on it will be rebuilt.
- Industry standard. Object dependencies are specified using standard makefile syntax, and the actual build engine is GNU Make -- exactly like tens of thousands of Linux and Unix software projects.
- Flexibility. Most objects defined to Bob typically build using your default values. Have a program that requires a custom activation group or a data area that needs to be created with a certain value? No problem, overriding compile parameters is trivial, and writing custom recipes for special objects is very straightforward. If you can code it, you can build it.
- Ease of use. Invoking a build of an entire codebase is done with just a single command. Or, if the Rational Developer for i integration pieces are installed, a single button click.

%prep

%setup -n Bob-%{version}

%build
ls -la
echo "skipping build"

%install
rm -fr CRTFRMSTMF/*
tar xzvf %{SOURCE1} -C CRTFRMSTMF --strip-components=1
mkdir -p %{buildroot}%{_libdir}/bob
cp -r ./* %{buildroot}%{_libdir}/bob

%post -p %{_bindir}/bash
echo "post processing"

%files
%defattr(-, qsys, *none)
%{_libdir}/bob

%changelog
