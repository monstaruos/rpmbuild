%global commit1 b5cc0083a5766e773885e8dd624c51a967c17de0
%global commit2 e09b87bfe2b3ad6004d31894ee58bd611c8e3e39

Name:           phantomjs
Version:        2.1.1
Release:        2%{?dist}
Summary:        Scriptable Headless WebKit

License:        BSD
Source0:        https://github.com/ariya/phantomjs/archive/%{version}.tar.gz
Source1:        https://github.com/Vitallium/qtbase/archive/%{commit1}.tar.gz#/qtbase-%{commit1}.tar.gz
Source2:        https://github.com/Vitallium/qtwebkit/archive/%{commit2}.tar.gz#/qtwebkit-%{commit2}.tar.gz
Patch1:         unset-QT_QPA_PLATFORM.patch
Patch2:         handle-empty-stack.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  gperf
BuildRequires:  ruby
BuildRequires:  openssl-devel
BuildRequires:  freetype-devel
BuildRequires:  fontconfig-devel
BuildRequires:  libicu-devel
BuildRequires:  sqlite-devel
BuildRequires:  libpng-devel
BuildRequires:  libjpeg-devel

%description
PhantomJS is a headless WebKit scriptable with a JavaScript API. It has fast and
native support for various web standards: DOM handling, CSS selector, JSON,
Canvas, and SVG.

%prep
%setup -qn %{name}-%{version}
tar -zxf %{SOURCE1} -C src/qt/qtbase   --strip-components=1
tar -zxf %{SOURCE2} -C src/qt/qtwebkit --strip-components=1

%patch1 -p1
%patch2 -p1

%build
# github issue #13930
touch src/qt/qtbase/.git
touch src/qt/qtwebkit/.git

python build.py --confirm --release --silent

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/%{name}/examples
cp bin/%{name} %{buildroot}%{_bindir}/%{name}
cp examples/* %{buildroot}%{_datadir}/%{name}/examples/

%files
%defattr(-,root,root)
%doc ChangeLog CONTRIBUTING.md LICENSE.BSD README.md
%{_bindir}/%{name}
%{_datadir}/%{name}

%changelog
* Tue Jun 12 2018 teruo.oshida@monstar-lab.com
- Backport PR 14111 (issue 14110)
  * Handle empty stack processing onError
* Mon Jun 12 2017 grainger@gmail.com
- Convert Suse SPEC file for use with EL7.
* Fri Dec  9 2016 qantas94heavy@gmail.com
- Downgrade phantomjs to 2.1.1
  * Fixes issue where PhantomJS crashes on startup (boo#1008760)
- Add unset-QT_QPA_PLATFORM.patch:
  * Stops PhantomJS crashing due to wrong Qt plugin type used
* Fri Jul  1 2016 toddrme2178@gmail.com
- Fix typo in Group tag.
* Sun May 29 2016 ro@suse.de
- update to version 2.1.1+git20160526.6090f54
* Sun May 29 2016 i@marguerite.su
- Update to version 2.1.1+git20160526.6090f54:
  * Disable QPA platform guard
  * Handle QtInfoMsg
  * Fix building with MSVC2015
  * Update QtWebkit module
  * Fixed typo
  * Upgrade example to run with Jasmine 2.4.1
  * Fix 'qt_config' problem.
  * Update request error message.
  * Update build.py to disable qtbase/qtwebkit unwanted features
  * [OS X] Allow building with custom OpenSSL library
* Mon Feb  1 2016 i@marguerite.su
- update version 2.1.1+git20160125.482b91d
* Thu Dec 25 2014 boris@steki.net
- update to latest release 1.9.8
  + Change default SSL protocol to TLSv1 to address POODLE (issue 12655)
  + Fixed building on OS X 10.10 Yosemite (issue 12622)
  + Backported crash fix when exit (issue 11642, 12431)
* Wed Aug  6 2014 toddrme2178@gmail.com
- Update source to point to website
- Minor spec file cleanups
- Update to 1.9.7
  * Reverted to GhostDriver 1.1.0 instead of 1.1.1 (issue 11915)
  * Fixed another warning of obsolete userSpaceScaleFactor on OS X 10.9 (issue 11612)
- Update to 1.9.6
  * Updated GhostDriver to version 1.1.1 (issue 11877, 11893)
- Update to 1.9.3
  * Fixed CoreText performance note on OS X 10.9 (issue 11418)
  * Fixed warning of obsolete userSpaceScaleFactor on OS X 10.9 (issue 11612)
- Update to 1.9.2
  * Fixed graphical artifacts with transparent background on Windows (issue 11276, 11007, 11366)
  * Updated GhostDriver to version 1.0.4 (issue 11452)
* Fri Jul 26 2013 boris@steki.net
- updated to version 1.9.1
* Tue Apr 30 2013 heydenberk@gmail.com
- add missing filenames for examples to files section
* Wed Apr 24 2013 lobbin@gmail.com
- updated to version 1.9
* Thu Jan 24 2013 mbarr@snap-interactive.com
- updated to version 1.8
* Thu Nov 15 2012 jschauma@etsy.com
- first rpm version
