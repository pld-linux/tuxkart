Summary:	Another game that stars Tux, the Linux Penguin
Summary(pl):	Kolejna gra z linuksowym pingwinem Tuksem
Name:		tuxkart
Version:	0.2.0
Release:	2
License:	GPL
Group:		X11/Applications/Games
Source0:	http://tuxkart.sourceforge.net/dist/%{name}-%{version}.tar.gz
# Source0-md5:	235683a252a9ae62793537944c1873bb
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-paths.patch
Patch1:		%{name}-ac_fixes.patch
URL:		http://tuxkart.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	plib >= 1.7.0-2
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1

%description
Another game that stars Tux, the Linux Penguin.

%description -l pl
Kolejna gra z linuksowym pingwinem Tuksem.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
CPPFLAGS="-I/usr/X11R6/include"; export CPPFLAGS
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/tuxkart,%{_applnkdir}/Games} \
	$RPM_BUILD_ROOT%{_pixmapsdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games/%{name}.desktop
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS CHANGES
%attr(755,root,root) %{_bindir}/*
%{_datadir}/tuxkart
%{_applnkdir}/Games/*
%{_pixmapsdir}/*
