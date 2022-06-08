# RequestItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project** | **int** | Only required when creating a new item (POST). | 
**item_type** | **int** | ID of an item type | 
**child_item_type** | **int** | ID of an item type | 
**location** | [**RequestLocation**](RequestLocation.md) |  | 
**fields** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type,)}** | A map of field names to field values e.g. {\&quot;name\&quot;:\&quot;Sample Item\&quot;, \&quot;status\&quot;: 292, \&quot;release\&quot;: 2, \&quot;assigned\&quot;: 23} | 
**global_id** | **str** | Must use override if you want to set this value on POST. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


