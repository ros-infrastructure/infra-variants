VERSION 0.6

equivs:
  FROM ubuntu:jammy
  RUN apt-get update
  RUN apt-get install -y equivs

rpmbuild:
  FROM almalinux:8
  RUN dnf install -y rpmdevtools

RPM:
  COMMAND
  ARG package
  FROM +rpmbuild
  COPY $package /tmp/$package
  WORKDIR /tmp/$package
  RUN rpmbuild -ba ${package}.spec --define "_topdir /tmp/$package/rpm" --define "_sourcedir /tmp/$package"
  SAVE ARTIFACT /tmp/$package/rpm/RPMS/noarch/${package}*.rpm AS LOCAL output/

DEB:
  COMMAND
  ARG package
  FROM +equivs
  COPY $package /tmp/$package
  WORKDIR /tmp/$package
  RUN equivs-build ${package}.control
  SAVE ARTIFACT ${package}_*.deb AS LOCAL output/

ros-dev-tools-rpm:
  DO +RPM --package=ros-dev-tools

ros-dev-tools-deb:
  DO +DEB --package=ros-dev-tools

ros-build-essential-deb:
  DO +DEB --package=ros-build-essential

ros-build-essential-rpm:
  DO +RPM --package=ros-build-essential
