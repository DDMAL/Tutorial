from django.conf import settings
import pysolr


def __solr_prepare(instances):
    """
        Both index and delete require the step of checking
        to see if the requested documents exist. For indexing, this is so we don't get
        duplicate records in the index; for deleting, it's rather obvious.

        This method deletes the documents in question and returns the connection object.

        If further action is required (i.e., actually indexing) the calling method
        can re-use the connection object to do this.

        An array of model instances must be passed to this method. For single instances,
        the caller should wrap it in an array of length 1 before passing it in.
    """
    connection = pysolr.Solr(settings.SOLR['SERVER'])

    for instance in instances:
        fq = [
            'type:{0}'.format(instance.__class__.__name__.lower()),
            'pk:{0}'.format(instance.pk)
        ]
        records = connection.search("*:*", fq=fq, fl='id')
        if records.hits > 0:
            for doc in records.docs:
                connection.delete(id=doc['id'])

    return connection


def solr_index(serializer, instances):
    """
        Indexes an array of model instances.

        Calling methods should wrap single instances in a list before passing them in to this method.
    """
    connection = __solr_prepare(instances)
    serialized = serializer(instances, many=True)
    data = serialized.data
    connection.add(data)
    connection.commit()


def solr_delete(instances):
    """
        Deletes an array of model instances from the Solr system.

        Calling methods should wrap single instances in a list before passing them in to this method.
    """
    __solr_prepare(instances)
