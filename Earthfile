VERSION 0.6

equivs:
  FROM ubuntu:bionic
  RUN apt-get update
  RUN apt-get install -y equivs lintian

rpmbuild:
  FROM almalinux:8
  RUN dnf install -y rpmdevtools rpmlint

RPM:
  COMMAND
  ARG package
  FROM +rpmbuild
  COPY $package /tmp/$package
  WORKDIR /tmp/$package
  RUN rpmbuild -ba ${package}.spec --define "_topdir /tmp/$package/rpm" --define "_sourcedir /tmp/$package"
  RUN rpmlint /tmp/$package/rpm/RPMS/noarch/${package}*.rpm /tmp/$package/rpm/SRPMS/${package}*.src.rpm
  SAVE ARTIFACT /tmp/$package/rpm/RPMS/noarch/${package}*.rpm AS LOCAL output/
  SAVE ARTIFACT /tmp/$package/rpm/SRPMS/${package}*.src.rpm AS LOCAL output/

DEB:
  COMMAND
  ARG package
  FROM +equivs
  COPY $package /tmp/$package
  WORKDIR /tmp/$package
  RUN equivs-build ${package}.control
  RUN lintian --suppress-tags empty-binary-package ${package}_*.deb
  SAVE ARTIFACT ${package}_*.deb AS LOCAL output/

ros-dev-tools-rpm:
  DO +RPM --package=ros-dev-tools

ros-dev-tools-deb:
  DO +DEB --package=ros-dev-tools

ros-build-essential-deb:
  DO +DEB --package=ros-build-essential

ros-build-essential-rpm:
  DO +RPM --package=ros-build-essential

check-debs:
  FROM ubuntu:jammy
  ARG DEBIAN_FRONTEND=noninteractive
  RUN apt update && apt install -y curl gnupg2
  RUN echo 'deb http://packages.ros.org/ros2/ubuntu jammy main' > /etc/apt/sources.list.d/ros2.list
  RUN curl 'https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc' | apt-key add -
  RUN apt update
  COPY +ros-build-essential-deb/ros-build-essential*.deb ./
  RUN dpkg -i *.deb || true
  RUN apt install -yf
  RUN dpkg -i *.deb
  COPY +ros-dev-tools-deb/ros-dev-tools*.deb ./
  RUN dpkg -i *.deb || true
  RUN apt install -yf
  RUN dpkg -i *.deb

check-rpms:
  FROM almalinux:8
  RUN dnf install -y dnf-command\(config-manager\) && dnf config-manager --set-enabled powertools && dnf install -y epel-release
  COPY +ros-build-essential-rpm/ros-build-essential*.noarch.rpm ./
  RUN dnf install -y *.rpm
  COPY +ros-dev-tools-rpm/ros-dev-tools*.noarch.rpm ./
  RUN dnf install -y *.rpm
