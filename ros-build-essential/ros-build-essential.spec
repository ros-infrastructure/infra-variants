Name: ros-build-essential
Version: 1.0.0
Summary: Packages expected when building any ROS package
Release: 1%{?dist}%{?release_suffix}
BuildArch: noarch
License: ASL 2.0
URL: https://github.com/ros-infrastructure/infra-variants
Source0: README.md
Source1: copyright

# TODO add packages from mock's default configuration.
Requires: cmake, gcc-c++, git, make, python3

%description
ROS Infrastructure variant including packages that are expected to be present
when building any ROS packages.

%prep
cp -a %{SOURCE0} %{SOURCE1} .

%files
%doc README.md
%license copyright

%changelog
* Mon Oct 10 2022 Steven! Ragnarök - 1.0.0-1
- Initial package creation.
