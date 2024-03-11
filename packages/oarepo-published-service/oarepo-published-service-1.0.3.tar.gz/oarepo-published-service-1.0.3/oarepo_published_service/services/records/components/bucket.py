from invenio_records_resources.services.records.components import ServiceComponent
class CreatePublishedBucketComponent(ServiceComponent):
    def create(self, identity, *, record, **kwargs):
        record.files.create_bucket()