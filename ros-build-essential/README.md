# ROS Build Essential

`ros-build-essential` includes packages that are expected to be present when building any ROS packages without an explicit dependency.
It should include the base toolchain for any operating system (such as `build-essential`) on Debian as well as Make and a C++ compiler if not already part of that toolchain.

### Platform-specific build toolchains

This variant is meant primarily for internal use by the ROS Infrastructure team to set up the environment in which packages will be built on the ROS build farm.
Since this package is used by the more user-facing ros-dev-tools variant as well, it can be useful to define the variant for platforms that are not currently enabled, or potentially even supported, by the build farm infrastructure.
When selecting packages to include in this variant, the platform's own build toolchain, including any utilities used in the package creation process, should be used as a starting point.
For example the `build-essential` package in Debian, `base-devel` in Arch Linux, or the `Development Tools` group in RHEL.

If the default build toolchain for a distribution does not include GNU Make and a C++ compiler, those should be included as well.


### Additional packages included in this variant

* cmake
* git
* python3
