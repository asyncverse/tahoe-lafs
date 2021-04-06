"""
Track the port to Python 3.

The two easiest ways to run the part of the test suite which is expected to
pass on Python 3 are::

    $ tox -e py36

and::

    $ trial allmydata.test.python3_tests

This module has been ported to Python 3.
"""

from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from future.utils import PY2
if PY2:
    from future.builtins import filter, map, zip, ascii, chr, hex, input, next, oct, open, pow, round, super, bytes, dict, list, object, range, str, max, min  # noqa: F401

# Keep these sorted alphabetically, to reduce merge conflicts:
PORTED_MODULES = [
    "allmydata",
    "allmydata.__main__",
    "allmydata._auto_deps",
    "allmydata._monkeypatch",
    "allmydata.blacklist",
    "allmydata.check_results",
    "allmydata.client",
    "allmydata.codec",
    "allmydata.control",
    "allmydata.crypto",
    "allmydata.crypto.aes",
    "allmydata.crypto.ed25519",
    "allmydata.crypto.error",
    "allmydata.crypto.rsa",
    "allmydata.crypto.util",
    "allmydata.deep_stats",
    "allmydata.dirnode",
    "allmydata.frontends",
    "allmydata.frontends.sftpd",
    "allmydata.hashtree",
    "allmydata.history",
    "allmydata.immutable",
    "allmydata.immutable.checker",
    "allmydata.immutable.downloader",
    "allmydata.immutable.downloader.common",
    "allmydata.immutable.downloader.fetcher",
    "allmydata.immutable.downloader.finder",
    "allmydata.immutable.downloader.node",
    "allmydata.immutable.downloader.segmentation",
    "allmydata.immutable.downloader.share",
    "allmydata.immutable.downloader.status",
    "allmydata.immutable.encode",
    "allmydata.immutable.filenode",
    "allmydata.immutable.happiness_upload",
    "allmydata.immutable.layout",
    "allmydata.immutable.literal",
    "allmydata.immutable.offloaded",
    "allmydata.immutable.repairer",
    "allmydata.immutable.upload",
    "allmydata.interfaces",
    "allmydata.introducer",
    "allmydata.introducer.client",
    "allmydata.introducer.common",
    "allmydata.introducer.interfaces",
    "allmydata.introducer.server",
    "allmydata.monitor",
    "allmydata.mutable",
    "allmydata.mutable.checker",
    "allmydata.mutable.common",
    "allmydata.mutable.filenode",
    "allmydata.mutable.layout",
    "allmydata.mutable.publish",
    "allmydata.mutable.repairer",
    "allmydata.mutable.retrieve",
    "allmydata.mutable.servermap",
    "allmydata.node",
    "allmydata.nodemaker",
    "allmydata.scripts",
    "allmydata.scripts.create_node",
    "allmydata.scripts.runner",
    "allmydata.scripts.types_",
    "allmydata.stats",
    "allmydata.storage_client",
    "allmydata.storage",
    "allmydata.storage.common",
    "allmydata.storage.crawler",
    "allmydata.storage.expirer",
    "allmydata.storage.immutable",
    "allmydata.storage.lease",
    "allmydata.storage.mutable",
    "allmydata.storage.server",
    "allmydata.storage.shares",
    "allmydata.test",
    "allmydata.test.cli",
    "allmydata.test.cli_node_api",
    "allmydata.test.common",
    "allmydata.test.common_util",
    "allmydata.test.common_web",
    "allmydata.test.eliotutil",
    "allmydata.test.no_network",
    "allmydata.test.matchers",
    "allmydata.test.mutable",
    "allmydata.test.mutable.util",
    "allmydata.test.python3_tests",
    "allmydata.test.storage_plugin",
    "allmydata.test.strategies",
    "allmydata.test.web",
    "allmydata.test.web.common",
    "allmydata.test.web.matchers",
    "allmydata.testing",
    "allmydata.testing.web",
    "allmydata.unknown",
    "allmydata.uri",
    "allmydata.util",
    "allmydata.util._python3",
    "allmydata.util.abbreviate",
    "allmydata.util.assertutil",
    "allmydata.util.base32",
    "allmydata.util.base62",
    "allmydata.util.configutil",
    "allmydata.util.connection_status",
    "allmydata.util.deferredutil",
    "allmydata.util.dictutil",
    "allmydata.util.eliotutil",
    "allmydata.util.encodingutil",
    "allmydata.util.fileutil",
    "allmydata.util.gcutil",
    "allmydata.util.happinessutil",
    "allmydata.util.hashutil",
    "allmydata.util.humanreadable",
    "allmydata.util.i2p_provider",
    "allmydata.util.idlib",
    "allmydata.util.iputil",
    "allmydata.util.jsonbytes",
    "allmydata.util.log",
    "allmydata.util.mathutil",
    "allmydata.util.namespace",
    "allmydata.util.netstring",
    "allmydata.util.observer",
    "allmydata.util.pipeline",
    "allmydata.util.pollmixin",
    "allmydata.util.spans",
    "allmydata.util.statistics",
    "allmydata.util.time_format",
    "allmydata.util.tor_provider",
    "allmydata.web",
    "allmydata.web.check_results",
    "allmydata.web.common",
    "allmydata.web.directory",
    "allmydata.web.filenode",
    "allmydata.web.info",
    "allmydata.web.introweb",
    "allmydata.web.logs",
    "allmydata.web.operations",
    "allmydata.web.private",
    "allmydata.web.root",
    "allmydata.web.status",
    "allmydata.web.storage",
    "allmydata.web.storage_plugins",
    "allmydata.web.unlinked",
    "allmydata.webish",
    "allmydata.windows",
]

PORTED_TEST_MODULES = [
    "allmydata.test.cli.test_alias",
    "allmydata.test.cli.test_backupdb",
    "allmydata.test.cli.test_create",
    "allmydata.test.cli.test_invite",
    "allmydata.test.cli.test_status",

    "allmydata.test.mutable.test_checker",
    "allmydata.test.mutable.test_datahandle",
    "allmydata.test.mutable.test_different_encoding",
    "allmydata.test.mutable.test_exceptions",
    "allmydata.test.mutable.test_filehandle",
    "allmydata.test.mutable.test_filenode",
    "allmydata.test.mutable.test_interoperability",
    "allmydata.test.mutable.test_multiple_encodings",
    "allmydata.test.mutable.test_multiple_versions",
    "allmydata.test.mutable.test_problems",
    "allmydata.test.mutable.test_repair",
    "allmydata.test.mutable.test_roundtrip",
    "allmydata.test.mutable.test_servermap",
    "allmydata.test.mutable.test_update",
    "allmydata.test.mutable.test_version",
    "allmydata.test.test_abbreviate",
    "allmydata.test.test_auth",
    "allmydata.test.test_base32",
    "allmydata.test.test_base62",
    "allmydata.test.test_checker",
    "allmydata.test.test_client",
    "allmydata.test.test_codec",
    "allmydata.test.test_common_util",
    "allmydata.test.test_configutil",
    "allmydata.test.test_connections",
    "allmydata.test.test_connection_status",
    "allmydata.test.test_crawler",
    "allmydata.test.test_crypto",

    # Only partially ported, CLI-using test code is disabled for now until CLI
    # is ported.
    "allmydata.test.test_deepcheck",

    "allmydata.test.test_deferredutil",
    "allmydata.test.test_dictutil",
    "allmydata.test.test_dirnode",
    "allmydata.test.test_download",
    "allmydata.test.test_eliotutil",
    "allmydata.test.test_encode",
    "allmydata.test.test_encodingutil",
    "allmydata.test.test_filenode",
    "allmydata.test.test_happiness",
    "allmydata.test.test_hashtree",
    "allmydata.test.test_hashutil",
    "allmydata.test.test_helper",
    "allmydata.test.test_humanreadable",
    "allmydata.test.test_hung_server",
    "allmydata.test.test_i2p_provider",
    "allmydata.test.test_immutable",
    "allmydata.test.test_introducer",
    "allmydata.test.test_iputil",
    "allmydata.test.test_json_metadata",
    "allmydata.test.test_log",
    "allmydata.test.test_monitor",
    "allmydata.test.test_netstring",
    "allmydata.test.test_no_network",
    "allmydata.test.test_node",
    "allmydata.test.test_observer",
    "allmydata.test.test_pipeline",
    "allmydata.test.test_python3",
    "allmydata.test.test_repairer",
    "allmydata.test.test_runner",
    "allmydata.test.test_sftp",
    "allmydata.test.test_spans",
    "allmydata.test.test_statistics",
    "allmydata.test.test_stats",
    "allmydata.test.test_storage",
    "allmydata.test.test_storage_client",
    "allmydata.test.test_storage_web",

    # Only partially ported, test_filesystem_with_cli_in_subprocess isn't
    # ported yet, nor is part of test_filesystem (the call to _test_cli). This
    # should be done once CLI is ported.
    "allmydata.test.test_system",

    "allmydata.test.test_testing",
    "allmydata.test.test_time_format",
    "allmydata.test.test_tor_provider",
    "allmydata.test.test_upload",
    "allmydata.test.test_uri",
    "allmydata.test.test_util",
    "allmydata.test.web.test_common",
    "allmydata.test.web.test_grid",
    "allmydata.test.web.test_introducer",
    "allmydata.test.web.test_logs",
    "allmydata.test.web.test_private",
    "allmydata.test.web.test_root",
    "allmydata.test.web.test_status",
    "allmydata.test.web.test_util",
    "allmydata.test.web.test_web",
    "allmydata.test.web.test_webish",
    "allmydata.test.test_windows",
]
