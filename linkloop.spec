Summary:	Link level connectivity testing tool
Summary(pl.UTF-8):	Narzędzie do sprawdzania łączności w warstwie połączenia
Name:		linkloop
Version:	0.0.2
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	http://users.actcom.co.il/~oron/oron/docs/%{name}-%{version}.tar.gz
# Source0-md5:	00ea5fecd0fb73c08626232ae322ac1a
URL:		http://users.actcom.co.il/~oron/oron/oron_main.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program is similar to ping, but tests connectivity at the link
layer (layer 2) instead of the network layer (layer 3). This works
like the HP-UX linkloop utility. It was tested between Linux and HP-UX
(both ways). There is also a "server-side" utility for Linux
(linkloop_reply). There are plans to move the "reply" support into the
kernel.

%description -l pl.UTF-8
Ten program jest podobny do pinga, ale sprawdza łączność w warstwie
połączenia (warstwie 2) zamiast na poziomie sieci (warstwie 3). Działa
podobnie do narzędzia linkloop z HP-UX-a. Było testowane między
Linuksem i HP-UX-em (w obie strony). Jest także narzędzie
"server-side" dla Linuksa (linkloop_reply). Są plany przeniesienia
obsługi odpowiadania do jądra.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/linkloop.1*
