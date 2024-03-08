Minimal-ActivityPub
===================

|Repo| |CI| |Downloads|

|Safety| |pip-audit| |CodeLimit|

|Codestyle| |Version| |Wheel|

|AGPL|

!!! This is an early alpha release of a new version using `httpx AsyncClient`_. Expect errors to be present in this version !!!

.. _httpx AsyncClient: https://www.python-httpx.org/async/


Minimal-ActivityPub is a minimal Python implementation of the ActivityPub rest API used by `Mastodon`_, `Pleroma`_,
and `Takahe`_. This implementation makes use of asyncio where appropriate. It is intended to be used as a library by
other applications. No standalone functionality is provided.

Minimal refers to the fact that only API calls I need for my other projects `Fedinesia`_ and `Tootbot`_ are implemented.

**DO NOT** expect a full or complete implementation of all `ActivityPub API <https://activitypub.rocks/>`_ functionality.

For more details have a look at the `Documentation`_

Contributing
==================================
Issues and pull requests are welcome.

Minimal-ActivityPub is using `pre-commit`_  and `pdm`_. Please install and use both pre-commit and pdm if you'd
like to contribute.

Licensing
==================================
Minimal-ActivityPub is licences under licensed under the `GNU Affero General Public License v3.0 <http://www.gnu.org/licenses/agpl-3.0.html>`_

Supporting Minimal-ActivityPub
==================================

There are a number of ways you can support Minimal-ActivityPub:

- Create an issue with problems or ideas you have with/for Minimal-ActivityPub
- You can `buy me a coffee <https://www.buymeacoffee.com/marvin8>`_.
- You can send me small change in Monero to the address below:

Monero donation address:
----------------------------------
`8ADQkCya3orL178dADn4bnKuF1JuVGEG97HPRgmXgmZ2cZFSkWU9M2v7BssEGeTRNN2V5p6bSyHa83nrdu1XffDX3cnjKVu`


.. |AGPL| image:: https://www.gnu.org/graphics/agplv3-with-text-162x68.png
    :alt: AGLP 3 or later
    :target:  https://codeberg.org/MarvinsMastodonTools/minimal-activitypub/src/branch/main/LICENSE.md

.. |Repo| image:: https://img.shields.io/badge/repo-Codeberg.org-blue
    :alt: Repo at Codeberg.org
    :target: https://codeberg.org/MarvinsMastodonTools/minimal-activitypub

.. |Downloads| image:: https://pepy.tech/badge/minimal-activitypub
    :alt: Download count
    :target: https://pepy.tech/project/minimal-activitypub

.. |Codestyle| image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :alt: Code style: black
    :target: https://github.com/psf/black

.. |Safety| image:: https://img.shields.io/badge/Safety--DB-checked-green
    :alt: Checked against PyUp Safety DB
    :target: https://pyup.io/safety/

.. |pip-audit| image:: https://img.shields.io/badge/pip--audit-checked-green
    :alt: Checked with pip-audit
    :target: https://pypi.org/project/pip-audit/

.. |Version| image:: https://img.shields.io/pypi/pyversions/minimal-activitypub
    :alt: PyPI - Python Version

.. |Wheel| image:: https://img.shields.io/pypi/wheel/minimal-activitypub
    :alt: PyPI - Wheel

.. |CI| image:: https://ci.codeberg.org/api/badges/MarvinsMastodonTools/minimal-activitypub/status.svg
    :alt: CI / Woodpecker
    :target: https://ci.codeberg.org/MarvinsMastodonTools/minimal-activitypub

.. |CodeLimit| image:: https://img.shields.io/badge/CodeLimit-checked-green.svg
    :target: https://github.com/getcodelimit/codelimit

.. _Documentation: https://marvinsmastodontools.codeberg.page/minimal-activitypub/
.. _pre-commit: https://pre-commit.com/
.. _pdm: https://pdm.fming.dev/latest/
.. _Mastodon: https://joinmastodon.org/
.. _Pleroma: https://pleroma.social/
.. _Takahe: https://jointakahe.org/
.. _Fedinesia: https://codeberg.org/MarvinsMastodonTools/fedinesia
.. _Tootbot: https://codeberg.org/MarvinsMastodonTools/tootbot
