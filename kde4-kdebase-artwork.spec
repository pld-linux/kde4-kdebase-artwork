%define		_state		stable
%define		orgname		kde-base-artwork
%define		qtver		4.8.3

Summary:	K Desktop Environment - base artwork
Summary(pl.UTF-8):	K Desktop Environment - podstawowe grafiki itp.
Name:		kde4-kdebase-artwork
Version:	4.10.2
Release:	1
License:	LGPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	9fc21c80fe620efb931fa6ab2800ccda
URL:		http://www.kde.org/
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
Obsoletes:	kde4-splash-Default
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Default splashscreen that came with this version of KDE.

%description -l pl.UTF-8
Domyślny ekran powitalny dostarczony w tej wersji KDE.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/apps/ksplash/Themes/Default
