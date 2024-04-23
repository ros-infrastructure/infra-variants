Name: ros-dev-tools
Version: 1.0.1
Summary: Developer Tools for ROS
Release: 1%{?dist}%{?release_suffix}
BuildArch: noarch
License: ASL 2.0
URL: https://github.com/ros-infrastructure/infra-variants
Source0: README.md
Source1: copyright
Requires: ros-build-essential
Requires: python3-bloom
Requires: python3-colcon-common-extensions
Requires: python3-colcon-mixin
Requires: python3-rosdep
Requires: python3-vcstool
Requires: wget

%description
Variant which includes packages generally useful during ROS development.

%prep
cp -a %{SOURCE0} %{SOURCE1} .

%build

%install

%files
%doc README.md
%license copyright

%changelog
* Tue Apr 23 2024 Scott K Logan - 1.0.1-1
- Add python3-colcon-mixin to ros-dev-tools variant

* Mon Oct 10 2022 Steven! Ragnarök - 1.0.0-1
- Initial package creation.
