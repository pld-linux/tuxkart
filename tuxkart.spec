Summary:	Another game that stars Tux, the Linux Penguin
Summary(pl.UTF-8):	Kolejna gra z linuksowym pingwinem Tuksem
Name:		tuxkart
Version:	0.4.0
Release:	2
License:	GPL
Group:		X11/Applications/Games
Source0:	http://tuxkart.sourceforge.net/dist/%{name}-%{version}.tar.gz
# Source0-md5:	e84ab2748ff1ce5ef11d1d7da5188f8f
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-paths.patch
Patch1:		%{name}-ac_fixes.patch
Patch2:		%{name}-parport.patch
URL:		http://tuxkart.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	plib-devel >= 1.8.0
Requires:	OpenGL
Requires:	plib >= 1.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1

%description
Another game that stars Tux, the Linux Penguin.

%description -l pl.UTF-8
Kolejna gra z linuksowym pingwinem Tuksem.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
CPPFLAGS="-I/usr/X11R6/include"; export CPPFLAGS
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/tuxkart,%{_desktopdir}} \
	$RPM_BUILD_ROOT%{_pixmapsdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS CHANGES
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
