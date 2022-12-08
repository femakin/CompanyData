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
"""Commands for interacting with the Cloud NetApp Files Volume API resource."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from apitools.base.py import list_pager
from googlecloudsdk.api_lib.netapp.constants import OPERATIONS_COLLECTION
from googlecloudsdk.api_lib.netapp.constants import VOLUME_RESOURCE
from googlecloudsdk.api_lib.netapp.util import GetClientInstance
from googlecloudsdk.api_lib.netapp.util import GetMessagesModule
from googlecloudsdk.api_lib.netapp.util import VERSION_MAP
from googlecloudsdk.api_lib.util import waiter
from googlecloudsdk.calliope import base
from googlecloudsdk.core import log
from googlecloudsdk.core import resources


class VolumesClient(object):
  """Wrapper for working with Storage Pool in the Cloud NetApp Files API Client."""

  def __init__(self, release_track=base.ReleaseTrack.ALPHA):
    if release_track == base.ReleaseTrack.ALPHA:
      self._adapter = AlphaVolumesAdapter()
    else:
      raise ValueError('[{}] is not a valid API version.'.format(
          VERSION_MAP[release_track]))

  @property
  def client(self):
    return self._adapter.client

  @property
  def messages(self):
    return self._adapter.messages

  def WaitForOperation(self, operation_ref):
    """Waits on the long-running operation until the done field is True.

    Args:
      operation_ref: the operation reference.

    Raises:
      waiter.OperationError: if the operation contains an error.

    Returns:
      the 'response' field of the Operation.
    """
    return waiter.WaitFor(
        waiter.CloudOperationPollerNoResources(
            self.client.projects_locations_operations), operation_ref,
        'Waiting for [{0}] to finish'.format(operation_ref.Name()))

  def ListVolumes(self, location_ref, limit=None):
    """Make API calls to List active Cloud NetApp Volumes.

    Args:
      location_ref: The parsed location of the listed NetApp Volumes.
      limit: The number of Cloud NetApp Volumes to limit the results to. This
        limit is passed to the server and the server does the limiting.

    Returns:
      Generator that yields the Cloud NetApp Volumes.
    """
    request = self.messages.NetappProjectsLocationsVolumesListRequest(
        parent=location_ref)
    # Check for unreachable locations.
    response = self.client.projects_locations_volumes.List(request)
    for location in response.unreachable:
      log.warning('Location {} may be unreachable.'.format(location))
    return list_pager.YieldFromList(
        self.client.projects_locations_volumes,
        request,
        field=VOLUME_RESOURCE,
        limit=limit,
        batch_size_attribute='pageSize')

  def CreateVolume(self, volume_ref, async_, config):
    """Create a Cloud NetApp Volume."""
    request = self.messages.NetappProjectsLocationsVolumesCreateRequest(
        parent=volume_ref.Parent().RelativeName(),
        volumeId=volume_ref.Name(),
        volume=config)
    create_op = self.client.projects_locations_volumes.Create(request)
    if async_:
      return create_op
    operation_ref = resources.REGISTRY.ParseRelativeName(
        create_op.name, collection=OPERATIONS_COLLECTION)
    return self.WaitForOperation(operation_ref)

  def ParseVolumeConfig(self,
                        name=None,
                        capacity=None,
                        description=None,
                        storage_pool=None,
                        network=None,
                        protocols=None,
                        share_name=None,
                        export_policy=None,
                        unix_permissions=None,
                        smb_settings=None,
                        snapshot_policy=None,
                        snap_reserve=None,
                        snapshot_directory=None,
                        security_style=None,
                        enable_kerberos=None,
                        enable_ldap=None,
                        active_directory=None,
                        snapshot=None,
                        labels=None):
    """Parses the command line arguments for Create Volume into a config.

    Args:
      name: the name of the Volume
      capacity: the storage capacity of the Volume.
      description: the description of the Volume.
      storage_pool: the Storage Pool the Volume is attached to.
      network: the VPC network for the Volume.
      protocols: the type of fileshare protocol of the Volume.
      share_name: the share name or mount point of the Volume.
      export_policy: the export policy of the Volume if NFS.
      unix_permissions: the Unix permissions for the Volume.
      smb_settings: the SMB settings for the Volume.
      snapshot_policy: the Snapshot Policy for the Volume
      snap_reserve: the snap reserve (double) for the Volume
      snapshot_directory: Bool on whether to use snapshot directory for Volume
      security_style: the security style of the Volume
      enable_kerberos: Bool on whether to use kerberos for Volume
      enable_ldap: Bool on whether to use LDAP for Volume
      active_directory: the Active Directory associated with the Volume
      snapshot: the snapshot name to create Volume from
      labels: the parsed labels value.

    Returns:
      the configuration that will be used as the request body for creating a
      Cloud NetApp Files Volume.
    """
    volume = self.messages.Volume()
    volume.name = name
    volume.capacityGib = capacity
    volume.description = description
    volume.labels = labels
    volume.storagePoolName = storage_pool
    volume.shareName = share_name
    self._adapter.ParseExportPolicy(volume, export_policy)
    self._adapter.ParseProtocols(volume, protocols)
    volume.unixPermissions = unix_permissions
    volume.network = network.get('name')
    if 'reserved-ip-range' in network:
      volume.psaRange = network.get('reserved-ip-range')
    volume.smbSettings = smb_settings
    self._adapter.ParseSnapshotPolicy(volume, snapshot_policy)
    volume.snapReserve = snap_reserve
    volume.snapshotDirectory = snapshot_directory
    volume.securityStyle = security_style
    volume.kerberosEnabled = enable_kerberos
    volume.ldapEnabled = enable_ldap
    volume.activeDirectoryName = active_directory
    volume.restoreParameters = self.messages.RestoreParameters(
        sourceSnapshot=snapshot
    ) if snapshot else None
    return volume

  def GetVolume(self, volume_ref):
    """Get Cloud NetApp Volume information."""
    request = self.messages.NetappProjectsLocationsVolumesGetRequest(
        name=volume_ref.RelativeName())
    return self.client.projects_locations_volumes.Get(request)

  def DeleteVolume(self, volume_ref, async_, force):
    """Deletes an existing Cloud NetApp Volume."""
    request = self.messages.NetappProjectsLocationsVolumesDeleteRequest(
        name=volume_ref.RelativeName(), force=force)
    return self._DeleteVolume(async_, request)

  def _DeleteVolume(self, async_, request):
    delete_op = self.client.projects_locations_volumes.Delete(request)
    if async_:
      return delete_op
    operation_ref = resources.REGISTRY.ParseRelativeName(
        delete_op.name, collection=OPERATIONS_COLLECTION)
    return self.WaitForOperation(operation_ref)

  def RevertVolume(self, volume_ref, snapshot_id):
    """Reverts an existing Cloud NetApp Volume."""
    request = self.messages.NetappProjectsLocationsVolumesRevertRequest(
        name=volume_ref.RelativeName(),
        revertVolumeRequest=self.messages.RevertVolumeRequest(
            snapshotId=snapshot_id))
    return self.client.projects_locations_volumes.Revert(request)

  def ParseUpdatedVolumeConfig(self,
                               volume_config,
                               description=None,
                               labels=None,
                               storage_pool=None,
                               protocols=None,
                               share_name=None,
                               export_policy=None,
                               capacity=None,
                               network=None,
                               unix_permissions=None,
                               smb_settings=None,
                               snapshot_policy=None,
                               snap_reserve=None,
                               snapshot_directory=None,
                               security_style=None,
                               enable_kerberos=None,
                               enable_ldap=None,
                               active_directory=None):
    """Parses updates into a volume config.

    Args:
      volume_config: The volume config to update.
      description: str, a new description, if any.
      labels: LabelsValue message, the new labels value, if any.
      storage_pool: the new storage pool ID, if any.
      protocols: protocol Enum type, if any
      share_name: share name of volume, if any
      export_policy: the export policy of a volume, if any
      capacity: capacity of a volume, if any
      network: the network of a volume, if any
      unix_permissions: the UNIX style permissions of a volume, if any
      smb_settings: the SMB settings for the Volume, if any
      snapshot_policy: the Snapshot Policy for the Volume, if any
      snap_reserve: the snapshot reserved storage percentage, if any
      snapshot_directory: the snapshot directory Bool for a Volume, if any
      security_style: the Security Style for a Volume, if any
      enable_kerberos: Bool on whether Kerberos is enabled, if any
      enable_ldap: Bool on whether LDAP is enabled, if any
      active_directory: The Active Directory for the Volume, if any

    Returns:
      The volume message.
    """
    return self._adapter.ParseUpdatedVolumeConfig(
        volume_config,
        description=description,
        labels=labels,
        storage_pool=storage_pool,
        protocols=protocols,
        share_name=share_name,
        export_policy=export_policy,
        capacity=capacity,
        network=network,
        unix_permissions=unix_permissions,
        smb_settings=smb_settings,
        snapshot_policy=snapshot_policy,
        snap_reserve=snap_reserve,
        snapshot_directory=snapshot_directory,
        security_style=security_style,
        enable_kerberos=enable_kerberos,
        enable_ldap=enable_ldap,
        active_directory=active_directory)

  def UpdateVolume(self, volume_ref, volume_config, update_mask, async_):
    """Updates a Cloud NetApp Volume.

    Args:
      volume_ref: the reference to the Volume.
      volume_config: Volume config, the updated volume.
      update_mask: str, a comma-separated list of updated fields.
      async_: bool, if False, wait for the operation to complete.

    Returns:
      an Operation or Volume message.
    """
    update_op = self._adapter.UpdateVolume(volume_ref, volume_config,
                                           update_mask)
    if async_:
      return update_op
    operation_ref = resources.REGISTRY.ParseRelativeName(
        update_op.name, collection=OPERATIONS_COLLECTION)
    return self.WaitForOperation(operation_ref)


class AlphaVolumesAdapter(object):
  """Adapter for the Alpha Cloud NetApp Files API Volume resource."""

  def __init__(self):
    self.release_track = base.ReleaseTrack.ALPHA
    self.client = GetClientInstance(release_track=self.release_track)
    self.messages = GetMessagesModule(release_track=self.release_track)

  def ParseExportPolicy(self, volume, export_policy):
    """Parses Export Policy for Volume into a config.

    Args:
      volume: The Cloud NetApp Volume message object
      export_policy: the Export Policy message object.

    Returns:
      Volume message populated with Export Policy values.

    """
    if not export_policy:
      return
    export_policy_config = self.messages.ExportPolicy()
    simple_export_policy_rule = self.messages.SimpleExportPolicyRule()
    for key, val in export_policy.items():
      if key == 'allowed-clients':
        simple_export_policy_rule.allowedClients = val
      if key == 'access-type':
        simple_export_policy_rule.accessType = (
            self.messages.SimpleExportPolicyRule.AccessTypeValueValuesEnum
            .lookup_by_name(val))
      if key == 'has-root-access':
        simple_export_policy_rule.hasRootAccess = val
      if key == 'kerberos-5-read-only':
        simple_export_policy_rule.kerberos5ReadOnly = val
      if key == 'kerberos-5-read-write':
        simple_export_policy_rule.kerberos5ReadWrite = val
      if key == 'kerberos-5i-read-only':
        simple_export_policy_rule.kerberos5iReadOnly = val
      if key == 'kerberos-5i-read-write':
        simple_export_policy_rule.kerberos5iReadWrite = val
      if key == 'kerberos-5p-read-only':
        simple_export_policy_rule.kerberos5pReadOnly = val
      if key == 'kerberos-5p-read-write':
        simple_export_policy_rule.kerberos5pReadWrite = val
      if key == 'nfsv3':
        simple_export_policy_rule.nfsv3 = val
      if key == 'nfsv4':
        simple_export_policy_rule.nfsv4 = val
    export_policy_config.rules.append(simple_export_policy_rule)
    volume.exportPolicy = export_policy_config

  def ParseProtocols(self, volume, protocols):
    """Parses Protocols from a list of Protocol Enums into the given volume.

    Args:
      volume: The Cloud NetApp Volume message object
      protocols: A list of protocol enums

    Returns:
      Volume message populated with protocol values.

    """
    protocols_config = []
    for protocol in protocols:
      protocols_config.append(protocol)
    volume.protocols = protocols_config

  def ParseSnapshotPolicy(self, volume, snapshot_policy):
    """Parses Snapshot Policy from a list of snapshot schedules into a given Volume.

    Args:
      volume: The Cloud NetApp Volume message object
      snapshot_policy: A list of snapshot policies (schedules) to parse

    Returns:
      Volume messages populated with snapshotPolicy field
    """
    if not snapshot_policy:
      return
    volume.snapshotPolicy = self.messages.SnapshotPolicy()
    volume.snapshotPolicy.enabled = True
    for name, snapshot_schedule in snapshot_policy.items():
      if name == 'hourly_snapshot':
        schedule = self.messages.HourlySchedule()
        schedule.snapshotsToKeep = snapshot_schedule.get('snapshots-to-keep')
        schedule.minute = snapshot_schedule.get('minute', 0)
        volume.snapshotPolicy.hourlySchedule = schedule
      elif name == 'daily_snapshot':
        schedule = self.messages.DailySchedule()
        schedule.snapshotsToKeep = snapshot_schedule.get('snapshots-to-keep')
        schedule.minute = snapshot_schedule.get('minute', 0)
        schedule.hour = snapshot_schedule.get('hour', 0)
        volume.snapshotPolicy.dailySchedule = schedule
      elif name == 'weekly_snapshot':
        schedule = self.messages.WeeklySchedule()
        schedule.snapshotsToKeep = snapshot_schedule.get('snapshots-to-keep')
        schedule.minute = snapshot_schedule.get('minute', 0)
        schedule.hour = snapshot_schedule.get('hour', 0)
        schedule.day = snapshot_schedule.get('day', 'Sunday')
        volume.snapshotPolicy.weeklySchedule = schedule
      elif name == 'monthly-snapshot':
        schedule = self.messages.MonthlySchedule()
        schedule.snapshotsToKeep = snapshot_schedule.get('snapshots-to-keep')
        schedule.minute = snapshot_schedule.get('minute', 0)
        schedule.hour = snapshot_schedule.get('hour', 0)
        schedule.day = snapshot_schedule.get('day', 1)
        volume.snapshotPolicy.monthlySchedule = schedule

  def UpdateVolume(self, volume_ref, volume_config, update_mask):
    """Send a Patch request for the Cloud NetApp Volume."""
    update_request = self.messages.NetappProjectsLocationsVolumesPatchRequest(
        volume=volume_config,
        name=volume_ref.RelativeName(),
        updateMask=update_mask)
    update_op = self.client.projects_locations_volumes.Patch(update_request)
    return update_op

  def ParseUpdatedVolumeConfig(self,
                               volume_config,
                               description=None,
                               labels=None,
                               storage_pool=None,
                               protocols=None,
                               share_name=None,
                               export_policy=None,
                               capacity=None,
                               network=None,
                               unix_permissions=None,
                               smb_settings=None,
                               snapshot_policy=None,
                               snap_reserve=None,
                               snapshot_directory=None,
                               security_style=None,
                               enable_kerberos=None,
                               enable_ldap=None,
                               active_directory=None):
    """Parse update information into an updated Volume message."""
    if description:
      volume_config.description = description
    if labels:
      volume_config.labels = labels
    if capacity:
      volume_config.capacityGib = capacity
    if storage_pool:
      volume_config.storagePoolName = storage_pool
    if protocols:
      self.ParseProtocols(volume_config, protocols)
    if share_name:
      volume_config.shareName = share_name
    if export_policy:
      self.ParseExportPolicy(volume_config, export_policy)
    if network:
      volume_config.network = network.get('name')
      if 'reserved-ip-range' in network:
        volume_config.psaRange = network.get('reserved-ip-range')
    if unix_permissions:
      volume_config.unixPermissions = unix_permissions
    if smb_settings:
      volume_config.smbSettings = smb_settings
    if snapshot_policy:
      self.ParseSnapshotPolicy(volume_config, snapshot_policy)
    if snap_reserve:
      volume_config.snapReserve = snap_reserve
    if snapshot_directory:
      volume_config.snapshotDirectory = snapshot_directory
    if security_style:
      volume_config.securityStyle = security_style
    if enable_kerberos:
      volume_config.kerberosEnabled = enable_kerberos
    if enable_ldap:
      volume_config.ldapEnabled = enable_ldap
    if active_directory:
      volume_config.activeDirectoryName = active_directory
    return volume_config
