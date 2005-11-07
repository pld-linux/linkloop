Summary:	Link level connectivity testing tool
Summary(pl):	Narzêdzie do sprawdzania ³±czno¶ci w warstwie po³±czenia
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

%description -l pl
Ten program jest podobny do pinga, ale sprawdza ³±czno¶æ w warstwie
po³±czenia (warstwie 2) zamiast na poziomie sieci (warstwie 3). Dzia³a
podobnie do narzêdzia linkloop z HP-UX-a. By³o testowane miêdzy
Linuksem i HP-UX-em (w obie strony). Jest tak¿e narzêdzie
"server-side" dla Linuksa (linkloop_reply). S± plany przeniesienia
obs³ugi odpowiadania do j±dra.

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
