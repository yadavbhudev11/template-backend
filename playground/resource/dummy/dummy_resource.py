
from playground.resource.dummy.dummy_rename_utils import dummy_util
def dummy(event_data):
    http_method = event_data.get('resource_method')

    if(http_method == 'POST'):
        data = event_data.get('body')
        return dummy_util(data)


