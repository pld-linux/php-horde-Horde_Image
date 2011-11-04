# TODO
# - system locale dir
%define		status		stable
%define		pearname	Horde_Image
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - Horde Image API
Name:		php-horde-Horde_Image
Version:	1.0.7
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.horde.org/get/%{pearname}-%{version}.tgz
# Source0-md5:	8cd676d99db0bff05a9724b8f8815e7a
URL:		https://github.com/horde/horde/tree/master/framework/Image/
BuildRequires:	php-channel(pear.horde.org)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR >= 1:1.7.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php-channel(pear.horde.org)
Requires:	php-horde-Horde_Exception < 2.0.0
Requires:	php-horde-Horde_Support < 2.0.0
Requires:	php-horde-Horde_Translation < 2.0.0
Requires:	php-horde-Horde_Util < 2.0.0
Requires:	php-pear >= 4:1.3.6-2
Suggests:	php-gd
Suggests:	php-json
Suggests:	php-pear-XML_SVG
Suggests:	php-zlib
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	 pear(XML/SVG.*)

%description
This package provides an Image utility API, with backends for:
- GD
- GIF
- PNG
- SVG
- SWF
- ImageMagick convert command line tool
- Imagick Extension

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%doc optional-packages.txt
%{php_pear_dir}/.registry/.channel.*/*.reg
%{php_pear_dir}/Horde/Image.php
%{php_pear_dir}/Horde/Image
%{php_pear_dir}/data/Horde_Image
