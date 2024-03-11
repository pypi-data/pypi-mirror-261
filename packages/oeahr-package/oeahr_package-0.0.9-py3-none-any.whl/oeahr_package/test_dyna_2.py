from promptflow import tool
from promptflow.connections import AzureOpenAIConnection
from promptflow.entities import InputSetting, DynamicList
from utils import list_deployment_names


deployment_names_dynamic_list_setting = DynamicList(function=list_deployment_names, input_mapping={"connection_name": "connection"})


# The inputs section will change based on the arguments of the tool function, after you save the code
# Adding type to arguments and return value will help the system show the types properly
# Please update the function name/signature per need
@tool(description="list func in utils.py", input_settings={
    "deployment_name": InputSetting(
        dynamic_list=deployment_names_dynamic_list_setting,
        is_multi_select=False
    )})
def test_dynamic_list_2(connection: AzureOpenAIConnection, deployment_name: str) -> str:
    # llm call...
    return 'hello ' + deployment_name
