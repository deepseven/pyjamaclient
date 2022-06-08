# VersionedItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**document_key** | **str** |  | 
**global_id** | **str** |  | 
**project** | **int** | ID of a project | 
**item_type** | **int** | ID of an item type | 
**child_item_type** | **int** | ID of an item type | 
**created_date** | **datetime** |  | 
**modified_date** | **datetime** |  | 
**last_activity_date** | **datetime** |  | 
**created_by** | **int** | ID of a user | 
**modified_by** | **int** | ID of a user | 
**resources** | [**{str: (AllowedResource,)}**](AllowedResource.md) | A set of resources and allowed permissions | 
**fields** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type,)}** | A map of field names to field values e.g. {\&quot;name\&quot;:\&quot;Sample Item\&quot;, \&quot;status\&quot;: 292, \&quot;release\&quot;: 2, \&quot;assigned\&quot;: 23} | 
**version** | **int** |  | [optional] 
**current_version** | **int** | Currently active version of the versioned item. If no version is active, currentVersion will not be returned. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


