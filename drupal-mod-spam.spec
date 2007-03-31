%define		modname spam
Summary:	Drupal Spam Module
Summary(pl.UTF-8):	Moduł Spam dla Drupala
Name:		drupal-mod-%{modname}
Version:	2.0.13
Release:	0.1
License:	BSD
Group:		Applications/WWW
Source0:	http://kerneltrap.org/jeremy/drupal/spam/spam-%{version}.tar.bz2
# Source0-md5:	e00cc205f912744ba0613d21618d5988
URL:		http://kerneltrap.org/jeremy/drupal/spam/
BuildRequires:	rpmbuild(macros) >= 1.194
Requires:	drupal >= 4.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/drupal
%define		_drupaldir	%{_datadir}/drupal
%define		_moddir		%{_drupaldir}/modules
%define		_incdir		%{_drupaldir}/includes
%define		_htdocs		%{_drupaldir}/htdocs
%define		_podir		%{_drupaldir}/po/%{modname}
%define		_htmlmoddir	%{_htdocs}/modules
%define		_htmlmoddir	%{_htdocs}/modules/%{modname}

%description
The spam module is a powerful collection of tools designed to help
website administrators to automatically deal with spam. Spam is any
content that is posted to a website that is unrelated to the subject
at hand, usually in the form of advertising and links back to the
spammer's own website. This module can automatically detect spam,
instantly unpublish it, and send notification to the site
administrator.

%description -l pl.UTF-8
Moduł spam to potężny zbiór narzędzi przygotowanych aby pomóc
administratorom serwisów WWW automatycznie radzić sobie ze spamem.
Spam to dowolna treść wysyłana na stronę nie związana z tematem,
zwykle w postaci reklam i odnośników do własnego serwisu spamera. Ten
moduł potrafi automatycznie wykrywać spam, natychmiast anulować jego
publikację i wysłać powiadomienie do administratora serwisu.

%prep
%setup -q -n %{modname}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_moddir}

install *.module $RPM_BUILD_ROOT%{_moddir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ "$1" = 1 ]; then
%banner -e %{name} <<EOF
To create Spam MySQL database tables, import:
zcat %{_docdir}/%{name}-%{version}/%{modname}.mysql.gz | mysql drupal
For Postgresql file is:
%{_docdir}/%{name}-%{version}/%{modname}.pgsql.gz
EOF
fi

%files
%defattr(644,root,root,755)
%doc *.txt
%doc %{modname}.{mysql,pgsql}
%{_moddir}/*.module
