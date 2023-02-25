from playground.resource.dummy.dummy_resource import \
    dummy

RESOURCE_MAP = {
    '/dummy': dummy,
}


def invoke_resource(event_data):
    return RESOURCE_MAP.get(event_data.get('resource_path'))(event_data)
