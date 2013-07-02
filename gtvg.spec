Name:    gtvg
Summary: A Gnome TV Guide
Version: 0.3
Release: 13
Source0: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0: gtvg-0.3-libnotify0.7.patch
URL: http://gtvg.sourceforge.net/
License: GPL
Group: Graphical desktop/GNOME
BuildRequires: pkgconfig(libgnome-2.0)
BuildRequires: pkgconfig(libgnomecanvas-2.0)
BuildRequires: pkgconfig(libglade-2.0)
BuildRequires: pkgconfig(libnotify)
BuildRequires: intltool
BuildRequires: desktop-file-utils
BuildRequires: pkgconfig(sm)
BuildRequires: pkgconfig(ice)
BuildRequires: pkgconfig(gconf-2.0) GConf2
Requires: xmltv-grabbers

%description
Gtvg is a simple TV program schedule viewer, which allows you to quickly see 
what is on TV at the moment or later, and be reminded of when your favourite 
shows start.

It uses XMLTV as a backend to grab TV programs, but can be configured to use 
nxtvepg instead.

%prep
%setup -q
%patch0 -p0

%build
%configure2_5x --disable-schemas-install LIBS="-lm"
%make
										
%install
%makeinstall_std

desktop-file-install --vendor="" \
  --remove-category="Utility" \
  --remove-key="Encoding" \
  --remove-key="Version" \
  --remove-key="StartupNotify" \
  --add-category="X-MandrivaLinux-Multimedia-Video" \
  --dir %{buildroot}%{_datadir}/applications/ \
  %{buildroot}%{_datadir}/applications/*

rm -rf %{buildroot}/%{_prefix}/doc/%{name}
rm -f %{buildroot}%{_iconsdir}/hicolor/icon-theme.cache

%find_lang %{name}

%preun
%preun_uninstall_gconf_schemas "%{name}"

%files -f %{name}.lang
%doc AUTHORS ChangeLog
%{_sysconfdir}/gconf/schemas/%{name}.schemas
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*



%changelog
* Mon May 23 2011 Funda Wang <fwang@mandriva.org> 0.3-11mdv2011.0
+ Revision: 677727
- rebuild to add gconftool as req

* Sat Apr 30 2011 Funda Wang <fwang@mandriva.org> 0.3-10
+ Revision: 661031
- fix build with libnotify 0.7

* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3-9mdv2011.0
+ Revision: 619298
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.3-8mdv2010.0
+ Revision: 429345
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.3-7mdv2009.0
+ Revision: 246723
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Guillaume Bedot <littletux@mandriva.org> 0.3-5mdv2008.1
+ Revision: 121730
- do not launch gtvg when installing schemas

* Mon Dec 17 2007 Guillaume Bedot <littletux@mandriva.org> 0.3-4mdv2008.1
+ Revision: 121642
- fix icon cache conflict

* Fri Dec 14 2007 Guillaume Bedot <littletux@mandriva.org> 0.3-3mdv2008.1
+ Revision: 120077
- fix schemas installation

* Tue Dec 11 2007 Guillaume Bedot <littletux@mandriva.org> 0.3-2mdv2008.1
+ Revision: 117184
- builreq again.
- also increase mkrel.
- requires, menus and and description fixes.

* Mon Dec 10 2007 Guillaume Bedot <littletux@mandriva.org> 0.3-1mdv2008.1
+ Revision: 117000
- Buildreqs.
- First package for Mandriva Linux (0.3 from svn).
- create gtvg

