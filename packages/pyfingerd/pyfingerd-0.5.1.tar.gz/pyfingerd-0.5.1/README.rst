finger (RFC 1288) server-side daemon
====================================

finger is both a protocol and a utility to get the information and status
from a user on a distant machine. It was standardized in `RFC 742`_
in 1977, then in `RFC 1288`_ in 1991, and has been abandoned since.

While describing the protocol in `a blog post of mine`_, I wanted
to implement this protocol for fun, but didn't want to present the
real information about the users on my server, so I made this to present
some fictional information in order to be able to tell a story through
finger.

For more information, consult the following links:

* `pyfingerd documentation`_;
* `PyPI package detail`_;
* `Issue tracker`_;
* `Pending contributions`_.

.. _RFC 742: https://tools.ietf.org/html/rfc742
.. _RFC 1288: https://tools.ietf.org/html/rfc1288
.. _a blog post of mine: https://thomas.touhey.fr/2018/09/12/finger.en.html
.. _pyfingerd documentation: https://pyfingerd.org/
.. _PyPI package detail: https://pypi.org/project/pyfingerd/
.. _Issue tracker: https://gitlab.com/pyfingerd/pyfingerd/-/issues
.. _Pending contributions:
    https://gitlab.com/pyfingerd/pyfingerd/-/merge_requests
