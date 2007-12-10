%define name gtvg
%define version 0.3
%define release %mkrel 1

Name: %{name}
Summary: Gtvg - A Gnome TV Guide
Version: %{version}
Release: %{release}
Source: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
URL: http://gtvg.sourceforge.net/
License: GPL
Group: Graphical desktop/GNOME
BuildRoot: %{_tmppath}/%{name}-buildroot
#BuildRequires:
#Requires:

%description
Gtvg is a simple TV program schedule viewer, which allows you to quickly see 
what is on TV at the moment or later, and be reminded of when your favourite 
shows start.

%prep
%setup -q

%build
%configure2_5x

%make
										
%install
rm -rf %{buildroot}
%makeinstall

rm -rf %{buildroot}/%{_prefix}/doc/%{name}

%find_lang %{name}

%post
%post_install_gconf_schemas %{name}
%update_icon_cache hicolor

%preun
%preun_uninstall_gconf_schemas %{name}

%postun
%update_icon_cache hicolor

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

