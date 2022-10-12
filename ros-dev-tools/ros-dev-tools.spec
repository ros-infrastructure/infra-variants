Name: ros-dev-tools
Version: 1.0
Summary: ROS Infrastructure variant including packages generally useful during ROS development.
Release: %{?dist}%{?release_suffix}
BuildArch: noarch
License: Apache-2.0
URL: https://github.com/ros-infrastructure/infra-variants
Source0: README.md
Source1: copyright
Requires: ros-build-essential, python3-bloom, python3-colcon-common-extensions, python3-rosdep, python3-vcstool

%description
ROS Infrastructure variant including packages generally useful during ROS development.

%files
%doc %{SOURCE0}
%license %{SOURCE1}

%changelog
* Mon Oct 10 2022 Steven! Ragnarök - 1.0.0
- Initial package creation.
