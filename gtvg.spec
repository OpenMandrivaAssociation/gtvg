%define name gtvg
%define version 0.3
%define release %mkrel 9

Name: %{name}
Summary: Gtvg - A Gnome TV Guide
Version: %{version}
Release: %{release}
Source: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
URL: http://gtvg.sourceforge.net/
License: GPL
Group: Graphical desktop/GNOME
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: libgnome2-devel
BuildRequires: libgnomecanvas2-devel
BuildRequires: libglade2-devel
BuildRequires: libnotify-devel
BuildRequires: intltool
BuildRequires: desktop-file-utils
Requires: xmltv-grabbers

%description
Gtvg is a simple TV program schedule viewer, which allows you to quickly see 
what is on TV at the moment or later, and be reminded of when your favourite 
shows start.

It uses XMLTV as a backend to grab TV programs, but can be configured to use 
nxtvepg instead.

%prep
%setup -q

%build
%configure2_5x

%make
										
%install
rm -rf %{buildroot}
%makeinstall

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

%if %mdkversion < 200900
%post
%update_menus
%post_install_gconf_schemas "%{name}"
%update_icon_cache hicolor
%endif

%preun
%preun_uninstall_gconf_schemas "%{name}"

%if %mdkversion < 200900
%postun
%clean_menus
%update_icon_cache hicolor
%endif

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog
%{_sysconfdir}/gconf/schemas/%{name}.schemas
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*

