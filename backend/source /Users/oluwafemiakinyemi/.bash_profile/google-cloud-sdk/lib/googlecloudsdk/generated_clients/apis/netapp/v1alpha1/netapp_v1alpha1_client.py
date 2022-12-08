"""Generated client library for netapp version v1alpha1."""
# NOTE: This file is autogenerated and should not be edited by hand.

from __future__ import absolute_import

from apitools.base.py import base_api
from googlecloudsdk.generated_clients.apis.netapp.v1alpha1 import netapp_v1alpha1_messages as messages


class NetappV1alpha1(base_api.BaseApiClient):
  """Generated client library for service netapp version v1alpha1."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://netapp.googleapis.com/'
  MTLS_BASE_URL = 'https://netapp.mtls.googleapis.com/'

  _PACKAGE = 'netapp'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
  _VERSION = 'v1alpha1'
  _CLIENT_ID = 'CLIENT_ID'
  _CLIENT_SECRET = 'CLIENT_SECRET'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'NetappV1alpha1'
  _URL_VERSION = 'v1alpha1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new netapp handle."""
    url = url or self.BASE_URL
    super(NetappV1alpha1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.projects_locations_activeDirectories = self.ProjectsLocationsActiveDirectoriesService(self)
    self.projects_locations_operations = self.ProjectsLocationsOperationsService(self)
    self.projects_locations_storagePools = self.ProjectsLocationsStoragePoolsService(self)
    self.projects_locations_volumes_snapshots = self.ProjectsLocationsVolumesSnapshotsService(self)
    self.projects_locations_volumes = self.ProjectsLocationsVolumesService(self)
    self.projects_locations = self.ProjectsLocationsService(self)
    self.projects = self.ProjectsService(self)

  class ProjectsLocationsActiveDirectoriesService(base_api.BaseApiService):
    """Service class for the projects_locations_activeDirectories resource."""

    _NAME = 'projects_locations_activeDirectories'

    def __init__(self, client):
      super(NetappV1alpha1.ProjectsLocationsActiveDirectoriesService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""CreateActiveDirectory Creates the active directory specified in the request.

      Args:
        request: (NetappProjectsLocationsActiveDirectoriesCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/activeDirectories',
        http_method='POST',
        method_id='netapp.projects.locations.activeDirectories.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['activeDirectoryId'],
        relative_path='v1alpha1/{+parent}/activeDirectories',
        request_field='activeDirectory',
        request_type_name='NetappProjectsLocationsActiveDirectoriesCreateRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""DeleteActiveDirectory Delete the active directory specified in the request.

      Args:
        request: (NetappProjectsLocationsActiveDirectoriesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/activeDirectories/{activeDirectoriesId}',
        http_method='DELETE',
        method_id='netapp.projects.locations.activeDirectories.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha1/{+name}',
        request_field='',
        request_type_name='NetappProjectsLocationsActiveDirectoriesDeleteRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""DescribeActiveDirectory Describes a specified active directory.

      Args:
        request: (NetappProjectsLocationsActiveDirectoriesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ActiveDirectory) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/activeDirectories/{activeDirectoriesId}',
        http_method='GET',
        method_id='netapp.projects.locations.activeDirectories.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha1/{+name}',
        request_field='',
        request_type_name='NetappProjectsLocationsActiveDirectoriesGetRequest',
        response_type_name='ActiveDirectory',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""ListActiveDirectories Lists active directories.

      Args:
        request: (NetappProjectsLocationsActiveDirectoriesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListActiveDirectoriesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/activeDirectories',
        http_method='GET',
        method_id='netapp.projects.locations.activeDirectories.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'orderBy', 'pageSize', 'pageToken'],
        relative_path='v1alpha1/{+parent}/activeDirectories',
        request_field='',
        request_type_name='NetappProjectsLocationsActiveDirectoriesListRequest',
        response_type_name='ListActiveDirectoriesResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""UpdateActiveDirectory Update the parameters of an active directories.

      Args:
        request: (NetappProjectsLocationsActiveDirectoriesPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/activeDirectories/{activeDirectoriesId}',
        http_method='PATCH',
        method_id='netapp.projects.locations.activeDirectories.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['updateMask'],
        relative_path='v1alpha1/{+name}',
        request_field='activeDirectory',
        request_type_name='NetappProjectsLocationsActiveDirectoriesPatchRequest',
        response_type_name='Operation',
        supports_download=False,
    )

  class ProjectsLocationsOperationsService(base_api.BaseApiService):
    """Service class for the projects_locations_operations resource."""

    _NAME = 'projects_locations_operations'

    def __init__(self, client):
      super(NetappV1alpha1.ProjectsLocationsOperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Cancel(self, request, global_params=None):
      r"""Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Clients can use Operations.GetOperation or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an Operation.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`.

      Args:
        request: (NetappProjectsLocationsOperationsCancelRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Cancel')
      return self._RunMethod(
          config, request, global_params=global_params)

    Cancel.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}:cancel',
        http_method='POST',
        method_id='netapp.projects.locations.operations.cancel',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha1/{+name}:cancel',
        request_field='cancelOperationRequest',
        request_type_name='NetappProjectsLocationsOperationsCancelRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a long-running operation. This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`.

      Args:
        request: (NetappProjectsLocationsOperationsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}',
        http_method='DELETE',
        method_id='netapp.projects.locations.operations.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha1/{+name}',
        request_field='',
        request_type_name='NetappProjectsLocationsOperationsDeleteRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

      Args:
        request: (NetappProjectsLocationsOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/operations/{operationsId}',
        http_method='GET',
        method_id='netapp.projects.locations.operations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha1/{+name}',
        request_field='',
        request_type_name='NetappProjectsLocationsOperationsGetRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`. NOTE: the `name` binding allows API services to override the binding to use different resource name schemes, such as `users/*/operations`. To override the binding, API services can add a binding such as `"/v1/{name=users/*}/operations"` to their service configuration. For backwards compatibility, the default name includes the operations collection id, however overriding users must ensure the name binding is the parent resource, without the operations collection id.

      Args:
        request: (NetappProjectsLocationsOperationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListOperationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/operations',
        http_method='GET',
        method_id='netapp.projects.locations.operations.list',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1alpha1/{+name}/operations',
        request_field='',
        request_type_name='NetappProjectsLocationsOperationsListRequest',
        response_type_name='ListOperationsResponse',
        supports_download=False,
    )

  class ProjectsLocationsStoragePoolsService(base_api.BaseApiService):
    """Service class for the projects_locations_storagePools resource."""

    _NAME = 'projects_locations_storagePools'

    def __init__(self, client):
      super(NetappV1alpha1.ProjectsLocationsStoragePoolsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""CreateStoragePool Creates a new storage pool.

      Args:
        request: (NetappProjectsLocationsStoragePoolsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/storagePools',
        http_method='POST',
        method_id='netapp.projects.locations.storagePools.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['storagePoolId'],
        relative_path='v1alpha1/{+parent}/storagePools',
        request_field='storagePool',
        request_type_name='NetappProjectsLocationsStoragePoolsCreateRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""DeleteStoragePool Warning! This operation will permanently delete the storage pool.

      Args:
        request: (NetappProjectsLocationsStoragePoolsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/storagePools/{storagePoolsId}',
        http_method='DELETE',
        method_id='netapp.projects.locations.storagePools.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha1/{+name}',
        request_field='',
        request_type_name='NetappProjectsLocationsStoragePoolsDeleteRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""GetStoragePool Returns the description of the specified storage pool by poolId.

      Args:
        request: (NetappProjectsLocationsStoragePoolsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (StoragePool) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/storagePools/{storagePoolsId}',
        http_method='GET',
        method_id='netapp.projects.locations.storagePools.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha1/{+name}',
        request_field='',
        request_type_name='NetappProjectsLocationsStoragePoolsGetRequest',
        response_type_name='StoragePool',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""ListStoragePools Returns descriptions of all storage pools owned by the caller.

      Args:
        request: (NetappProjectsLocationsStoragePoolsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListStoragePoolsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/storagePools',
        http_method='GET',
        method_id='netapp.projects.locations.storagePools.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'orderBy', 'pageSize', 'pageToken'],
        relative_path='v1alpha1/{+parent}/storagePools',
        request_field='',
        request_type_name='NetappProjectsLocationsStoragePoolsListRequest',
        response_type_name='ListStoragePoolsResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""UpdateStoragePool Updates the storage pool properties with the full spec.

      Args:
        request: (NetappProjectsLocationsStoragePoolsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/storagePools/{storagePoolsId}',
        http_method='PATCH',
        method_id='netapp.projects.locations.storagePools.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['updateMask'],
        relative_path='v1alpha1/{+name}',
        request_field='storagePool',
        request_type_name='NetappProjectsLocationsStoragePoolsPatchRequest',
        response_type_name='Operation',
        supports_download=False,
    )

  class ProjectsLocationsVolumesSnapshotsService(base_api.BaseApiService):
    """Service class for the projects_locations_volumes_snapshots resource."""

    _NAME = 'projects_locations_volumes_snapshots'

    def __init__(self, client):
      super(NetappV1alpha1.ProjectsLocationsVolumesSnapshotsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Create a new snapshot for a volume.

      Args:
        request: (NetappProjectsLocationsVolumesSnapshotsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/volumes/{volumesId}/snapshots',
        http_method='POST',
        method_id='netapp.projects.locations.volumes.snapshots.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['snapshotId'],
        relative_path='v1alpha1/{+parent}/snapshots',
        request_field='snapshot',
        request_type_name='NetappProjectsLocationsVolumesSnapshotsCreateRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a snapshot.

      Args:
        request: (NetappProjectsLocationsVolumesSnapshotsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/volumes/{volumesId}/snapshots/{snapshotsId}',
        http_method='DELETE',
        method_id='netapp.projects.locations.volumes.snapshots.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha1/{+name}',
        request_field='',
        request_type_name='NetappProjectsLocationsVolumesSnapshotsDeleteRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Describe a snapshot for a volume.

      Args:
        request: (NetappProjectsLocationsVolumesSnapshotsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Snapshot) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/volumes/{volumesId}/snapshots/{snapshotsId}',
        http_method='GET',
        method_id='netapp.projects.locations.volumes.snapshots.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha1/{+name}',
        request_field='',
        request_type_name='NetappProjectsLocationsVolumesSnapshotsGetRequest',
        response_type_name='Snapshot',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Returns descriptions of all snapshots for a volume.

      Args:
        request: (NetappProjectsLocationsVolumesSnapshotsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListSnapshotsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/volumes/{volumesId}/snapshots',
        http_method='GET',
        method_id='netapp.projects.locations.volumes.snapshots.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'orderBy', 'pageSize', 'pageToken'],
        relative_path='v1alpha1/{+parent}/snapshots',
        request_field='',
        request_type_name='NetappProjectsLocationsVolumesSnapshotsListRequest',
        response_type_name='ListSnapshotsResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Updates the settings of a specific snapshot.

      Args:
        request: (NetappProjectsLocationsVolumesSnapshotsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/volumes/{volumesId}/snapshots/{snapshotsId}',
        http_method='PATCH',
        method_id='netapp.projects.locations.volumes.snapshots.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['updateMask'],
        relative_path='v1alpha1/{+name}',
        request_field='snapshot',
        request_type_name='NetappProjectsLocationsVolumesSnapshotsPatchRequest',
        response_type_name='Operation',
        supports_download=False,
    )

  class ProjectsLocationsVolumesService(base_api.BaseApiService):
    """Service class for the projects_locations_volumes resource."""

    _NAME = 'projects_locations_volumes'

    def __init__(self, client):
      super(NetappV1alpha1.ProjectsLocationsVolumesService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""CreateVolume Creates a new Volume in a given project and location.

      Args:
        request: (NetappProjectsLocationsVolumesCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/volumes',
        http_method='POST',
        method_id='netapp.projects.locations.volumes.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['volumeId'],
        relative_path='v1alpha1/{+parent}/volumes',
        request_field='volume',
        request_type_name='NetappProjectsLocationsVolumesCreateRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""DeleteVolume Deletes a single Volume.

      Args:
        request: (NetappProjectsLocationsVolumesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/volumes/{volumesId}',
        http_method='DELETE',
        method_id='netapp.projects.locations.volumes.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['force'],
        relative_path='v1alpha1/{+name}',
        request_field='',
        request_type_name='NetappProjectsLocationsVolumesDeleteRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""GetVolume Gets details of a single Volume.

      Args:
        request: (NetappProjectsLocationsVolumesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Volume) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/volumes/{volumesId}',
        http_method='GET',
        method_id='netapp.projects.locations.volumes.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha1/{+name}',
        request_field='',
        request_type_name='NetappProjectsLocationsVolumesGetRequest',
        response_type_name='Volume',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""ListVolumes Lists Volumes in a given project.

      Args:
        request: (NetappProjectsLocationsVolumesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListVolumesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/volumes',
        http_method='GET',
        method_id='netapp.projects.locations.volumes.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['filter', 'orderBy', 'pageSize', 'pageToken'],
        relative_path='v1alpha1/{+parent}/volumes',
        request_field='',
        request_type_name='NetappProjectsLocationsVolumesListRequest',
        response_type_name='ListVolumesResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""UpdateVolume Updates the parameters of a single Volume.

      Args:
        request: (NetappProjectsLocationsVolumesPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/volumes/{volumesId}',
        http_method='PATCH',
        method_id='netapp.projects.locations.volumes.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['updateMask'],
        relative_path='v1alpha1/{+name}',
        request_field='volume',
        request_type_name='NetappProjectsLocationsVolumesPatchRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Revert(self, request, global_params=None):
      r"""Revert an existing volume to a specified snapshot. Warning! This operation will permanently revert all changes made after the snapshot was created.

      Args:
        request: (NetappProjectsLocationsVolumesRevertRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Revert')
      return self._RunMethod(
          config, request, global_params=global_params)

    Revert.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}/volumes/{volumesId}:revert',
        http_method='POST',
        method_id='netapp.projects.locations.volumes.revert',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha1/{+name}:revert',
        request_field='revertVolumeRequest',
        request_type_name='NetappProjectsLocationsVolumesRevertRequest',
        response_type_name='Operation',
        supports_download=False,
    )

  class ProjectsLocationsService(base_api.BaseApiService):
    """Service class for the projects_locations resource."""

    _NAME = 'projects_locations'

    def __init__(self, client):
      super(NetappV1alpha1.ProjectsLocationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Get(self, request, global_params=None):
      r"""Gets information about a location.

      Args:
        request: (NetappProjectsLocationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Location) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations/{locationsId}',
        http_method='GET',
        method_id='netapp.projects.locations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1alpha1/{+name}',
        request_field='',
        request_type_name='NetappProjectsLocationsGetRequest',
        response_type_name='Location',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists information about the supported locations for this service.

      Args:
        request: (NetappProjectsLocationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListLocationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1alpha1/projects/{projectsId}/locations',
        http_method='GET',
        method_id='netapp.projects.locations.list',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1alpha1/{+name}/locations',
        request_field='',
        request_type_name='NetappProjectsLocationsListRequest',
        response_type_name='ListLocationsResponse',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = 'projects'

    def __init__(self, client):
      super(NetappV1alpha1.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }
