# RequestParent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item** | **int** | ID of an item. If this is included, the item of this payload will be located at this parent item. If this is not included, the item will be located at the root of the project. | [optional] 
**project** | **int** | ID of an project. If this is included, the item of this payload will be located at the root of the project, and a parent item cannot be specified. This value will be inferred by the \&quot;project\&quot; property at the root of the payload when a parent location is not specified. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


