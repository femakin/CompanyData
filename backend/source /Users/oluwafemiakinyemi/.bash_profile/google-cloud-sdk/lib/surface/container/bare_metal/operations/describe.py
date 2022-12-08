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
"""Command to describe an operation."""

from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from googlecloudsdk.api_lib.container.gkeonprem import operations
from googlecloudsdk.calliope import base
from googlecloudsdk.command_lib.container.bare_metal import cluster_flags


_EXAMPLES = """
To describe an operation in location ``us-west1'', run:

$ {command} OPERATION_ID --location=us-west1
"""


@base.ReleaseTracks(base.ReleaseTrack.ALPHA)
class Describe(base.DescribeCommand):
  """Describe an operation."""
  detailed_help = {'EXAMPLES': _EXAMPLES}

  @staticmethod
  def Args(parser):
    """Registers flags for this command."""
    cluster_flags.AddOperationResourceArg(parser, 'to describe')

  def Run(self, args):
    """Runs the describe command."""
    operation_client = operations.OperationsClient()
    operation_ref = args.CONCEPTS.operation_id.Parse()
    return operation_client.Describe(operation_ref)
