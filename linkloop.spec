Summary:	Link level connectivity testing tool
Name:		linkloop
Version:	0.0.1
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	http://users.actcom.co.il/~oron/oron/docs/%{name}-%{version}.tar.gz
# Source0-md5:	8dfb7d0ad598d5aa94bab37fe5634cf2
URL:		http://users.actcom.co.il/~oron/oron/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program is similar to ping, but tests connectivity at the link
layer (layer 2) instead of the network layer (layer 3). This works
like the HP-UX linkloop utility. It was tested between Linux and HP-UX
(both ways). There is also a "server-side" utility for Linux
(linkloop_reply). There are plans to move the "reply" support into the
kernel.

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
