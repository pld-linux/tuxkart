Summary:	Another game that stars Tux, the Linux Penguin
Summary(pl):	Kolejna gra z linuksowym pingwinem Tuksem
Name:		tuxkart
Version:	0.0.6
Release:	1
License:	GPL
Group:		X11/Applications/Games
Group(de):	X11/Applikationen/Spiele
Group(pl):	X11/Aplikacje/Gry
Source0:	http://tuxkart.sourceforge.net/dist/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-paths.patch
URL:		http://tuxkart.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	plib
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1
%define		_prefix		/usr/X11R6

%description
Another game that stars Tux, the Linux Penguin.

%description -l pl
Kolejna gra z linuksowym pingwinem Tuksem.

%prep
%setup -q
%patch0 -p1

%build
automake -a
aclocal
autoconf
%configure CPPFLAGS="-I%{_includedir}"
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/tuxkart,%{_applnkdir}/Games}

%{__make} install DESTDIR="$RPM_BUILD_ROOT"

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games/%{name}.desktop

gzip -9nf README AUTHORS CHANGES 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/tuxkart
%{_applnkdir}/Games/*
