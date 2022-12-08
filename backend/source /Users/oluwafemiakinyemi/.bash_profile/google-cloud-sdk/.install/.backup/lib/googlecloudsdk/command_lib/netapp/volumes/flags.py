# -*- coding: utf-8 -*- #
# Copyright 2022 Google LLC. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Flags and helpers for the Cloud NetApp Files Volumes commands."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.api_lib.netapp import netapp_client
from googlecloudsdk.calliope import arg_parsers
from googlecloudsdk.command_lib.netapp import flags
from googlecloudsdk.command_lib.netapp import util as netapp_util
from googlecloudsdk.command_lib.util.apis import arg_utils
from googlecloudsdk.command_lib.util.args import labels_util
from googlecloudsdk.command_lib.util.concepts import concept_parsers


## Helper functions to add args / flags for Volumes gcloud commands ##


def AddVolumeAssociatedStoragePoolArg(parser, required=True):
  concept_parsers.ConceptParser.ForResource(
      '--storage-pool',
      flags.GetStoragePoolResourceSpec(),
      'The Storage Pool to associate with Volume.',
      required=required,
      flag_name_overrides={'location': ''}).AddToParser(parser)


def AddVolumeNetworkArg(parser, required=True):
  """Adds a --network arg to the given parser.

  Args:
    parser: argparse parser.
    required: bool whether arg is required or not
  """

  network_arg_spec = {
      'name': str,
      'reserved-ip-range': str,
  }

  network_help = """\
        Network configuration for a Cloud NetApp Files Volume. Specifying
        `reserved-ip-range` is optional.
        *name*::: The name of the Google Compute Engine
        [VPC network](/compute/docs/networks-and-firewalls#networks) to which
        the instance is connected.
        *reserved-ip-range*::: The `reserved-ip-range` can have
        an allocated IP address range
        (https://cloud.google.com/compute/docs/ip-addresses/reserve-static-internal-ip-address). When the name of an
        allocated IP address range is specified, it must be one of the ranges
        associated with the private service access connection. The range you specify can't
        overlap with either existing subnets or assigned IP address ranges for
        other Cloud NetApp Files Volumes in the selected VPC network.
  """

  parser.add_argument(
      '--network',
      type=arg_parsers.ArgDict(spec=network_arg_spec, required_keys=['name']),
      required=required,
      help=network_help)


def GetVolumeProtocolsArgMapper(messages):
  """Returns the Choice Enum mapper for Protocols.

  Args:
    messages: The messages module.

  Returns:
    the choice arg Enum mapper
  """
  protocols_arg_mapper = (
      arg_utils.ChoiceEnumMapper(
          '--protocols',
          messages.Volume.ProtocolsValueListEntryValuesEnum,
          help_str="""The File share protocol types for the Cloud NetApp Files Volume.""",
          custom_mappings={
              'NFSV3': ('nfsv3', """File System Protocol NFSv3."""),
              'NFSV4': ('nfsv4', """File System Protocol NFSv3."""),
              'SMB': ('smb', """File System Protocol SMB."""),
          },
          default='PROTOCOL_UNSPECIFIED'))
  return protocols_arg_mapper


def AddVolumeProtocolsArg(parser, required=True):
  """Adds the Protocols arg to the arg parser."""
  parser.add_argument(
      '--protocols',
      type=arg_parsers.ArgList(min_length=1, element_type=str),
      required=required,
      help="""Type of File System protocols for the Cloud NetApp Files Volume\
           .""")


def AddVolumeShareNameArg(parser, required=True):
  """Adds the Share name arg to the arg parser."""
  parser.add_argument(
      '--share-name',
      type=str,
      required=required,
      help="""Share name of the Mount path clients will use.""")


def AddVolumeExportPolicyArg(parser):
  """Adds the Export Policy (--export-policy) arg to the given parser.

  Args:
    parser: argparse parser.
  """
  export_policy_arg_spec = {
      'allowed-clients':
          str,
      'has-root-access':
          str,
      'access-type':
          str,
      'kerberos-5-read-only':
          arg_parsers.ArgBoolean(
              truthy_strings=netapp_util.truthy,
              falsey_strings=netapp_util.falsey
          ),
      'kerberos-5-read-write':
          arg_parsers.ArgBoolean(
              truthy_strings=netapp_util.truthy,
              falsey_strings=netapp_util.falsey
          ),
      'kerberos-5i-read-only':
          arg_parsers.ArgBoolean(
              truthy_strings=netapp_util.truthy,
              falsey_strings=netapp_util.falsey
          ),
      'kerberos-5i-read-write':
          arg_parsers.ArgBoolean(
              truthy_strings=netapp_util.truthy,
              falsey_strings=netapp_util.falsey
          ),
      'kerberos-5p-read-write':
          arg_parsers.ArgBoolean(
              truthy_strings=netapp_util.truthy,
              falsey_strings=netapp_util.falsey
          ),
      'kerberos-5p-read-only':
          arg_parsers.ArgBoolean(
              truthy_strings=netapp_util.truthy,
              falsey_strings=netapp_util.falsey
          ),
      'nfsv3':
          arg_parsers.ArgBoolean(
              truthy_strings=netapp_util.truthy,
              falsey_strings=netapp_util.falsey),
      'nfsv4':
          arg_parsers.ArgBoolean(
              truthy_strings=netapp_util.truthy,
              falsey_strings=netapp_util.falsey),
  }
  export_policy_help = """\
        Export Policy of a Cloud NetApp Files Volume.
        This will be a field similar to network
        in which export policy fields can be specified as such:
        --export-policy=allowed-clients=ALLOWED_CLIENTS_IP_ADDRESSES,
        has-root-access=HAS_ROOT_ACCESS_BOOL,access=ACCESS_TYPE,nfsv3=NFSV3,
        nfsv4=NFSV4,kerberos-5-read-only=KERBEROS_5_READ_ONLY,
        kerberos-5-read-write=KERBEROS_5_READ_WRITE,
        kerberos-5i-read-only=KERBEROS_5I_READ_ONLY,
        kerberos-5i-read-write=KERBEROS_5I_READ_WRITE,
        kerberos-5p-read-only=KERBEROS_5P_READ_ONLY,
        kerberos-5p-read-write=KERBEROS_5P_READ_WRITE
  """
  parser.add_argument(
      '--export-policy',
      type=arg_parsers.ArgDict(spec=export_policy_arg_spec),
      help=export_policy_help)


def AddVolumeUnixPermissionsArg(parser):
  """Adds the Unix Permissions arg to the arg parser."""
  parser.add_argument(
      '--unix-permissions',
      type=str,
      help="""Unix permissions the mount point will be created with.
      Unix permissions are only applicable with NFS protocol only""")


def GetVolumeSmbSettingsArg(messages):
  """Returns a --smb-settings choice enum mapper arg.

  Args:
    messages: The messages module.

  Returns:
    The choice arg.
  """
  smb_settings_arg = (
      arg_utils.ChoiceEnumMapper(
          '--smb-settings',
          messages.Volume.SmbSettingsValueListEntryValuesEnum,
          ## TODO(b/239958861) Review, and add detailed smb settings help text
          help_str="""The SMB Settings of the Volume.""",
          custom_mappings={
              'ENCRYPT_DATA': 'encrypt-data',
              'BROWSABLE': 'browsable',
              'CHANGE_NOTIFY': 'change-notify',
              'NON_BROWSABLE': 'non-browsable',
              'OPLOCKS': 'oplocks',
              'SHOW_SNAPSHOT': 'show-snapshot',
              'SHOW_PREVIOUS_VERSIONS': 'show-previous-versions',
              'ACCESS_BASED_ENUMERATION': 'access-based-enumeration',
              'CONTINUOUSLY_AVAILABLE': 'continuously-available'
          },
          default='SMB_SETTINGS_UNSPECIFIED'))
  return smb_settings_arg


def AddVolumeSmbSettingsArg(parser):
  """Adds the --smb-settings arg to the arg parser."""
  parser.add_argument(
      '--smb-settings',
      type=arg_parsers.ArgList(min_length=1, element_type=str),
      help="""The SMB Settings of the Volume.The SMB Settings of the Volume.""")


def AddVolumeHourlySnapshotArg(parser):
  """Adds the --hourly-snapshot arg to the arg parser."""
  hourly_snapshot_arg_spec = {
      'snapshots-to-keep': float,
      'minute': float,
  }
  hourly_snapshot_help = """
  Make a snapshot every hour e.g. at 04:00, 05:20, 06:00
  """
  parser.add_argument(
      '--hourly-snapshot',
      type=arg_parsers.ArgDict(spec=hourly_snapshot_arg_spec),
      help=hourly_snapshot_help)


def AddVolumeDailySnapshotArg(parser):
  """Adds the --daily-snapshot arg to the arg parser."""
  daily_snapshot_arg_spec = {
      'snapshots-to-keep': float,
      'minute': float,
      'hour': float,
  }
  daily_snapshot_help = """
  Make a snapshot every day e.g. at 06:00, 05:20, 23:50
  """
  parser.add_argument(
      '--daily-snapshot',
      type=arg_parsers.ArgDict(spec=daily_snapshot_arg_spec),
      help=daily_snapshot_help)


def AddVolumeWeeklySnapshotArg(parser):
  """Adds the --weekly-snapshot arg to the arg parser."""
  weekly_snapshot_arg_spec = {
      'snapshots-to-keep': float,
      'minute': float,
      'hour': float,
      'day': str
  }
  weekly_snapshot_help = """
  Make a snapshot every week e.g. at Monday 04:00, Wednesday 05:20,
  Sunday 23:50
  """
  parser.add_argument(
      '--weekly-snapshot',
      type=arg_parsers.ArgDict(spec=weekly_snapshot_arg_spec),
      help=weekly_snapshot_help)


def AddVolumeMonthlySnapshotArg(parser):
  """Addss the --monthly-snapshot arg to the arg parser."""
  monthly_snapshot_arg_spec = {
      'snapshots-to-keep': float,
      'minute': float,
      'hour': float,
      'day': str
  }
  monthly_snapshot_help = """
  Make a snapshot once a month e.g. at 2nd 04:00, 7th 05:20, 24th 23:50
  """
  parser.add_argument(
      '--monthly-snapshot',
      type=arg_parsers.ArgDict(spec=monthly_snapshot_arg_spec),
      help=monthly_snapshot_help)


def AddVolumeSnapReserveArg(parser):
  """Adds the --snap-reserve arg to the arg parser."""
  parser.add_argument(
      '--snap-reserve',
      type=float,
      help="""The percentage of volume storage reserved for snapshot storage.
      The default value for this is 0 percent""")


def AddVolumeSnapshotDirectoryArg(parser):
  """Adds the --snapshot-directory arg to the arg parser."""
  parser.add_argument(
      '--snapshot-directory',
      type=arg_parsers.ArgBoolean(
          truthy_strings=netapp_util.truthy, falsey_strings=netapp_util.falsey),
      default='true',
      help="""Snapshot Directory if enabled (true) makes the Volume
            contain a read-only .snapshot directory which provides access
            to each of the volume's snapshots
          """)


def GetVolumeSecurityStyleArg(messages):
  """Returns a --security-style choice enum mapper arg.

  Args:
    messages: The messages module.

  Returns:
    The choice arg.
  """
  security_style_arg = (
      arg_utils.ChoiceEnumMapper(
          '--security-style',
          messages.Volume.SecurityStyleValueValuesEnum,
          help_str="""The security style of the Volume. This can either be
          UNIX or NTFS.
        """,
          custom_mappings={
              'UNIX': ('unix', """UNIX security style for Volume"""),
              'NTFS': ('ntfs', """NTFS security style for Volume."""),
          },
          default='SECURITY_STYLE_UNSPECIFIED'))
  return security_style_arg


def AddVolumeSecurityStyleArg(parser, messages):
  """Adds the --security-style arg to the arg parser."""
  GetVolumeSecurityStyleArg(messages).choice_arg.AddToParser(parser)


def AddVolumeEnableKerberosArg(parser):
  """Adds the --enable-kerberos arg to the arg parser."""
  parser.add_argument(
      '--enable-kerberos',
      type=arg_parsers.ArgBoolean(
          truthy_strings=netapp_util.truthy, falsey_strings=netapp_util.falsey),
      help="""Boolean flag indicating whether Volume is a kerberos Volume or not"""
  )


def AddVolumeEnableLdapArg(parser):
  """Adds the --enable-ladp arg to the arg parser."""
  parser.add_argument(
      '--enable-ldap',
      type=arg_parsers.ArgBoolean(
          truthy_strings=netapp_util.truthy, falsey_strings=netapp_util.falsey),
      help="""Boolean flag indicating whether Volume is a NFS LDAP Volume or not"""
  )


def AddVolumeForceArg(parser):
  """Adds the --force arg to the arg parser."""
  parser.add_argument(
      '--force',
      action='store_true',
      help="""Forces the deletion of a volume and its child resources, such as snapshots."""
  )


def AddVolumeActiveDirectoryArg(parser):
  """Adds the --active-directory resource arg to the arg parser."""
  concept_parsers.ConceptParser.ForResource(
      '--active-directory',
      flags.GetActiveDirectoryResourceSpec(),
      group_help='The Active Directory associated with Volume.',
      flag_name_overrides={'location': ''}).AddToParser(
          parser)


def AddVolumeRevertSnapshotArg(parser, required=True):
  """Adds the --snapshot arg to the arg parser."""
  concept_parsers.ConceptParser.ForResource(
      '--snapshot',
      flags.GetSnapshotResourceSpec(revert_op=True, positional=False),
      required=required,
      flag_name_overrides={'location': '',
                           'volume': ''},
      group_help='The Snapshot to revert the Volume back to.').AddToParser(
          parser)


def AddVolumeFromSnapshotArg(parser):
  """Adds the --from-snapshot arg to the arg parser."""
  concept_parsers.ConceptParser.ForResource(
      '--from-snapshot',
      flags.GetSnapshotResourceSpec(revert_op=True, positional=False),
      flag_name_overrides={'location': '',
                           'volume': ''},
      group_help='The Snapshot to create the Volume from.').AddToParser(
          parser)

## Helper functions to combine Volumes args / flags for gcloud commands #


def AddVolumeCreateArgs(parser, release_track):
  """Add args for creating a Volume."""
  concept_parsers.ConceptParser([
      flags.GetVolumePresentationSpec('The Volume to create.')
  ]).AddToParser(parser)
  messages = netapp_client.GetMessagesModule(release_track=release_track)
  flags.AddResourceDescriptionArg(parser, 'Volume')
  flags.AddResourceCapacityArg(parser, 'Volume')
  AddVolumeAssociatedStoragePoolArg(parser)
  AddVolumeNetworkArg(parser)
  flags.AddResourceAsyncFlag(parser)
  AddVolumeProtocolsArg(parser)
  AddVolumeShareNameArg(parser)
  AddVolumeExportPolicyArg(parser)
  AddVolumeUnixPermissionsArg(parser)
  AddVolumeSmbSettingsArg(parser)
  AddVolumeFromSnapshotArg(parser)
  AddVolumeHourlySnapshotArg(parser)
  AddVolumeDailySnapshotArg(parser)
  AddVolumeWeeklySnapshotArg(parser)
  AddVolumeMonthlySnapshotArg(parser)
  AddVolumeSnapReserveArg(parser)
  AddVolumeSnapshotDirectoryArg(parser)
  AddVolumeSecurityStyleArg(parser, messages)
  AddVolumeEnableKerberosArg(parser)
  AddVolumeEnableLdapArg(parser)
  AddVolumeActiveDirectoryArg(parser)
  labels_util.AddCreateLabelsFlags(parser)


def AddVolumeDeleteArgs(parser):
  """Add args for deleting a Volume."""
  concept_parsers.ConceptParser([
      flags.GetVolumePresentationSpec('The Volume to delete.')
  ]).AddToParser(parser)
  flags.AddResourceAsyncFlag(parser)
  AddVolumeForceArg(parser)


def AddVolumeUpdateArgs(parser, release_track):
  """Add args for updating a Volume."""
  concept_parsers.ConceptParser([
      flags.GetVolumePresentationSpec('The Volume to update.')
  ]).AddToParser(parser)
  messages = netapp_client.GetMessagesModule(release_track=release_track)
  flags.AddResourceDescriptionArg(parser, 'Volume')
  flags.AddResourceCapacityArg(parser, 'Volume', required=False)
  AddVolumeAssociatedStoragePoolArg(parser, required=False)
  AddVolumeNetworkArg(parser, required=False)
  flags.AddResourceAsyncFlag(parser)
  AddVolumeProtocolsArg(parser, required=False)
  AddVolumeShareNameArg(parser, required=False)
  AddVolumeExportPolicyArg(parser)
  AddVolumeUnixPermissionsArg(parser)
  AddVolumeSmbSettingsArg(parser)
  AddVolumeHourlySnapshotArg(parser)
  AddVolumeDailySnapshotArg(parser)
  AddVolumeWeeklySnapshotArg(parser)
  AddVolumeMonthlySnapshotArg(parser)
  AddVolumeSnapReserveArg(parser)
  AddVolumeSnapshotDirectoryArg(parser)
  AddVolumeSecurityStyleArg(parser, messages)
  AddVolumeEnableKerberosArg(parser)
  AddVolumeEnableLdapArg(parser)
  AddVolumeActiveDirectoryArg(parser)
  labels_util.AddUpdateLabelsFlags(parser)
