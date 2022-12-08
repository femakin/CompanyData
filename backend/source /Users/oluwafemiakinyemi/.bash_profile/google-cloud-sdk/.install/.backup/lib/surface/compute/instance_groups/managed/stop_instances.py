# -*- coding: utf-8 -*- #
# Copyright 2021 Google LLC. All Rights Reserved.
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
"""Command for stoping instances owned by a managed instance group."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.api_lib.compute import base_classes
from googlecloudsdk.api_lib.compute import instance_groups_utils
from googlecloudsdk.calliope import arg_parsers
from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.compute import flags
from googlecloudsdk.command_lib.compute import scope as compute_scope
from googlecloudsdk.command_lib.compute.instance_groups import flags as instance_groups_flags


@base.ReleaseTracks(base.ReleaseTrack.ALPHA)
class StopInstances(base.Command):
  """Stop instances owned by a managed instance group."""

  @staticmethod
  def Args(parser):
    parser.display_info.AddFormat("""
        table(project(),
              zone(),
              instanceName:label=INSTANCE,
              status)""")
    parser.add_argument('--instances',
                        type=arg_parsers.ArgList(min_length=1),
                        metavar='INSTANCE',
                        required=True,
                        help='Names of instances to stop.')
    parser.add_argument(
        '--force',
        default=False,
        action='store_true',
        help="""
          Immediately stop the specified instances, skipping the initial
          delay, if one is specified in the standby policy.""")
    instance_groups_flags.MULTISCOPE_INSTANCE_GROUP_MANAGER_ARG.AddArgument(
        parser)

  def Run(self, args):
    holder = base_classes.ComputeApiHolder(self.ReleaseTrack())
    client = holder.client

    resource_arg = instance_groups_flags.MULTISCOPE_INSTANCE_GROUP_MANAGER_ARG
    default_scope = compute_scope.ScopeEnum.ZONE
    scope_lister = flags.GetDefaultScopeLister(client)
    igm_ref = resource_arg.ResolveAsResource(
        args,
        holder.resources,
        default_scope=default_scope,
        scope_lister=scope_lister)

    if igm_ref.Collection() == 'compute.instanceGroupManagers':
      instances_holder_field = 'instanceGroupManagersStopInstancesRequest'
      request = client.messages.ComputeInstanceGroupManagersStopInstancesRequest(
          instanceGroupManager=igm_ref.Name(),
          instanceGroupManagersStopInstancesRequest=client.messages
          .InstanceGroupManagersStopInstancesRequest(instances=[]),
          project=igm_ref.project,
          zone=igm_ref.zone)
    elif igm_ref.Collection() == 'compute.regionInstanceGroupManagers':
      instances_holder_field = 'regionInstanceGroupManagersStopInstancesRequest'
      request = client.messages.ComputeRegionInstanceGroupManagersStopInstancesRequest(
          instanceGroupManager=igm_ref.Name(),
          regionInstanceGroupManagersStopInstancesRequest=client.messages
          .RegionInstanceGroupManagersStopInstancesRequest(instances=[]),
          project=igm_ref.project,
          region=igm_ref.region,
      )
    else:
      raise ValueError('Unknown reference type {0}'.format(
          igm_ref.Collection()))

    if args.IsSpecified('force'):
      if igm_ref.Collection() == 'compute.instanceGroupManagers':
        request.instanceGroupManagersStopInstancesRequest.forceStop = args.force
      else:
        request.regionInstanceGroupManagersStopInstancesRequest.forceStop = args.force

    return instance_groups_utils.SendInstancesRequestsAndPostProcessOutputs(
        api_holder=holder,
        method_name='StopInstances',
        request_template=request,
        instances_holder_field=instances_holder_field,
        igm_ref=igm_ref,
        instances=args.instances)


StopInstances.detailed_help = {
    'brief':
        'Stop instances owned by a managed instance group.',
    'DESCRIPTION':
        """
        *{command}* stops one or more instances from a managed instance group
""",
}
