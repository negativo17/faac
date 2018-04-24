Name:           faac
Version:        1.29.9.2
Release:        1%{?dist}
Summary:        Encoder and encoding library for MPEG2/4 AAC
License:        LGPLv2+
URL:            http://faac.sourceforge.net/

Source0:        http://downloads.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
#Patch0:         %{name}-libmp4v2.patch

BuildRequires:  libtool
BuildRequires:  libmp4v2-devel

%description
FAAC is an AAC audio encoder. It currently supports MPEG-4 LTP, MAIN and LOW
COMPLEXITY object types and MAIN and LOW MPEG-2 object types. It also supports
multichannel and gapless encoding.

%package devel
Summary:        Development libraries of the FAAC AAC encoder
Requires:       %{name} = %{version}-%{release}

%description devel
FAAC is an AAC audio encoder. It currently supports MPEG-4 LTP, MAIN and LOW
COMPLEXITY object types and MAIN and LOW MPEG-2 object types. It also supports
multichannel and gapless encoding.

This package contains development files and documentation for libfaac.

%prep
%setup -q -n %{name}-%{version}

# fix encoding
iconv -f iso8859-1 -t utf-8 AUTHORS > AUTHORS.conv && touch -r AUTHORS AUTHORS.conv && /bin/mv -f AUTHORS.conv AUTHORS

%build
autoreconf -vif
%configure --disable-static
%make_build

%install
%make_install

find %{buildroot} -name "*.la" -delete

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files 
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%{_bindir}/*
%{_libdir}/*.so.*
%{_mandir}/man1/%{name}*

%files devel
%{_libdir}/*.so
%{_includedir}/*.h

%changelog
* Tue Apr 24 2018 Simone Caronni <negativo17@gmail.com> - 1.29.9.2-1
- Update to 1.29.9.2.
- Update SPEC file.

* Sat Dec  6 2014 Nicolas Chauvet <kwizart@gmail.com> - 1.28-7
- Fix build with libmp4v2-devel - rfbz#3188
- Clean-up spec file
