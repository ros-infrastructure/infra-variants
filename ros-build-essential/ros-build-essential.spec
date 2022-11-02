Name: ros-build-essential
Version: 1.0.0
Summary: Packages expected when building any ROS package
Release: 1%{?dist}%{?release_suffix}
BuildArch: noarch
License: ASL 2.0
URL: https://github.com/ros-infrastructure/infra-variants
Source0: README.md
Source1: copyright

# Includes packages from mock's default configuration for Almalinux 8 plus ROS-specfic build packages.
# https://github.com/rpm-software-management/mock/blob/0e7e8db8489563cbd6a21378860f45828c25a99b/mock-core-configs/etc/mock/templates/almalinux-8.tpl#L1
Requires: bash
Requires: bzip2
Requires: coreutils
Requires: cpio
Requires: diffutils
Requires: findutils
Requires: gawk
Requires: gcc
Requires: gcc-c++
Requires: grep
Requires: gzip
Requires: info
Requires: make
Requires: patch
Requires: redhat-release
Requires: redhat-rpm-config
Requires: rpm-build
Requires: sed
Requires: shadow-utils
Requires: tar
Requires: unzip
Requires: util-linux
Requires: which
Requires: xz
# Additional packages as specified in REP-2001.
Requires: cmake
Requires: gcc-c++
Requires: git
Requires: python3
Requires: python3-setuptools

%description
Variant which includes packages that are expected to be present when building
any ROS packages.

%prep
cp -a %{SOURCE0} %{SOURCE1} .

%build

%install

%files
%doc README.md
%license copyright

%changelog
* Mon Oct 10 2022 Steven! Ragnarök - 1.0.0-1
- Initial package creation.
