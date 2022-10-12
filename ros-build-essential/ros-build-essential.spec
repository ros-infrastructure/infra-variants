Name: ros-build-essential
Version: 1.0.0
Summary: ROS Infrastructure variant including packages that are expected to be present when building any ROS packages.
Release: %{?dist}%{?release_suffix}
BuildArch: noarch
License: Apache-2.0
URL: https://github.com/ros-infrastructure/infra-variants
Source0: README.md
Source1: copyright

# TODO add packages from mock's default configuration.
Requires: cmake, g++, git, make, python3

%description
ROS Infrastructure variant including packages that are expected to be present when building any ROS packages.


%files
%doc %{SOURCE0}
%license %{SOURCE1}

%changelog
* Mon Oct 10 2022 Steven! Ragnarök - 1.0.0
- Initial package creation.
