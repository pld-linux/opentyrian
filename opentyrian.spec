%define		snap	20110209
Summary:	Arcade-style vertical scrolling shooter
Name:		opentyrian
Version:	0
Release:	0.%{snap}
License:	GPL v2, freeware (artwork)
Group:		X11/Applications/Games
Source0:	%{name}-0.%{snap}.tar.bz2
# Source0-md5:	1388f4d0fa902f24c54134203ccd0337
Source1:	http://camanis.net/tyrian/tyrian21.zip
# Source1-md5:	c3b8400abb2d9dd45d2e3c3fb5ce1563
URL:		http://code.google.com/p/opentyrian/
BuildRequires:	SDL_net-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tyrian is an arcade-style vertical scrolling shooter. The story is set
in 20,031 where you play as Trent Hawkins, a skilled fighter-pilot
employed to fight MicroSol and save the galaxy.

Tyrian features a story mode, one- and two-player arcade modes, and
networked multiplayer.

%prep
%setup -q -n %{name} -a1
%{__rm} tyrian21/{dpmi16bi.ovl,*.{exe,int},{net*,shipedit,tyrset}.pcx,exitmsg.bin,file_id.diz,{helpme,license,order}.doc,order.tfp,setup.{box,ini},modems.txt}

%build
%{__make} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}/data,%{_mandir}/man6,%{_desktopdir},%{_pixmapsdir}}

install %{name} $RPM_BUILD_ROOT%{_bindir}
cp -a linux/man/opentyrian.6 $RPM_BUILD_ROOT%{_mandir}/man6
cp -a linux/opentyrian.desktop $RPM_BUILD_ROOT%{_desktopdir}
cp -a linux/icons/tyrian-*.png $RPM_BUILD_ROOT%{_pixmapsdir}
cp -a tyrian21/* $RPM_BUILD_ROOT%{_datadir}/%{name}/data

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS NEWS README doc/*
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/tyrian-*.png
%{_mandir}/man6/%{name}.6*
