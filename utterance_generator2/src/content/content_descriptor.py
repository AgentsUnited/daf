_content_descriptors = {}

def content_descriptor(klass):
    if issubclass(klass, ContentDescriptor):
        _content_descriptors[klass.__name__.lower()] = klass
    else:
        print("Warning: content descriptors must be sub-classes of ContentDescriptor")

    return klass


class ContentDescriptor:

    def find_content(self, query, existing_content=None):
        pass
