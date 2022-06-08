# TestRun


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**document_key** | **str** |  | 
**global_id** | **str** |  | 
**project** | **int** | ID of a project | 
**item_type** | **int** | ID of an item type | 
**created_date** | **datetime** |  | 
**modified_date** | **datetime** |  | 
**last_activity_date** | **datetime** |  | 
**created_by** | **int** | ID of a user | 
**modified_by** | **int** | ID of a user | 
**test_case_version_number** | **int** | The version of the test case at the time of test run creation | 
**sort_order_from_test_group** | **int** | The sort order within the test group at the time of test cycle creation | 
**test_group** | **[int]** | ID of a test cycle and ID of a test group | 
**resources** | [**{str: (AllowedResource,)}**](AllowedResource.md) | A set of resources and allowed permissions | 
**fields** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type,)}** | A map of field names to field values e.g. {\&quot;name\&quot;:\&quot;Sample Item\&quot;, \&quot;status\&quot;: 292, \&quot;release\&quot;: 2, \&quot;assigned\&quot;: 23} | 
**test_case_current_version_number** | **int** | The current version of the test case that the test run is based on | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


