Processing of Forbild phantom files for RTK
===========================================

The [Forbild phantom](http://www.imp.uni-erlangen.de/forbild/deutsch/results/)
is a standard in computed tomography (CT). This repository tracks how the
original files, which are available from the [Forbild
 website](http://www.imp.uni-erlangen.de/forbild/deutsch/results/) (currently
 down but still available on the [Web
 archive](https://web.archive.org/web/20070611224909/http://www.imp.uni-erlangen.de/forbild/deutsch/results/)),
 can be pre-pocessed to be used in the [reconstruction toolkit
 (RTK)](http://www.openrtk.org).

 Each phantom file is manually edited to correct for typos (e.g. missing translation from German or spaces between the `-` sign and the number) and indicate union of shapes. The file is then processed with `ProcessForbildPhantomFile.py` which combines `gcc` pre-processing (for `#include` and `#define` syntaxes) and regular expressions (for arithmetic) to produce a single phantom file usable by [RTK](http://www.openrtk.org).
