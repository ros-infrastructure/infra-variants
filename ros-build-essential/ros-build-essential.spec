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
Requires: bash, bzip2, coreutils, cpio, diffutils, findutils, gawk, gcc, gcc-c++, grep, gzip, info, make, patch, redhat-release, redhat-rpm-config, rpm-build, sed, shadow-utils, tar, unzip, util-linux, which, xz, cmake, gcc-c++, git, python3

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
