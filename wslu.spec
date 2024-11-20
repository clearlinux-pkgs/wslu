#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: make
# autospec version: v21
# autospec commit: 5424026
#
Name     : wslu
Version  : 4.1.4
Release  : 5
URL      : https://github.com/wslutilities/wslu/archive/v4.1.4/wslu-4.1.4.tar.gz
Source0  : https://github.com/wslutilities/wslu/archive/v4.1.4/wslu-4.1.4.tar.gz
Summary  : A collection of utilities for the Windows Subsystem for Linux
Group    : Development/Tools
License  : GPL-3.0 GPL-3.0-or-later MIT
Requires: wslu-bin = %{version}-%{release}
Requires: wslu-data = %{version}-%{release}
Requires: wslu-license = %{version}-%{release}
Requires: wslu-man = %{version}-%{release}
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This is a collection of utilities for Windows 10 Linux Subsystem, such as converting WSL path to Windows path or creating your favorite linux app shortcuts on Windows 10 Desktop. Requires Windows 10 Creators Update and higher.

%package bin
Summary: bin components for the wslu package.
Group: Binaries
Requires: wslu-data = %{version}-%{release}
Requires: wslu-license = %{version}-%{release}

%description bin
bin components for the wslu package.


%package data
Summary: data components for the wslu package.
Group: Data

%description data
data components for the wslu package.


%package license
Summary: license components for the wslu package.
Group: Default

%description license
license components for the wslu package.


%package man
Summary: man components for the wslu package.
Group: Default

%description man
man components for the wslu package.


%prep
%setup -q -n wslu-4.1.4
cd %{_builddir}/wslu-4.1.4
pushd ..
cp -a wslu-4.1.4 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1732119136
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
make  %{?_smp_mflags}

pushd ../buildavx2
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1732119136
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/wslu
cp %{_builddir}/wslu-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/wslu/31a3d460bb3c7d98845187c716a30db81c44b615 || :
cp %{_builddir}/wslu-%{version}/THIRD_PARTY_LICENSE %{buildroot}/usr/share/package-licenses/wslu/fc646e897c796c06938ceae56a5ee7a2c97e88ba || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/wslact
/usr/bin/wslclip
/usr/bin/wslfetch
/usr/bin/wslgsu
/usr/bin/wslsys
/usr/bin/wslupath
/usr/bin/wslusc
/usr/bin/wslvar
/usr/bin/wslview

%files data
%defattr(-,root,root,-)
/usr/share/applications/wslview.desktop
/usr/share/wslu/conf
/usr/share/wslu/get_dpi.ps1
/usr/share/wslu/runHidden.vbs
/usr/share/wslu/sudo.ps1
/usr/share/wslu/wsl-gui.ico
/usr/share/wslu/wsl-term.ico
/usr/share/wslu/wsl.ico
/usr/share/wslu/wslusc-helper.sh

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/wslu/31a3d460bb3c7d98845187c716a30db81c44b615
/usr/share/package-licenses/wslu/fc646e897c796c06938ceae56a5ee7a2c97e88ba

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/wslact.1.gz
/usr/share/man/man1/wslclip.1.gz
/usr/share/man/man1/wslfetch.1.gz
/usr/share/man/man1/wslgsu.1.gz
/usr/share/man/man1/wslsys.1.gz
/usr/share/man/man1/wslupath.1.gz
/usr/share/man/man1/wslusc.1.gz
/usr/share/man/man1/wslvar.1.gz
/usr/share/man/man1/wslview.1.gz
/usr/share/man/man7/wslu.7.gz
