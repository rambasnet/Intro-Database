# MongoDB CRUD Statements

- documentation - [https://www.mongodb.com/docs/manual/crud/](https://www.mongodb.com/docs/manual/crud/)
- 
## Create Database, Collection, Documents
- connect to your Atlas server
- create database, collection, and documents


```python
from pymongo import MongoClient
from pymongo.server_api import ServerApi
```


```python
from pymongo.errors import OperationFailure
```


```python
path_to_certificate = 'python/x509-cert-MongoDB-Atlas.pem'
```


```python
uri = "mongodb+srv://cluster0.xeszaub.mongodb.net/?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"
```


```python
client = MongoClient(uri,
                     tls=True,
                     tlsCertificateKeyFile=path_to_certificate,
                     server_api=ServerApi('1'))
```


```python
# Create database called myDatabase
db = client.myDatabase
```


```python
# create a collection named 'recipes'
# collection is equivalent to table
my_collection = db.recipes
```


```python
# drop collection in case it already exists
try:
    my_collection.drop()
except pymongo.errors.OperationFailure as ex:
    print("An authentication error was received. Are you sure your uri/certificate is correct?")
    raise ex
```


```python
help(my_collection)
```

    Help on Collection in module pymongo.collection object:
    
    class Collection(pymongo.common.BaseObject, typing.Generic)
     |  Collection(database: 'Database[_DocumentType]', name: 'str', create: 'Optional[bool]' = False, codec_options: 'Optional[CodecOptions[_DocumentTypeArg]]' = None, read_preference: 'Optional[_ServerMode]' = None, write_concern: 'Optional[WriteConcern]' = None, read_concern: 'Optional[ReadConcern]' = None, session: 'Optional[ClientSession]' = None, **kwargs: 'Any') -> 'None'
     |
     |  A Mongo collection.
     |
     |  Method resolution order:
     |      Collection
     |      pymongo.common.BaseObject
     |      typing.Generic
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __bool__(self) -> 'NoReturn'
     |
     |  __call__(self, *args: 'Any', **kwargs: 'Any') -> 'NoReturn'
     |      This is only here so that some API misusages are easier to debug.
     |
     |  __eq__(self, other: 'Any') -> 'bool'
     |      Return self==value.
     |
     |  __getattr__(self, name: 'str') -> 'Collection[_DocumentType]'
     |      Get a sub-collection of this collection by name.
     |
     |      Raises InvalidName if an invalid collection name is used.
     |
     |      :Parameters:
     |        - `name`: the name of the collection to get
     |
     |  __getitem__(self, name: 'str') -> 'Collection[_DocumentType]'
     |
     |  __hash__(self) -> 'int'
     |      Return hash(self).
     |
     |  __init__(self, database: 'Database[_DocumentType]', name: 'str', create: 'Optional[bool]' = False, codec_options: 'Optional[CodecOptions[_DocumentTypeArg]]' = None, read_preference: 'Optional[_ServerMode]' = None, write_concern: 'Optional[WriteConcern]' = None, read_concern: 'Optional[ReadConcern]' = None, session: 'Optional[ClientSession]' = None, **kwargs: 'Any') -> 'None'
     |      Get / create a Mongo collection.
     |
     |      Raises :class:`TypeError` if `name` is not an instance of
     |      :class:`str`. Raises :class:`~pymongo.errors.InvalidName` if `name` is
     |      not a valid collection name. Any additional keyword arguments will be used
     |      as options passed to the create command. See
     |      :meth:`~pymongo.database.Database.create_collection` for valid
     |      options.
     |
     |      If `create` is ``True``, `collation` is specified, or any additional
     |      keyword arguments are present, a ``create`` command will be
     |      sent, using ``session`` if specified. Otherwise, a ``create`` command
     |      will not be sent and the collection will be created implicitly on first
     |      use. The optional ``session`` argument is *only* used for the ``create``
     |      command, it is not associated with the collection afterward.
     |
     |      :Parameters:
     |        - `database`: the database to get a collection from
     |        - `name`: the name of the collection to get
     |        - `create` (optional): if ``True``, force collection
     |          creation even without options being set
     |        - `codec_options` (optional): An instance of
     |          :class:`~bson.codec_options.CodecOptions`. If ``None`` (the
     |          default) database.codec_options is used.
     |        - `read_preference` (optional): The read preference to use. If
     |          ``None`` (the default) database.read_preference is used.
     |        - `write_concern` (optional): An instance of
     |          :class:`~pymongo.write_concern.WriteConcern`. If ``None`` (the
     |          default) database.write_concern is used.
     |        - `read_concern` (optional): An instance of
     |          :class:`~pymongo.read_concern.ReadConcern`. If ``None`` (the
     |          default) database.read_concern is used.
     |        - `collation` (optional): An instance of
     |          :class:`~pymongo.collation.Collation`. If a collation is provided,
     |          it will be passed to the create collection command.
     |        - `session` (optional): a
     |          :class:`~pymongo.client_session.ClientSession` that is used with
     |          the create collection command
     |        - `**kwargs` (optional): additional keyword arguments will
     |          be passed as options for the create collection command
     |
     |      .. versionchanged:: 4.2
     |         Added the ``clusteredIndex`` and ``encryptedFields`` parameters.
     |
     |      .. versionchanged:: 4.0
     |         Removed the reindex, map_reduce, inline_map_reduce,
     |         parallel_scan, initialize_unordered_bulk_op,
     |         initialize_ordered_bulk_op, group, count, insert, save,
     |         update, remove, find_and_modify, and ensure_index methods. See the
     |         :ref:`pymongo4-migration-guide`.
     |
     |      .. versionchanged:: 3.6
     |         Added ``session`` parameter.
     |
     |      .. versionchanged:: 3.4
     |         Support the `collation` option.
     |
     |      .. versionchanged:: 3.2
     |         Added the read_concern option.
     |
     |      .. versionchanged:: 3.0
     |         Added the codec_options, read_preference, and write_concern options.
     |         Removed the uuid_subtype attribute.
     |         :class:`~pymongo.collection.Collection` no longer returns an
     |         instance of :class:`~pymongo.collection.Collection` for attribute
     |         names with leading underscores. You must use dict-style lookups
     |         instead::
     |
     |             collection['__my_collection__']
     |
     |         Not:
     |
     |             collection.__my_collection__
     |
     |      .. seealso:: The MongoDB documentation on `collections <https://dochub.mongodb.org/core/collections>`_.
     |
     |  __ne__(self, other: 'Any') -> 'bool'
     |      Return self!=value.
     |
     |  __next__(self) -> 'NoReturn'
     |
     |  __repr__(self) -> 'str'
     |      Return repr(self).
     |
     |  aggregate(self, pipeline: '_Pipeline', session: 'Optional[ClientSession]' = None, let: 'Optional[Mapping[str, Any]]' = None, comment: 'Optional[Any]' = None, **kwargs: 'Any') -> 'CommandCursor[_DocumentType]'
     |      Perform an aggregation using the aggregation framework on this
     |      collection.
     |
     |      The :meth:`aggregate` method obeys the :attr:`read_preference` of this
     |      :class:`Collection`, except when ``$out`` or ``$merge`` are used on
     |      MongoDB <5.0, in which case
     |      :attr:`~pymongo.read_preferences.ReadPreference.PRIMARY` is used.
     |
     |      .. note:: This method does not support the 'explain' option. Please
     |         use `PyMongoExplain <https://pypi.org/project/pymongoexplain/>`_
     |         instead. An example is included in the :ref:`aggregate-examples`
     |         documentation.
     |
     |      .. note:: The :attr:`~pymongo.collection.Collection.write_concern` of
     |         this collection is automatically applied to this operation.
     |
     |      :Parameters:
     |        - `pipeline`: a list of aggregation pipeline stages
     |        - `session` (optional): a
     |          :class:`~pymongo.client_session.ClientSession`.
     |        - `**kwargs` (optional): extra `aggregate command`_ parameters.
     |
     |      All optional `aggregate command`_ parameters should be passed as
     |      keyword arguments to this method. Valid options include, but are not
     |      limited to:
     |
     |        - `allowDiskUse` (bool): Enables writing to temporary files. When set
     |          to True, aggregation stages can write data to the _tmp subdirectory
     |          of the --dbpath directory. The default is False.
     |        - `maxTimeMS` (int): The maximum amount of time to allow the operation
     |          to run in milliseconds.
     |        - `batchSize` (int): The maximum number of documents to return per
     |          batch. Ignored if the connected mongod or mongos does not support
     |          returning aggregate results using a cursor.
     |        - `collation` (optional): An instance of
     |          :class:`~pymongo.collation.Collation`.
     |        - `let` (dict): A dict of parameter names and values. Values must be
     |          constant or closed expressions that do not reference document
     |          fields. Parameters can then be accessed as variables in an
     |          aggregate expression context (e.g. ``"$$var"``). This option is
     |          only supported on MongoDB >= 5.0.
     |        - `comment` (optional): A user-provided comment to attach to this
     |          command.
     |
     |
     |      :Returns:
     |        A :class:`~pymongo.command_cursor.CommandCursor` over the result
     |        set.
     |
     |      .. versionchanged:: 4.1
     |         Added ``comment`` parameter.
     |         Added ``let`` parameter.
     |         Support $merge and $out executing on secondaries according to the
     |         collection's :attr:`read_preference`.
     |      .. versionchanged:: 4.0
     |         Removed the ``useCursor`` option.
     |      .. versionchanged:: 3.9
     |         Apply this collection's read concern to pipelines containing the
     |         `$out` stage when connected to MongoDB >= 4.2.
     |         Added support for the ``$merge`` pipeline stage.
     |         Aggregations that write always use read preference
     |         :attr:`~pymongo.read_preferences.ReadPreference.PRIMARY`.
     |      .. versionchanged:: 3.6
     |         Added the `session` parameter. Added the `maxAwaitTimeMS` option.
     |         Deprecated the `useCursor` option.
     |      .. versionchanged:: 3.4
     |         Apply this collection's write concern automatically to this operation
     |         when connected to MongoDB >= 3.4. Support the `collation` option.
     |      .. versionchanged:: 3.0
     |         The :meth:`aggregate` method always returns a CommandCursor. The
     |         pipeline argument must be a list.
     |
     |      .. seealso:: :doc:`/examples/aggregation`
     |
     |      .. _aggregate command:
     |          https://mongodb.com/docs/manual/reference/command/aggregate
     |
     |  aggregate_raw_batches(self, pipeline: '_Pipeline', session: 'Optional[ClientSession]' = None, comment: 'Optional[Any]' = None, **kwargs: 'Any') -> 'RawBatchCursor[_DocumentType]'
     |      Perform an aggregation and retrieve batches of raw BSON.
     |
     |      Similar to the :meth:`aggregate` method but returns a
     |      :class:`~pymongo.cursor.RawBatchCursor`.
     |
     |      This example demonstrates how to work with raw batches, but in practice
     |      raw batches should be passed to an external library that can decode
     |      BSON into another data type, rather than used with PyMongo's
     |      :mod:`bson` module.
     |
     |        >>> import bson
     |        >>> cursor = db.test.aggregate_raw_batches([
     |        ...     {'$project': {'x': {'$multiply': [2, '$x']}}}])
     |        >>> for batch in cursor:
     |        ...     print(bson.decode_all(batch))
     |
     |      .. note:: aggregate_raw_batches does not support auto encryption.
     |
     |      .. versionchanged:: 3.12
     |         Added session support.
     |
     |      .. versionadded:: 3.6
     |
     |  bulk_write(self, requests: 'Sequence[_WriteOp[_DocumentType]]', ordered: 'bool' = True, bypass_document_validation: 'bool' = False, session: 'Optional[ClientSession]' = None, comment: 'Optional[Any]' = None, let: 'Optional[Mapping]' = None) -> 'BulkWriteResult'
     |      Send a batch of write operations to the server.
     |
     |      Requests are passed as a list of write operation instances (
     |      :class:`~pymongo.operations.InsertOne`,
     |      :class:`~pymongo.operations.UpdateOne`,
     |      :class:`~pymongo.operations.UpdateMany`,
     |      :class:`~pymongo.operations.ReplaceOne`,
     |      :class:`~pymongo.operations.DeleteOne`, or
     |      :class:`~pymongo.operations.DeleteMany`).
     |
     |        >>> for doc in db.test.find({}):
     |        ...     print(doc)
     |        ...
     |        {'x': 1, '_id': ObjectId('54f62e60fba5226811f634ef')}
     |        {'x': 1, '_id': ObjectId('54f62e60fba5226811f634f0')}
     |        >>> # DeleteMany, UpdateOne, and UpdateMany are also available.
     |        ...
     |        >>> from pymongo import InsertOne, DeleteOne, ReplaceOne
     |        >>> requests = [InsertOne({'y': 1}), DeleteOne({'x': 1}),
     |        ...             ReplaceOne({'w': 1}, {'z': 1}, upsert=True)]
     |        >>> result = db.test.bulk_write(requests)
     |        >>> result.inserted_count
     |        1
     |        >>> result.deleted_count
     |        1
     |        >>> result.modified_count
     |        0
     |        >>> result.upserted_ids
     |        {2: ObjectId('54f62ee28891e756a6e1abd5')}
     |        >>> for doc in db.test.find({}):
     |        ...     print(doc)
     |        ...
     |        {'x': 1, '_id': ObjectId('54f62e60fba5226811f634f0')}
     |        {'y': 1, '_id': ObjectId('54f62ee2fba5226811f634f1')}
     |        {'z': 1, '_id': ObjectId('54f62ee28891e756a6e1abd5')}
     |
     |      :Parameters:
     |        - `requests`: A list of write operations (see examples above).
     |        - `ordered` (optional): If ``True`` (the default) requests will be
     |          performed on the server serially, in the order provided. If an error
     |          occurs all remaining operations are aborted. If ``False`` requests
     |          will be performed on the server in arbitrary order, possibly in
     |          parallel, and all operations will be attempted.
     |        - `bypass_document_validation`: (optional) If ``True``, allows the
     |          write to opt-out of document level validation. Default is
     |          ``False``.
     |        - `session` (optional): a
     |          :class:`~pymongo.client_session.ClientSession`.
     |        - `comment` (optional): A user-provided comment to attach to this
     |          command.
     |        - `let` (optional): Map of parameter names and values. Values must be
     |          constant or closed expressions that do not reference document
     |          fields. Parameters can then be accessed as variables in an
     |          aggregate expression context (e.g. "$$var").
     |
     |      :Returns:
     |        An instance of :class:`~pymongo.results.BulkWriteResult`.
     |
     |      .. seealso:: :ref:`writes-and-ids`
     |
     |      .. note:: `bypass_document_validation` requires server version
     |        **>= 3.2**
     |
     |      .. versionchanged:: 4.1
     |         Added ``comment`` parameter.
     |         Added ``let`` parameter.
     |
     |      .. versionchanged:: 3.6
     |         Added ``session`` parameter.
     |
     |      .. versionchanged:: 3.2
     |        Added bypass_document_validation support
     |
     |      .. versionadded:: 3.0
     |
     |  count_documents(self, filter: 'Mapping[str, Any]', session: 'Optional[ClientSession]' = None, comment: 'Optional[Any]' = None, **kwargs: 'Any') -> 'int'
     |      Count the number of documents in this collection.
     |
     |      .. note:: For a fast count of the total documents in a collection see
     |         :meth:`estimated_document_count`.
     |
     |      The :meth:`count_documents` method is supported in a transaction.
     |
     |      All optional parameters should be passed as keyword arguments
     |      to this method. Valid options include:
     |
     |        - `skip` (int): The number of matching documents to skip before
     |          returning results.
     |        - `limit` (int): The maximum number of documents to count. Must be
     |          a positive integer. If not provided, no limit is imposed.
     |        - `maxTimeMS` (int): The maximum amount of time to allow this
     |          operation to run, in milliseconds.
     |        - `collation` (optional): An instance of
     |          :class:`~pymongo.collation.Collation`.
     |        - `hint` (string or list of tuples): The index to use. Specify either
     |          the index name as a string or the index specification as a list of
     |          tuples (e.g. [('a', pymongo.ASCENDING), ('b', pymongo.ASCENDING)]).
     |
     |      The :meth:`count_documents` method obeys the :attr:`read_preference` of
     |      this :class:`Collection`.
     |
     |      .. note:: When migrating from :meth:`count` to :meth:`count_documents`
     |         the following query operators must be replaced:
     |
     |         +-------------+-------------------------------------+
     |         | Operator    | Replacement                         |
     |         +=============+=====================================+
     |         | $where      | `$expr`_                            |
     |         +-------------+-------------------------------------+
     |         | $near       | `$geoWithin`_ with `$center`_       |
     |         +-------------+-------------------------------------+
     |         | $nearSphere | `$geoWithin`_ with `$centerSphere`_ |
     |         +-------------+-------------------------------------+
     |
     |      :Parameters:
     |        - `filter` (required): A query document that selects which documents
     |          to count in the collection. Can be an empty document to count all
     |          documents.
     |        - `session` (optional): a
     |          :class:`~pymongo.client_session.ClientSession`.
     |        - `comment` (optional): A user-provided comment to attach to this
     |          command.
     |        - `**kwargs` (optional): See list of options above.
     |
     |
     |      .. versionadded:: 3.7
     |
     |      .. _$expr: https://mongodb.com/docs/manual/reference/operator/query/expr/
     |      .. _$geoWithin: https://mongodb.com/docs/manual/reference/operator/query/geoWithin/
     |      .. _$center: https://mongodb.com/docs/manual/reference/operator/query/center/
     |      .. _$centerSphere: https://mongodb.com/docs/manual/reference/operator/query/centerSphere/
     |
     |  create_index(self, keys: '_IndexKeyHint', session: 'Optional[ClientSession]' = None, comment: 'Optional[Any]' = None, **kwargs: 'Any') -> 'str'
     |      Creates an index on this collection.
     |
     |      Takes either a single key or a list containing (key, direction) pairs
     |      or keys.  If no direction is given, :data:`~pymongo.ASCENDING` will
     |      be assumed.
     |      The key(s) must be an instance of :class:`str`and the direction(s) must
     |      be one of (:data:`~pymongo.ASCENDING`, :data:`~pymongo.DESCENDING`,
     |      :data:`~pymongo.GEO2D`, :data:`~pymongo.GEOSPHERE`,
     |      :data:`~pymongo.HASHED`, :data:`~pymongo.TEXT`).
     |
     |      To create a single key ascending index on the key ``'mike'`` we just
     |      use a string argument::
     |
     |        >>> my_collection.create_index("mike")
     |
     |      For a compound index on ``'mike'`` descending and ``'eliot'``
     |      ascending we need to use a list of tuples::
     |
     |        >>> my_collection.create_index([("mike", pymongo.DESCENDING),
     |        ...                             "eliot"])
     |
     |      All optional index creation parameters should be passed as
     |      keyword arguments to this method. For example::
     |
     |        >>> my_collection.create_index([("mike", pymongo.DESCENDING)],
     |        ...                            background=True)
     |
     |      Valid options include, but are not limited to:
     |
     |        - `name`: custom name to use for this index - if none is
     |          given, a name will be generated.
     |        - `unique`: if ``True``, creates a uniqueness constraint on the
     |          index.
     |        - `background`: if ``True``, this index should be created in the
     |          background.
     |        - `sparse`: if ``True``, omit from the index any documents that lack
     |          the indexed field.
     |        - `bucketSize`: for use with geoHaystack indexes.
     |          Number of documents to group together within a certain proximity
     |          to a given longitude and latitude.
     |        - `min`: minimum value for keys in a :data:`~pymongo.GEO2D`
     |          index.
     |        - `max`: maximum value for keys in a :data:`~pymongo.GEO2D`
     |          index.
     |        - `expireAfterSeconds`: <int> Used to create an expiring (TTL)
     |          collection. MongoDB will automatically delete documents from
     |          this collection after <int> seconds. The indexed field must
     |          be a UTC datetime or the data will not expire.
     |        - `partialFilterExpression`: A document that specifies a filter for
     |          a partial index.
     |        - `collation` (optional): An instance of
     |          :class:`~pymongo.collation.Collation`.
     |        - `wildcardProjection`: Allows users to include or exclude specific
     |          field paths from a `wildcard index`_ using the {"$**" : 1} key
     |          pattern. Requires MongoDB >= 4.2.
     |        - `hidden`: if ``True``, this index will be hidden from the query
     |          planner and will not be evaluated as part of query plan
     |          selection. Requires MongoDB >= 4.4.
     |
     |      See the MongoDB documentation for a full list of supported options by
     |      server version.
     |
     |      .. warning:: `dropDups` is not supported by MongoDB 3.0 or newer. The
     |        option is silently ignored by the server and unique index builds
     |        using the option will fail if a duplicate value is detected.
     |
     |      .. note:: The :attr:`~pymongo.collection.Collection.write_concern` of
     |         this collection is automatically applied to this operation.
     |
     |      :Parameters:
     |        - `keys`: a single key or a list of (key, direction)
     |          pairs specifying the index to create
     |        - `session` (optional): a
     |          :class:`~pymongo.client_session.ClientSession`.
     |        - `comment` (optional): A user-provided comment to attach to this
     |          command.
     |        - `**kwargs` (optional): any additional index creation
     |          options (see the above list) should be passed as keyword
     |          arguments.
     |
     |      .. versionchanged:: 4.4
     |         Allow passing a list containing (key, direction) pairs
     |         or keys for the ``keys`` parameter.
     |      .. versionchanged:: 4.1
     |         Added ``comment`` parameter.
     |      .. versionchanged:: 3.11
     |         Added the ``hidden`` option.
     |      .. versionchanged:: 3.6
     |         Added ``session`` parameter. Added support for passing maxTimeMS
     |         in kwargs.
     |      .. versionchanged:: 3.4
     |         Apply this collection's write concern automatically to this operation
     |         when connected to MongoDB >= 3.4. Support the `collation` option.
     |      .. versionchanged:: 3.2
     |         Added partialFilterExpression to support partial indexes.
     |      .. versionchanged:: 3.0
     |         Renamed `key_or_list` to `keys`. Removed the `cache_for` option.
     |         :meth:`create_index` no longer caches index names. Removed support
     |         for the drop_dups and bucket_size aliases.
     |
     |      .. seealso:: The MongoDB documentation on `indexes <https://dochub.mongodb.org/core/indexes>`_.
     |
     |      .. _wildcard index: https://dochub.mongodb.org/core/index-wildcard/
     |
     |  create_indexes(self, indexes: 'Sequence[IndexModel]', session: 'Optional[ClientSession]' = None, comment: 'Optional[Any]' = None, **kwargs: 'Any') -> 'List[str]'
     |      Create one or more indexes on this collection.
     |
     |        >>> from pymongo import IndexModel, ASCENDING, DESCENDING
     |        >>> index1 = IndexModel([("hello", DESCENDING),
     |        ...                      ("world", ASCENDING)], name="hello_world")
     |        >>> index2 = IndexModel([("goodbye", DESCENDING)])
     |        >>> db.test.create_indexes([index1, index2])
     |        ["hello_world", "goodbye_-1"]
     |
     |      :Parameters:
     |        - `indexes`: A list of :class:`~pymongo.operations.IndexModel`
     |          instances.
     |        - `session` (optional): a
     |          :class:`~pymongo.client_session.ClientSession`.
     |        - `comment` (optional): A user-provided comment to attach to this
     |          command.
     |        - `**kwargs` (optional): optional arguments to the createIndexes
     |          command (like maxTimeMS) can be passed as keyword arguments.
     |
     |
     |
     |
     |      .. note:: The :attr:`~pymongo.collection.Collection.write_concern` of
     |         this collection is automatically applied to this operation.
     |
     |      .. versionchanged:: 3.6
     |         Added ``session`` parameter. Added support for arbitrary keyword
     |         arguments.
     |
     |      .. versionchanged:: 3.4
     |         Apply this collection's write concern automatically to this operation
     |         when connected to MongoDB >= 3.4.
     |      .. versionadded:: 3.0
     |
     |      .. _createIndexes: https://mongodb.com/docs/manual/reference/command/createIndexes/
     |
     |  create_search_index(self, model: 'Union[Mapping[str, Any], SearchIndexModel]', session: 'Optional[ClientSession]' = None, comment: 'Any' = None, **kwargs: 'Any') -> 'str'
     |      Create a single search index for the current collection.
     |
     |      :Parameters:
     |        - `model`: The model for the new search index.
     |          It can be given as a :class:`~pymongo.operations.SearchIndexModel`
     |          instance or a dictionary with a model "definition"  and optional
     |          "name".
     |        - `session` (optional): a
     |          :class:`~pymongo.client_session.ClientSession`.
     |        - `comment` (optional): A user-provided comment to attach to this
     |          command.
     |        - `**kwargs` (optional): optional arguments to the createSearchIndexes
     |          command (like maxTimeMS) can be passed as keyword arguments.
     |
     |      :Returns:
     |        The name of the new search index.
     |
     |      .. note:: requires a MongoDB server version 7.0+ Atlas cluster.
     |
     |      .. versionadded:: 4.5
     |
     |  create_search_indexes(self, models: 'List[SearchIndexModel]', session: 'Optional[ClientSession]' = None, comment: 'Optional[Any]' = None, **kwargs: 'Any') -> 'List[str]'
     |      Create multiple search indexes for the current collection.
     |
     |      :Parameters:
     |        - `models`: A list of :class:`~pymongo.operations.SearchIndexModel` instances.
     |        - `session` (optional): a :class:`~pymongo.client_session.ClientSession`.
     |        - `comment` (optional): A user-provided comment to attach to this
     |          command.
     |        - `**kwargs` (optional): optional arguments to the createSearchIndexes
     |          command (like maxTimeMS) can be passed as keyword arguments.
     |
     |      :Returns:
     |          A list of the newly created search index names.
     |
     |      .. note:: requires a MongoDB server version 7.0+ Atlas cluster.
     |
     |      .. versionadded:: 4.5
     |
     |  delete_many(self, filter: 'Mapping[str, Any]', collation: 'Optional[_CollationIn]' = None, hint: 'Optional[_IndexKeyHint]' = None, session: 'Optional[ClientSession]' = None, let: 'Optional[Mapping[str, Any]]' = None, comment: 'Optional[Any]' = None) -> 'DeleteResult'
     |      Delete one or more documents matching the filter.
     |
     |        >>> db.test.count_documents({'x': 1})
     |        3
     |        >>> result = db.test.delete_many({'x': 1})
     |        >>> result.deleted_count
     |        3
     |        >>> db.test.count_documents({'x': 1})
     |        0
     |
     |      :Parameters:
     |        - `filter`: A query that matches the documents to delete.
     |        - `collation` (optional): An instance of
     |          :class:`~pymongo.collation.Collation`.
     |        - `hint` (optional): An index to use to support the query
     |          predicate specified either by its string name, or in the same
     |          format as passed to
     |          :meth:`~pymongo.collection.Collection.create_index` (e.g.
     |          ``[('field', ASCENDING)]``). This option is only supported on
     |          MongoDB 4.4 and above.
     |        - `session` (optional): a
     |          :class:`~pymongo.client_session.ClientSession`.
     |        - `let` (optional): Map of parameter names and values. Values must be
     |          constant or closed expressions that do not reference document
     |          fields. Parameters can then be accessed as variables in an
     |          aggregate expression context (e.g. "$$var").
     |        - `comment` (optional): A user-provided comment to attach to this
     |          command.
     |
     |      :Returns:
     |        - An instance of :class:`~pymongo.results.DeleteResult`.
     |
     |      .. versionchanged:: 4.1
     |         Added ``let`` parameter.
     |         Added ``comment`` parameter.
     |      .. versionchanged:: 3.11
     |         Added ``hint`` parameter.
     |      .. versionchanged:: 3.6
     |         Added ``session`` parameter.
     |      .. versionchanged:: 3.4
     |        Added the `collation` option.
     |      .. versionadded:: 3.0
     |
     |  delete_one(self, filter: 'Mapping[str, Any]', collation: 'Optional[_CollationIn]' = None, hint: 'Optional[_IndexKeyHint]' = None, session: 'Optional[ClientSession]' = None, let: 'Optional[Mapping[str, Any]]' = None, comment: 'Optional[Any]' = None) -> 'DeleteResult'
     |      Delete a single document matching the filter.
     |
     |        >>> db.test.count_documents({'x': 1})
     |        3
     |        >>> result = db.test.delete_one({'x': 1})
     |        >>> result.deleted_count
     |        1
     |        >>> db.test.count_documents({'x': 1})
     |        2
     |
     |      :Parameters:
     |        - `filter`: A query that matches the document to delete.
     |        - `collation` (optional): An instance of
     |          :class:`~pymongo.collation.Collation`.
     |        - `hint` (optional): An index to use to support the query
     |          predicate specified either by its string name, or in the same
     |          format as passed to
     |          :meth:`~pymongo.collection.Collection.create_index` (e.g.
     |          ``[('field', ASCENDING)]``). This option is only supported on
     |          MongoDB 4.4 and above.
     |        - `session` (optional): a
     |          :class:`~pymongo.client_session.ClientSession`.
     |        - `let` (optional): Map of parameter names and values. Values must be
     |          constant or closed expressions that do not reference document
     |          fields. Parameters can then be accessed as variables in an
     |          aggregate expression context (e.g. "$$var").
     |        - `comment` (optional): A user-provided comment to attach to this
     |          command.
     |
     |      :Returns:
     |        - An instance of :class:`~pymongo.results.DeleteResult`.
     |
     |      .. versionchanged:: 4.1
     |         Added ``let`` parameter.
     |         Added ``comment`` parameter.
     |      .. versionchanged:: 3.11
     |         Added ``hint`` parameter.
     |      .. versionchanged:: 3.6
     |         Added ``session`` parameter.
     |      .. versionchanged:: 3.4
     |        Added the `collation` option.
     |      .. versionadded:: 3.0
     |
     |  distinct(self, key: 'str', filter: 'Optional[Mapping[str, Any]]' = None, session: 'Optional[ClientSession]' = None, comment: 'Optional[Any]' = None, **kwargs: 'Any') -> 'List'
     |      Get a list of distinct values for `key` among all documents
     |      in this collection.
     |
     |      Raises :class:`TypeError` if `key` is not an instance of
     |      :class:`str`.
     |
     |      All optional distinct parameters should be passed as keyword arguments
     |      to this method. Valid options include:
     |
     |        - `maxTimeMS` (int): The maximum amount of time to allow the count
     |          command to run, in milliseconds.
     |        - `collation` (optional): An instance of
     |          :class:`~pymongo.collation.Collation`.
     |
     |      The :meth:`distinct` method obeys the :attr:`read_preference` of
     |      this :class:`Collection`.
     |
     |      :Parameters:
     |        - `key`: name of the field for which we want to get the distinct
     |          values
     |        - `filter` (optional): A query document that specifies the documents
     |          from which to retrieve the distinct values.
     |        - `session` (optional): a
     |          :class:`~pymongo.client_session.ClientSession`.
     |        - `comment` (optional): A user-provided comment to attach to this
     |          command.
     |        - `**kwargs` (optional): See list of options above.
     |
     |      .. versionchanged:: 3.6
     |         Added ``session`` parameter.
     |
     |      .. versionchanged:: 3.4
     |         Support the `collation` option.
     |
     |  drop(self, session: 'Optional[ClientSession]' = None, comment: 'Optional[Any]' = None, encrypted_fields: 'Optional[Mapping[str, Any]]' = None) -> 'None'
     |      Alias for :meth:`~pymongo.database.Database.drop_collection`.
     |
     |      :Parameters:
     |        - `session` (optional): a
     |          :class:`~pymongo.client_session.ClientSession`.
     |        - `comment` (optional): A user-provided comment to attach to this
     |          command.
     |        - `encrypted_fields`: **(BETA)** Document that describes the encrypted fields for
     |          Queryable Encryption.
     |
     |      The following two calls are equivalent:
     |
     |        >>> db.foo.drop()
     |        >>> db.drop_collection("foo")
     |
     |      .. versionchanged:: 4.2
     |         Added ``encrypted_fields`` parameter.
     |
     |      .. versionchanged:: 4.1
     |         Added ``comment`` parameter.
     |
     |      .. versionchanged:: 3.7
     |         :meth:`drop` now respects this :class:`Collection`'s :attr:`write_concern`.
     |
     |      .. versionchanged:: 3.6
     |         Added ``session`` parameter.
     |
     |  drop_index(self, index_or_name: '_IndexKeyHint', session: 'Optional[ClientSession]' = None, comment: 'Optional[Any]' = None, **kwargs: 'Any') -> 'None'
     |      Drops the specified index on this collection.
     |
     |      Can be used on non-existent collections or collections with no
     |      indexes.  Raises OperationFailure on an error (e.g. trying to
     |      drop an index that does not exist). `index_or_name`
     |      can be either an index name (as returned by `create_index`),
     |      or an index specifier (as passed to `create_index`). An index
     |      specifier should be a list of (key, direction) pairs. Raises
     |      TypeError if index is not an instance of (str, unicode, list).
     |
     |      .. warning::
     |
     |        if a custom name was used on index creation (by
     |        passing the `name` parameter to :meth:`create_index`) the index
     |        **must** be dropped by name.
     |
     |      :Parameters:
     |        - `index_or_name`: index (or name of index) to drop
     |        - `session` (optional): a
     |          :class:`~pymongo.client_session.ClientSession`.
     |        - `comment` (optional): A user-provided comment to attach to this
     |          command.
     |        - `**kwargs` (optional): optional arguments to the createIndexes
     |          command (like maxTimeMS) can be passed as keyword arguments.
     |
     |
     |
     |      .. note:: The :attr:`~pymongo.collection.Collection.write_concern` of
     |         this collection is automatically applied to this operation.
     |
     |
     |      .. versionchanged:: 3.6
     |         Added ``session`` parameter. Added support for arbitrary keyword
     |         arguments.
     |
     |      .. versionchanged:: 3.4
     |         Apply this collection's write concern automatically to this operation
     |         when connected to MongoDB >= 3.4.
     |
     |  drop_indexes(self, session: 'Optional[ClientSession]' = None, comment: 'Optional[Any]' = None, **kwargs: 'Any') -> 'None'
     |      Drops all indexes on this collection.
     |
     |      Can be used on non-existent collections or collections with no indexes.
     |      Raises OperationFailure on an error.
     |
     |      :Parameters:
     |        - `session` (optional): a
     |          :class:`~pymongo.client_session.ClientSession`.
     |        - `comment` (optional): A user-provided comment to attach to this
     |          command.
     |        - `**kwargs` (optional): optional arguments to the createIndexes
     |          command (like maxTimeMS) can be passed as keyword arguments.
     |
     |      .. note:: The :attr:`~pymongo.collection.Collection.write_concern` of
     |         this collection is automatically applied to this operation.
     |
     |      .. versionchanged:: 3.6
     |         Added ``session`` parameter. Added support for arbitrary keyword
     |         arguments.
     |
     |      .. versionchanged:: 3.4
     |         Apply this collection's write concern automatically to this operation
     |         when connected to MongoDB >= 3.4.
     |
     |  drop_search_index(self, name: 'str', session: 'Optional[ClientSession]' = None, comment: 'Optional[Any]' = None, **kwargs: 'Any') -> 'None'
     |      Delete a search index by index name.
     |
     |      :Parameters:
     |        - `name`: The name of the search index to be deleted.
     |        - `session` (optional): a
     |          :class:`~pymongo.client_session.ClientSession`.
     |        - `comment` (optional): A user-provided comment to attach to this
     |          command.
     |        - `**kwargs` (optional): optional arguments to the dropSearchIndexes
     |          command (like maxTimeMS) can be passed as keyword arguments.
     |
     |      .. note:: requires a MongoDB server version 7.0+ Atlas cluster.
     |
     |      .. versionadded:: 4.5
     |
     |  estimated_document_count(self, comment: 'Optional[Any]' = None, **kwargs: 'Any') -> 'int'
     |      Get an estimate of the number of documents in this collection using
     |      collection metadata.
     |
     |      The :meth:`estimated_document_count` method is **not** supported in a
     |      transaction.
     |
     |      All optional parameters should be passed as keyword arguments
     |      to this method. Valid options include:
     |
     |        - `maxTimeMS` (int): The maximum amount of time to allow this
     |          operation to run, in milliseconds.
     |
     |      :Parameters:
     |        - `comment` (optional): A user-provided comment to attach to this
     |          command.
     |        - `**kwargs` (optional): See list of options above.
     |
     |      .. versionchanged:: 4.2
     |         This method now always uses the `count`_ command. Due to an oversight in versions
     |         5.0.0-5.0.8 of MongoDB, the count command was not included in V1 of the
     |         :ref:`versioned-api-ref`. Users of the Stable API with estimated_document_count are
     |         recommended to upgrade their server version to 5.0.9+ or set
     |         :attr:`pymongo.server_api.ServerApi.strict` to ``False`` to avoid encountering errors.
     |
     |      .. versionadded:: 3.7
     |      .. _count: https://mongodb.com/docs/manual/reference/command/count/
     |
     |  find(self, *args: 'Any', **kwargs: 'Any') -> 'Cursor[_DocumentType]'
     |      Query the database.
     |
     |      The `filter` argument is a query document that all results
     |      must match. For example:
     |
     |      >>> db.test.find({"hello": "world"})
     |
     |      only matches documents that have a key "hello" with value
     |      "world".  Matches can have other keys *in addition* to
     |      "hello". The `projection` argument is used to specify a subset
     |      of fields that should be included in the result documents. By
     |      limiting results to a certain subset of fields you can cut
     |      down on network traffic and decoding time.
     |
     |      Raises :class:`TypeError` if any of the arguments are of
     |      improper type. Returns an instance of
     |      :class:`~pymongo.cursor.Cursor` corresponding to this query.
     |
     |      The :meth:`find` method obeys the :attr:`read_preference` of
     |      this :class:`Collection`.
     |
     |      :Parameters:
     |        - `filter` (optional): A query document that selects which documents
     |          to include in the result set. Can be an empty document to include
     |          all documents.
     |        - `projection` (optional): a list of field names that should be
     |          returned in the result set or a dict specifying the fields
     |          to include or exclude. If `projection` is a list "_id" will
     |          always be returned. Use a dict to exclude fields from
     |          the result (e.g. projection={'_id': False}).
     |        - `session` (optional): a
     |          :class:`~pymongo.client_session.ClientSession`.
     |        - `skip` (optional): the number of documents to omit (from
     |          the start of the result set) when returning the results
     |        - `limit` (optional): the maximum number of results to
     |          return. A limit of 0 (the default) is equivalent to setting no
     |          limit.
     |        - `no_cursor_timeout` (optional): if False (the default), any
     |          returned cursor is closed by the server after 10 minutes of
     |          inactivity. If set to True, the returned cursor will never
     |          time out on the server. Care should be taken to ensure that
     |          cursors with no_cursor_timeout turned on are properly closed.
     |        - `cursor_type` (optional): the type of cursor to return. The valid
     |          options are defined by :class:`~pymongo.cursor.CursorType`:
     |
     |          - :attr:`~pymongo.cursor.CursorType.NON_TAILABLE` - the result of
     |            this find call will return a standard cursor over the result set.
     |          - :attr:`~pymongo.cursor.CursorType.TAILABLE` - the result of this
     |            find call will be a tailable cursor - tailable cursors are only
     |            for use with capped collections. They are not closed when the
     |            last data is retrieved but are kept open and the cursor location
     |            marks the final document position. If more data is received
     |            iteration of the cursor will continue from the last document
     |            received. For details, see the `tailable cursor documentation
     |            <https://www.mongodb.com/docs/manual/core/tailable-cursors/>`_.
     |          - :attr:`~pymongo.cursor.CursorType.TAILABLE_AWAIT` - the result
     |            of this find call will be a tailable cursor with the await flag
     |            set. The server will wait for a few seconds after returning the
     |            full result set so that it can capture and return additional data
     |            added during the query.
     |          - :attr:`~pymongo.cursor.CursorType.EXHAUST` - the result of this
     |            find call will be an exhaust cursor. MongoDB will stream batched
     |            results to the client without waiting for the client to request
     |            each batch, reducing latency. See notes on compatibility below.
     |
     |        - `sort` (optional): a list of (key, direction) pairs
     |          specifying the sort order for this query. See
     |          :meth:`~pymongo.cursor.Cursor.sort` for details.
     |        - `allow_partial_results` (optional): if True, mongos will return
     |          partial results if some shards are down instead of returning an
     |          error.
     |        - `oplog_replay` (optional): **DEPRECATED** - if True, set the
     |          oplogReplay query flag. Default: False.
     |        - `batch_size` (optional): Limits the number of documents returned in
     |          a single batch.
     |        - `collation` (optional): An instance of
     |          :class:`~pymongo.collation.Collation`.
     |        - `return_key` (optional): If True, return only the index keys in
     |          each document.
     |        - `show_record_id` (optional): If True, adds a field ``$recordId`` in
     |          each document with the storage engine's internal record identifier.
     |        - `snapshot` (optional): **DEPRECATED** - If True, prevents the
     |          cursor from returning a document more than once because of an
     |          intervening write operation.
     |        - `hint` (optional): An index, in the same format as passed to
     |          :meth:`~pymongo.collection.Collection.create_index` (e.g.
     |          ``[('field', ASCENDING)]``). Pass this as an alternative to calling
     |          :meth:`~pymongo.cursor.Cursor.hint` on the cursor to tell Mongo the
     |          proper index to use for the query.
     |        - `max_time_ms` (optional): Specifies a time limit for a query
     |          operation. If the specified time is exceeded, the operation will be
     |          aborted and :exc:`~pymongo.errors.ExecutionTimeout` is raised. Pass
     |          this as an alternative to calling
     |          :meth:`~pymongo.cursor.Cursor.max_time_ms` on the cursor.
     |        - `max_scan` (optional): **DEPRECATED** - The maximum number of
     |          documents to scan. Pass this as an alternative to calling
     |          :meth:`~pymongo.cursor.Cursor.max_scan` on the cursor.
     |        - `min` (optional): A list of field, limit pairs specifying the
     |          inclusive lower bound for all keys of a specific index in order.
     |          Pass this as an alternative to calling
     |          :meth:`~pymongo.cursor.Cursor.min` on the cursor. ``hint`` must
     |          also be passed to ensure the query utilizes the correct index.
     |        - `max` (optional): A list of field, limit pairs specifying the
     |          exclusive upper bound for all keys of a specific index in order.
     |          Pass this as an alternative to calling
     |          :meth:`~pymongo.cursor.Cursor.max` on the cursor. ``hint`` must
     |          also be passed to ensure the query utilizes the correct index.
     |        - `comment` (optional): A string to attach to the query to help
     |          interpret and trace the operation in the server logs and in profile
     |          data. Pass this as an alternative to calling
     |          :meth:`~pymongo.cursor.Cursor.comment` on the cursor.
     |        - `allow_disk_use` (optional): if True, MongoDB may use temporary
     |          disk files to store data exceeding the system memory limit while
     |          processing a blocking sort operation. The option has no effect if
     |          MongoDB can satisfy the specified sort using an index, or if the
     |          blocking sort requires less memory than the 100 MiB limit. This
     |          option is only supported on MongoDB 4.4 and above.
     |
     |      .. note:: There are a number of caveats to using
     |        :attr:`~pymongo.cursor.CursorType.EXHAUST` as cursor_type:
     |
     |        - The `limit` option can not be used with an exhaust cursor.
     |
     |        - Exhaust cursors are not supported by mongos and can not be
     |          used with a sharded cluster.
     |
     |        - A :class:`~pymongo.cursor.Cursor` instance created with the
     |          :attr:`~pymongo.cursor.CursorType.EXHAUST` cursor_type requires an
     |          exclusive :class:`~socket.socket` connection to MongoDB. If the
     |          :class:`~pymongo.cursor.Cursor` is discarded without being
     |          completely iterated the underlying :class:`~socket.socket`
     |          connection will be closed and discarded without being returned to
     |          the connection pool.
     |
     |      .. versionchanged:: 4.0
     |         Removed the ``modifiers`` option.
     |         Empty projections (eg {} or []) are passed to the server as-is,
     |         rather than the previous behavior which substituted in a
     |         projection of ``{"_id": 1}``. This means that an empty projection
     |         will now return the entire document, not just the ``"_id"`` field.
     |
     |      .. versionchanged:: 3.11
     |         Added the ``allow_disk_use`` option.
     |         Deprecated the ``oplog_replay`` option. Support for this option is
     |         deprecated in MongoDB 4.4. The query engine now automatically
     |         optimizes queries against the oplog without requiring this
     |         option to be set.
     |
     |      .. versionchanged:: 3.7
     |         Deprecated the ``snapshot`` option, which is deprecated in MongoDB
     |         3.6 and removed in MongoDB 4.0.
     |         Deprecated the ``max_scan`` option. Support for this option is
     |         deprecated in MongoDB 4.0. Use ``max_time_ms`` instead to limit
     |         server-side execution time.
     |
     |      .. versionchanged:: 3.6
     |         Added ``session`` parameter.
     |
     |      .. versionchanged:: 3.5
     |         Added the options ``return_key``, ``show_record_id``, ``snapshot``,
     |         ``hint``, ``max_time_ms``, ``max_scan``, ``min``, ``max``, and
     |         ``comment``.
     |         Deprecated the ``modifiers`` option.
     |
     |      .. versionchanged:: 3.4
     |         Added support for the ``collation`` option.
     |
     |      .. versionchanged:: 3.0
     |         Changed the parameter names ``spec``, ``fields``, ``timeout``, and
     |         ``partial`` to ``filter``, ``projection``, ``no_cursor_timeout``,
     |         and ``allow_partial_results`` respectively.
     |         Added the ``cursor_type``, ``oplog_replay``, and ``modifiers``
     |         options.
     |         Removed the ``network_timeout``, ``read_preference``, ``tag_sets``,
     |         ``secondary_acceptable_latency_ms``, ``max_scan``, ``snapshot``,
     |         ``tailable``, ``await_data``, ``exhaust``, ``as_class``, and
     |         slave_okay parameters.
     |         Removed ``compile_re`` option: PyMongo now always
     |         represents BSON regular expressions as :class:`~bson.regex.Regex`
     |         objects. Use :meth:`~bson.regex.Regex.try_compile` to attempt to
     |         convert from a BSON regular expression to a Python regular
     |         expression object.
     |         Soft deprecated the ``manipulate`` option.
     |
     |      .. seealso:: The MongoDB documentation on `find <https://dochub.mongodb.org/core/find>`_.
     |
     |  find_one(self, filter: 'Optional[Any]' = None, *args: 'Any', **kwargs: 'Any') -> 'Optional[_DocumentType]'
     |      Get a single document from the database.
     |
     |      All arguments to :meth:`find` are also valid arguments for
     |      :meth:`find_one`, although any `limit` argument will be
     |      ignored. Returns a single document, or ``None`` if no matching
     |      document is found.
     |
     |      The :meth:`find_one` method obeys the :attr:`read_preference` of
     |      this :class:`Collection`.
     |
     |      :Parameters:
     |
     |        - `filter` (optional): a dictionary specifying
     |          the query to be performed OR any other type to be used as
     |          the value for a query for ``"_id"``.
     |
     |        - `*args` (optional): any additional positional arguments
     |          are the same as the arguments to :meth:`find`.
     |
     |        - `**kwargs` (optional): any additional keyword arguments
     |          are the same as the arguments to :meth:`find`.
     |
     |            >>> collection.find_one(max_time_ms=100)
     |
     |  find_one_and_delete(self, filter: 'Mapping[str, Any]', projection: 'Optional[Union[Mapping[str, Any], Iterable[str]]]' = None, sort: 'Optional[_IndexList]' = None, hint: 'Optional[_IndexKeyHint]' = None, session: 'Optional[ClientSession]' = None, let: 'Optional[Mapping[str, Any]]' = None, comment: 'Optional[Any]' = None, **kwargs: 'Any') -> '_DocumentType'
     |      Finds a single document and deletes it, returning the document.
     |
     |        >>> db.test.count_documents({'x': 1})
     |        2
     |        >>> db.test.find_one_and_delete({'x': 1})
     |        {'x': 1, '_id': ObjectId('54f4e12bfba5220aa4d6dee8')}
     |        >>> db.test.count_documents({'x': 1})
     |        1
     |
     |      If multiple documents match *filter*, a *sort* can be applied.
     |
     |        >>> for doc in db.test.find({'x': 1}):
     |        ...     print(doc)
     |        ...
     |        {'x': 1, '_id': 0}
     |        {'x': 1, '_id': 1}
     |        {'x': 1, '_id': 2}
     |        >>> db.test.find_one_and_delete(
     |        ...     {'x': 1}, sort=[('_id', pymongo.DESCENDING)])
     |        {'x': 1, '_id': 2}
     |
     |      The *projection* option can be used to limit the fields returned.
     |
     |        >>> db.test.find_one_and_delete({'x': 1}, projection={'_id': False})
     |        {'x': 1}
     |
     |      :Parameters:
     |        - `filter`: A query that matches the document to delete.
     |        - `projection` (optional): a list of field names that should be
     |          returned in the result document or a mapping specifying the fields
     |          to include or exclude. If `projection` is a list "_id" will
     |          always be returned. Use a mapping to exclude fields from
     |          the result (e.g. projection={'_id': False}).
     |        - `sort` (optional): a list of (key, direction) pairs
     |          specifying the sort order for the query. If multiple documents
     |          match the query, they are sorted and the first is deleted.
     |        - `hint` (optional): An index to use to support the query predicate
     |          specified either by its string name, or in the same format as
     |          passed to :meth:`~pymongo.collection.Collection.create_index`
     |          (e.g. ``[('field', ASCENDING)]``). This option is only supported
     |          on MongoDB 4.4 and above.
     |        - `session` (optional): a
     |          :class:`~pymongo.client_session.ClientSession`.
     |        - `let` (optional): Map of parameter names and values. Values must be
     |          constant or closed expressions that do not reference document
     |          fields. Parameters can then be accessed as variables in an
     |          aggregate expression context (e.g. "$$var").
     |        - `comment` (optional): A user-provided comment to attach to this
     |          command.
     |        - `**kwargs` (optional): additional command arguments can be passed
     |          as keyword arguments (for example maxTimeMS can be used with
     |          recent server versions).
     |
     |      .. versionchanged:: 4.1
     |         Added ``let`` parameter.
     |      .. versionchanged:: 3.11
     |         Added ``hint`` parameter.
     |      .. versionchanged:: 3.6
     |         Added ``session`` parameter.
     |      .. versionchanged:: 3.2
     |         Respects write concern.
     |
     |      .. warning:: Starting in PyMongo 3.2, this command uses the
     |         :class:`~pymongo.write_concern.WriteConcern` of this
     |         :class:`~pymongo.collection.Collection` when connected to MongoDB >=
     |         3.2. Note that using an elevated write concern with this command may
     |         be slower compared to using the default write concern.
     |
     |      .. versionchanged:: 3.4
     |         Added the `collation` option.
     |      .. versionadded:: 3.0
     |
     |  find_one_and_replace(self, filter: 'Mapping[str, Any]', replacement: 'Mapping[str, Any]', projection: 'Optional[Union[Mapping[str, Any], Iterable[str]]]' = None, sort: 'Optional[_IndexList]' = None, upsert: 'bool' = False, return_document: 'bool' = False, hint: 'Optional[_IndexKeyHint]' = None, session: 'Optional[ClientSession]' = None, let: 'Optional[Mapping[str, Any]]' = None, comment: 'Optional[Any]' = None, **kwargs: 'Any') -> '_DocumentType'
     |      Finds a single document and replaces it, returning either the
     |      original or the replaced document.
     |
     |      The :meth:`find_one_and_replace` method differs from
     |      :meth:`find_one_and_update` by replacing the document matched by
     |      *filter*, rather than modifying the existing document.
     |
     |        >>> for doc in db.test.find({}):
     |        ...     print(doc)
     |        ...
     |        {'x': 1, '_id': 0}
     |        {'x': 1, '_id': 1}
     |        {'x': 1, '_id': 2}
     |        >>> db.test.find_one_and_replace({'x': 1}, {'y': 1})
     |        {'x': 1, '_id': 0}
     |        >>> for doc in db.test.find({}):
     |        ...     print(doc)
     |        ...
     |        {'y': 1, '_id': 0}
     |        {'x': 1, '_id': 1}
     |        {'x': 1, '_id': 2}
     |
     |      :Parameters:
     |        - `filter`: A query that matches the document to replace.
     |        - `replacement`: The replacement document.
     |        - `projection` (optional): A list of field names that should be
     |          returned in the result document or a mapping specifying the fields
     |          to include or exclude. If `projection` is a list "_id" will
     |          always be returned. Use a mapping to exclude fields from
     |          the result (e.g. projection={'_id': False}).
     |        - `sort` (optional): a list of (key, direction) pairs
     |          specifying the sort order for the query. If multiple documents
     |          match the query, they are sorted and the first is replaced.
     |        - `upsert` (optional): When ``True``, inserts a new document if no
     |          document matches the query. Defaults to ``False``.
     |        - `return_document`: If
     |          :attr:`ReturnDocument.BEFORE` (the default),
     |          returns the original document before it was replaced, or ``None``
     |          if no document matches. If
     |          :attr:`ReturnDocument.AFTER`, returns the replaced
     |          or inserted document.
     |        - `hint` (optional): An index to use to support the query
     |          predicate specified either by its string name, or in the same
     |          format as passed to
     |          :meth:`~pymongo.collection.Collection.create_index` (e.g.
     |          ``[('field', ASCENDING)]``). This option is only supported on
     |          MongoDB 4.4 and above.
     |        - `session` (optional): a
     |          :class:`~pymongo.client_session.ClientSession`.
     |        - `let` (optional): Map of parameter names and values. Values must be
     |          constant or closed expressions that do not reference document
     |          fields. Parameters can then be accessed as variables in an
     |          aggregate expression context (e.g. "$$var").
     |        - `comment` (optional): A user-provided comment to attach to this
     |          command.
     |        - `**kwargs` (optional): additional command arguments can be passed
     |          as keyword arguments (for example maxTimeMS can be used with
     |          recent server versions).
     |
     |      .. versionchanged:: 4.1
     |         Added ``let`` parameter.
     |      .. versionchanged:: 3.11
     |         Added the ``hint`` option.
     |      .. versionchanged:: 3.6
     |         Added ``session`` parameter.
     |      .. versionchanged:: 3.4
     |         Added the ``collation`` option.
     |      .. versionchanged:: 3.2
     |         Respects write concern.
     |
     |      .. warning:: Starting in PyMongo 3.2, this command uses the
     |         :class:`~pymongo.write_concern.WriteConcern` of this
     |         :class:`~pymongo.collection.Collection` when connected to MongoDB >=
     |         3.2. Note that using an elevated write concern with this command may
     |         be slower compared to using the default write concern.
     |
     |      .. versionadded:: 3.0
     |
     |  find_one_and_update(self, filter: 'Mapping[str, Any]', update: 'Union[Mapping[str, Any], _Pipeline]', projection: 'Optional[Union[Mapping[str, Any], Iterable[str]]]' = None, sort: 'Optional[_IndexList]' = None, upsert: 'bool' = False, return_document: 'bool' = False, array_filters: 'Optional[Sequence[Mapping[str, Any]]]' = None, hint: 'Optional[_IndexKeyHint]' = None, session: 'Optional[ClientSession]' = None, let: 'Optional[Mapping[str, Any]]' = None, comment: 'Optional[Any]' = None, **kwargs: 'Any') -> '_DocumentType'
     |      Finds a single document and updates it, returning either the
     |      original or the updated document.
     |
     |        >>> db.test.find_one_and_update(
     |        ...    {'_id': 665}, {'$inc': {'count': 1}, '$set': {'done': True}})
     |        {'_id': 665, 'done': False, 'count': 25}}
     |
     |      Returns ``None`` if no document matches the filter.
     |
     |        >>> db.test.find_one_and_update(
     |        ...    {'_exists': False}, {'$inc': {'count': 1}})
     |
     |      When the filter matches, by default :meth:`find_one_and_update`
     |      returns the original version of the document before the update was
     |      applied. To return the updated (or inserted in the case of
     |      *upsert*) version of the document instead, use the *return_document*
     |      option.
     |
     |        >>> from pymongo import ReturnDocument
     |        >>> db.example.find_one_and_update(
     |        ...     {'_id': 'userid'},
     |        ...     {'$inc': {'seq': 1}},
     |        ...     return_document=ReturnDocument.AFTER)
     |        {'_id': 'userid', 'seq': 1}
     |
     |      You can limit the fields returned with the *projection* option.
     |
     |        >>> db.example.find_one_and_update(
     |        ...     {'_id': 'userid'},
     |        ...     {'$inc': {'seq': 1}},
     |        ...     projection={'seq': True, '_id': False},
     |        ...     return_document=ReturnDocument.AFTER)
     |        {'seq': 2}
     |
     |      The *upsert* option can be used to create the document if it doesn't
     |      already exist.
     |
     |        >>> db.example.delete_many({}).deleted_count
     |        1
     |        >>> db.example.find_one_and_update(
     |        ...     {'_id': 'userid'},
     |        ...     {'$inc': {'seq': 1}},
     |        ...     projection={'seq': True, '_id': False},
     |        ...     upsert=True,
     |        ...     return_document=ReturnDocument.AFTER)
     |        {'seq': 1}
     |
     |      If multiple documents match *filter*, a *sort* can be applied.
     |
     |        >>> for doc in db.test.find({'done': True}):
     |        ...     print(doc)
     |        ...
     |        {'_id': 665, 'done': True, 'result': {'count': 26}}
     |        {'_id': 701, 'done': True, 'result': {'count': 17}}
     |        >>> db.test.find_one_and_update(
     |        ...     {'done': True},
     |        ...     {'$set': {'final': True}},
     |        ...     sort=[('_id', pymongo.DESCENDING)])
     |        {'_id': 701, 'done': True, 'result': {'count': 17}}
     |
     |      :Parameters:
     |        - `filter`: A query that matches the document to update.
     |        - `update`: The update operations to apply.
     |        - `projection` (optional): A list of field names that should be
     |          returned in the result document or a mapping specifying the fields
     |          to include or exclude. If `projection` is a list "_id" will
     |          always be returned. Use a dict to exclude fields from
     |          the result (e.g. projection={'_id': False}).
     |        - `sort` (optional): a list of (key, direction) pairs
     |          specifying the sort order for the query. If multiple documents
     |          match the query, they are sorted and the first is updated.
     |        - `upsert` (optional): When ``True``, inserts a new document if no
     |          document matches the query. Defaults to ``False``.
     |        - `return_document`: If
     |          :attr:`ReturnDocument.BEFORE` (the default),
     |          returns the original document before it was updated. If
     |          :attr:`ReturnDocument.AFTER`, returns the updated
     |          or inserted document.
     |        - `array_filters` (optional): A list of filters specifying which
     |          array elements an update should apply.
     |        - `hint` (optional): An index to use to support the query
     |          predicate specified either by its string name, or in the same
     |          format as passed to
     |          :meth:`~pymongo.collection.Collection.create_index` (e.g.
     |          ``[('field', ASCENDING)]``). This option is only supported on
     |          MongoDB 4.4 and above.
     |        - `session` (optional): a
     |          :class:`~pymongo.client_session.ClientSession`.
     |        - `let` (optional): Map of parameter names and values. Values must be
     |          constant or closed expressions that do not reference document
     |          fields. Parameters can then be accessed as variables in an
     |          aggregate expression context (e.g. "$$var").
     |        - `comment` (optional): A user-provided comment to attach to this
     |          command.
     |        - `**kwargs` (optional): additional command arguments can be passed
     |          as keyword arguments (for example maxTimeMS can be used with
     |          recent server versions).
     |
     |      .. versionchanged:: 3.11
     |         Added the ``hint`` option.
     |      .. versionchanged:: 3.9
     |         Added the ability to accept a pipeline as the ``update``.
     |      .. versionchanged:: 3.6
     |         Added the ``array_filters`` and ``session`` options.
     |      .. versionchanged:: 3.4
     |         Added the ``collation`` option.
     |      .. versionchanged:: 3.2
     |         Respects write concern.
     |
     |      .. warning:: Starting in PyMongo 3.2, this command uses the
     |         :class:`~pymongo.write_concern.WriteConcern` of this
     |         :class:`~pymongo.collection.Collection` when connected to MongoDB >=
     |         3.2. Note that using an elevated write concern with this command may
     |         be slower compared to using the default write concern.
     |
     |      .. versionadded:: 3.0
     |
     |  find_raw_batches(self, *args: 'Any', **kwargs: 'Any') -> 'RawBatchCursor[_DocumentType]'
     |      Query the database and retrieve batches of raw BSON.
     |
     |      Similar to the :meth:`find` method but returns a
     |      :class:`~pymongo.cursor.RawBatchCursor`.
     |
     |      This example demonstrates how to work with raw batches, but in practice
     |      raw batches should be passed to an external library that can decode
     |      BSON into another data type, rather than used with PyMongo's
     |      :mod:`bson` module.
     |
     |        >>> import bson
     |        >>> cursor = db.test.find_raw_batches()
     |        >>> for batch in cursor:
     |        ...     print(bson.decode_all(batch))
     |
     |      .. note:: find_raw_batches does not support auto encryption.
     |
     |      .. versionchanged:: 3.12
     |         Instead of ignoring the user-specified read concern, this method
     |         now sends it to the server when connected to MongoDB 3.6+.
     |
     |         Added session support.
     |
     |      .. versionadded:: 3.6
     |
     |  index_information(self, session: 'Optional[ClientSession]' = None, comment: 'Optional[Any]' = None) -> 'MutableMapping[str, Any]'
     |      Get information on this collection's indexes.
     |
     |      Returns a dictionary where the keys are index names (as
     |      returned by create_index()) and the values are dictionaries
     |      containing information about each index. The dictionary is
     |      guaranteed to contain at least a single key, ``"key"`` which
     |      is a list of (key, direction) pairs specifying the index (as
     |      passed to create_index()). It will also contain any other
     |      metadata about the indexes, except for the ``"ns"`` and
     |      ``"name"`` keys, which are cleaned. Example output might look
     |      like this:
     |
     |      >>> db.test.create_index("x", unique=True)
     |      'x_1'
     |      >>> db.test.index_information()
     |      {'_id_': {'key': [('_id', 1)]},
     |       'x_1': {'unique': True, 'key': [('x', 1)]}}
     |
     |      :Parameters:
     |        - `session` (optional): a
     |          :class:`~pymongo.client_session.ClientSession`.
     |        - `comment` (optional): A user-provided comment to attach to this
     |          command.
     |
     |      .. versionchanged:: 4.1
     |         Added ``comment`` parameter.
     |
     |      .. versionchanged:: 3.6
     |         Added ``session`` parameter.
     |
     |  insert_many(self, documents: 'Iterable[Union[_DocumentType, RawBSONDocument]]', ordered: 'bool' = True, bypass_document_validation: 'bool' = False, session: 'Optional[ClientSession]' = None, comment: 'Optional[Any]' = None) -> 'InsertManyResult'
     |      Insert an iterable of documents.
     |
     |        >>> db.test.count_documents({})
     |        0
     |        >>> result = db.test.insert_many([{'x': i} for i in range(2)])
     |        >>> result.inserted_ids
     |        [ObjectId('54f113fffba522406c9cc20e'), ObjectId('54f113fffba522406c9cc20f')]
     |        >>> db.test.count_documents({})
     |        2
     |
     |      :Parameters:
     |        - `documents`: A iterable of documents to insert.
     |        - `ordered` (optional): If ``True`` (the default) documents will be
     |          inserted on the server serially, in the order provided. If an error
     |          occurs all remaining inserts are aborted. If ``False``, documents
     |          will be inserted on the server in arbitrary order, possibly in
     |          parallel, and all document inserts will be attempted.
     |        - `bypass_document_validation`: (optional) If ``True``, allows the
     |          write to opt-out of document level validation. Default is
     |          ``False``.
     |        - `session` (optional): a
     |          :class:`~pymongo.client_session.ClientSession`.
     |        - `comment` (optional): A user-provided comment to attach to this
     |          command.
     |
     |      :Returns:
     |        An instance of :class:`~pymongo.results.InsertManyResult`.
     |
     |      .. seealso:: :ref:`writes-and-ids`
     |
     |      .. note:: `bypass_document_validation` requires server version
     |        **>= 3.2**
     |
     |      .. versionchanged:: 4.1
     |         Added ``comment`` parameter.
     |
     |      .. versionchanged:: 3.6
     |         Added ``session`` parameter.
     |
     |      .. versionchanged:: 3.2
     |        Added bypass_document_validation support
     |
     |      .. versionadded:: 3.0
     |
     |  insert_one(self, document: 'Union[_DocumentType, RawBSONDocument]', bypass_document_validation: 'bool' = False, session: 'Optional[ClientSession]' = None, comment: 'Optional[Any]' = None) -> 'InsertOneResult'
     |      Insert a single document.
     |
     |        >>> db.test.count_documents({'x': 1})
     |        0
     |        >>> result = db.test.insert_one({'x': 1})
     |        >>> result.inserted_id
     |        ObjectId('54f112defba522406c9cc208')
     |        >>> db.test.find_one({'x': 1})
     |        {'x': 1, '_id': ObjectId('54f112defba522406c9cc208')}
     |
     |      :Parameters:
     |        - `document`: The document to insert. Must be a mutable mapping
     |          type. If the document does not have an _id field one will be
     |          added automatically.
     |        - `bypass_document_validation`: (optional) If ``True``, allows the
     |          write to opt-out of document level validation. Default is
     |          ``False``.
     |        - `session` (optional): a
     |          :class:`~pymongo.client_session.ClientSession`.
     |        - `comment` (optional): A user-provided comment to attach to this
     |          command.
     |
     |      :Returns:
     |        - An instance of :class:`~pymongo.results.InsertOneResult`.
     |
     |      .. seealso:: :ref:`writes-and-ids`
     |
     |      .. note:: `bypass_document_validation` requires server version
     |        **>= 3.2**
     |
     |      .. versionchanged:: 4.1
     |         Added ``comment`` parameter.
     |
     |      .. versionchanged:: 3.6
     |         Added ``session`` parameter.
     |
     |      .. versionchanged:: 3.2
     |        Added bypass_document_validation support
     |
     |      .. versionadded:: 3.0
     |
     |  list_indexes(self, session: 'Optional[ClientSession]' = None, comment: 'Optional[Any]' = None) -> 'CommandCursor[MutableMapping[str, Any]]'
     |      Get a cursor over the index documents for this collection.
     |
     |        >>> for index in db.test.list_indexes():
     |        ...     print(index)
     |        ...
     |        SON([('v', 2), ('key', SON([('_id', 1)])), ('name', '_id_')])
     |
     |      :Parameters:
     |        - `session` (optional): a
     |          :class:`~pymongo.client_session.ClientSession`.
     |        - `comment` (optional): A user-provided comment to attach to this
     |          command.
     |
     |      :Returns:
     |        An instance of :class:`~pymongo.command_cursor.CommandCursor`.
     |
     |      .. versionchanged:: 4.1
     |         Added ``comment`` parameter.
     |
     |      .. versionchanged:: 3.6
     |         Added ``session`` parameter.
     |
     |      .. versionadded:: 3.0
     |
     |  list_search_indexes(self, name: 'Optional[str]' = None, session: 'Optional[ClientSession]' = None, comment: 'Optional[Any]' = None, **kwargs: 'Any') -> 'CommandCursor[Mapping[str, Any]]'
     |      Return a cursor over search indexes for the current collection.
     |
     |      :Parameters:
     |        - `name` (optional): If given, the name of the index to search
     |          for.  Only indexes with matching index names will be returned.
     |          If not given, all search indexes for the current collection
     |          will be returned.
     |        - `session` (optional): a :class:`~pymongo.client_session.ClientSession`.
     |        - `comment` (optional): A user-provided comment to attach to this
     |          command.
     |
     |      :Returns:
     |        A :class:`~pymongo.command_cursor.CommandCursor` over the result
     |        set.
     |
     |      .. note:: requires a MongoDB server version 7.0+ Atlas cluster.
     |
     |      .. versionadded:: 4.5
     |
     |  next = __next__(self) -> 'NoReturn'
     |
     |  options(self, session: 'Optional[ClientSession]' = None, comment: 'Optional[Any]' = None) -> 'MutableMapping[str, Any]'
     |      Get the options set on this collection.
     |
     |      Returns a dictionary of options and their values - see
     |      :meth:`~pymongo.database.Database.create_collection` for more
     |      information on the possible options. Returns an empty
     |      dictionary if the collection has not been created yet.
     |
     |      :Parameters:
     |        - `session` (optional): a
     |          :class:`~pymongo.client_session.ClientSession`.
     |        - `comment` (optional): A user-provided comment to attach to this
     |          command.
     |
     |      .. versionchanged:: 3.6
     |         Added ``session`` parameter.
     |
     |  rename(self, new_name: 'str', session: 'Optional[ClientSession]' = None, comment: 'Optional[Any]' = None, **kwargs: 'Any') -> 'MutableMapping[str, Any]'
     |      Rename this collection.
     |
     |      If operating in auth mode, client must be authorized as an
     |      admin to perform this operation. Raises :class:`TypeError` if
     |      `new_name` is not an instance of :class:`str`.
     |      Raises :class:`~pymongo.errors.InvalidName`
     |      if `new_name` is not a valid collection name.
     |
     |      :Parameters:
     |        - `new_name`: new name for this collection
     |        - `session` (optional): a
     |          :class:`~pymongo.client_session.ClientSession`.
     |        - `comment` (optional): A user-provided comment to attach to this
     |          command.
     |        - `**kwargs` (optional): additional arguments to the rename command
     |          may be passed as keyword arguments to this helper method
     |          (i.e. ``dropTarget=True``)
     |
     |      .. note:: The :attr:`~pymongo.collection.Collection.write_concern` of
     |         this collection is automatically applied to this operation.
     |
     |      .. versionchanged:: 3.6
     |         Added ``session`` parameter.
     |
     |      .. versionchanged:: 3.4
     |         Apply this collection's write concern automatically to this operation
     |         when connected to MongoDB >= 3.4.
     |
     |  replace_one(self, filter: 'Mapping[str, Any]', replacement: 'Mapping[str, Any]', upsert: 'bool' = False, bypass_document_validation: 'bool' = False, collation: 'Optional[_CollationIn]' = None, hint: 'Optional[_IndexKeyHint]' = None, session: 'Optional[ClientSession]' = None, let: 'Optional[Mapping[str, Any]]' = None, comment: 'Optional[Any]' = None) -> 'UpdateResult'
     |      Replace a single document matching the filter.
     |
     |        >>> for doc in db.test.find({}):
     |        ...     print(doc)
     |        ...
     |        {'x': 1, '_id': ObjectId('54f4c5befba5220aa4d6dee7')}
     |        >>> result = db.test.replace_one({'x': 1}, {'y': 1})
     |        >>> result.matched_count
     |        1
     |        >>> result.modified_count
     |        1
     |        >>> for doc in db.test.find({}):
     |        ...     print(doc)
     |        ...
     |        {'y': 1, '_id': ObjectId('54f4c5befba5220aa4d6dee7')}
     |
     |      The *upsert* option can be used to insert a new document if a matching
     |      document does not exist.
     |
     |        >>> result = db.test.replace_one({'x': 1}, {'x': 1}, True)
     |        >>> result.matched_count
     |        0
     |        >>> result.modified_count
     |        0
     |        >>> result.upserted_id
     |        ObjectId('54f11e5c8891e756a6e1abd4')
     |        >>> db.test.find_one({'x': 1})
     |        {'x': 1, '_id': ObjectId('54f11e5c8891e756a6e1abd4')}
     |
     |      :Parameters:
     |        - `filter`: A query that matches the document to replace.
     |        - `replacement`: The new document.
     |        - `upsert` (optional): If ``True``, perform an insert if no documents
     |          match the filter.
     |        - `bypass_document_validation`: (optional) If ``True``, allows the
     |          write to opt-out of document level validation. Default is
     |          ``False``.
     |        - `collation` (optional): An instance of
     |          :class:`~pymongo.collation.Collation`.
     |        - `hint` (optional): An index to use to support the query
     |          predicate specified either by its string name, or in the same
     |          format as passed to
     |          :meth:`~pymongo.collection.Collection.create_index` (e.g.
     |          ``[('field', ASCENDING)]``). This option is only supported on
     |          MongoDB 4.2 and above.
     |        - `session` (optional): a
     |          :class:`~pymongo.client_session.ClientSession`.
     |        - `let` (optional): Map of parameter names and values. Values must be
     |          constant or closed expressions that do not reference document
     |          fields. Parameters can then be accessed as variables in an
     |          aggregate expression context (e.g. "$$var").
     |        - `comment` (optional): A user-provided comment to attach to this
     |          command.
     |      :Returns:
     |        - An instance of :class:`~pymongo.results.UpdateResult`.
     |
     |      .. versionchanged:: 4.1
     |         Added ``let`` parameter.
     |         Added ``comment`` parameter.
     |      .. versionchanged:: 3.11
     |         Added ``hint`` parameter.
     |      .. versionchanged:: 3.6
     |         Added ``session`` parameter.
     |      .. versionchanged:: 3.4
     |        Added the `collation` option.
     |      .. versionchanged:: 3.2
     |        Added bypass_document_validation support.
     |
     |      .. versionadded:: 3.0
     |
     |  update_many(self, filter: 'Mapping[str, Any]', update: 'Union[Mapping[str, Any], _Pipeline]', upsert: 'bool' = False, array_filters: 'Optional[Sequence[Mapping[str, Any]]]' = None, bypass_document_validation: 'Optional[bool]' = None, collation: 'Optional[_CollationIn]' = None, hint: 'Optional[_IndexKeyHint]' = None, session: 'Optional[ClientSession]' = None, let: 'Optional[Mapping[str, Any]]' = None, comment: 'Optional[Any]' = None) -> 'UpdateResult'
     |      Update one or more documents that match the filter.
     |
     |        >>> for doc in db.test.find():
     |        ...     print(doc)
     |        ...
     |        {'x': 1, '_id': 0}
     |        {'x': 1, '_id': 1}
     |        {'x': 1, '_id': 2}
     |        >>> result = db.test.update_many({'x': 1}, {'$inc': {'x': 3}})
     |        >>> result.matched_count
     |        3
     |        >>> result.modified_count
     |        3
     |        >>> for doc in db.test.find():
     |        ...     print(doc)
     |        ...
     |        {'x': 4, '_id': 0}
     |        {'x': 4, '_id': 1}
     |        {'x': 4, '_id': 2}
     |
     |      :Parameters:
     |        - `filter`: A query that matches the documents to update.
     |        - `update`: The modifications to apply.
     |        - `upsert` (optional): If ``True``, perform an insert if no documents
     |          match the filter.
     |        - `bypass_document_validation` (optional): If ``True``, allows the
     |          write to opt-out of document level validation. Default is
     |          ``False``.
     |        - `collation` (optional): An instance of
     |          :class:`~pymongo.collation.Collation`.
     |        - `array_filters` (optional): A list of filters specifying which
     |          array elements an update should apply.
     |        - `hint` (optional): An index to use to support the query
     |          predicate specified either by its string name, or in the same
     |          format as passed to
     |          :meth:`~pymongo.collection.Collection.create_index` (e.g.
     |          ``[('field', ASCENDING)]``). This option is only supported on
     |          MongoDB 4.2 and above.
     |        - `session` (optional): a
     |          :class:`~pymongo.client_session.ClientSession`.
     |        - `let` (optional): Map of parameter names and values. Values must be
     |          constant or closed expressions that do not reference document
     |          fields. Parameters can then be accessed as variables in an
     |          aggregate expression context (e.g. "$$var").
     |        - `comment` (optional): A user-provided comment to attach to this
     |          command.
     |
     |      :Returns:
     |        - An instance of :class:`~pymongo.results.UpdateResult`.
     |
     |      .. versionchanged:: 4.1
     |         Added ``let`` parameter.
     |         Added ``comment`` parameter.
     |      .. versionchanged:: 3.11
     |         Added ``hint`` parameter.
     |      .. versionchanged:: 3.9
     |         Added the ability to accept a pipeline as the `update`.
     |      .. versionchanged:: 3.6
     |         Added ``array_filters`` and ``session`` parameters.
     |      .. versionchanged:: 3.4
     |        Added the `collation` option.
     |      .. versionchanged:: 3.2
     |        Added bypass_document_validation support.
     |
     |      .. versionadded:: 3.0
     |
     |  update_one(self, filter: 'Mapping[str, Any]', update: 'Union[Mapping[str, Any], _Pipeline]', upsert: 'bool' = False, bypass_document_validation: 'bool' = False, collation: 'Optional[_CollationIn]' = None, array_filters: 'Optional[Sequence[Mapping[str, Any]]]' = None, hint: 'Optional[_IndexKeyHint]' = None, session: 'Optional[ClientSession]' = None, let: 'Optional[Mapping[str, Any]]' = None, comment: 'Optional[Any]' = None) -> 'UpdateResult'
     |      Update a single document matching the filter.
     |
     |        >>> for doc in db.test.find():
     |        ...     print(doc)
     |        ...
     |        {'x': 1, '_id': 0}
     |        {'x': 1, '_id': 1}
     |        {'x': 1, '_id': 2}
     |        >>> result = db.test.update_one({'x': 1}, {'$inc': {'x': 3}})
     |        >>> result.matched_count
     |        1
     |        >>> result.modified_count
     |        1
     |        >>> for doc in db.test.find():
     |        ...     print(doc)
     |        ...
     |        {'x': 4, '_id': 0}
     |        {'x': 1, '_id': 1}
     |        {'x': 1, '_id': 2}
     |
     |      If ``upsert=True`` and no documents match the filter, create a
     |      new document based on the filter criteria and update modifications.
     |
     |        >>> result = db.test.update_one({'x': -10}, {'$inc': {'x': 3}}, upsert=True)
     |        >>> result.matched_count
     |        0
     |        >>> result.modified_count
     |        0
     |        >>> result.upserted_id
     |        ObjectId('626a678eeaa80587d4bb3fb7')
     |        >>> db.test.find_one(result.upserted_id)
     |        {'_id': ObjectId('626a678eeaa80587d4bb3fb7'), 'x': -7}
     |
     |      :Parameters:
     |        - `filter`: A query that matches the document to update.
     |        - `update`: The modifications to apply.
     |        - `upsert` (optional): If ``True``, perform an insert if no documents
     |          match the filter.
     |        - `bypass_document_validation`: (optional) If ``True``, allows the
     |          write to opt-out of document level validation. Default is
     |          ``False``.
     |        - `collation` (optional): An instance of
     |          :class:`~pymongo.collation.Collation`.
     |        - `array_filters` (optional): A list of filters specifying which
     |          array elements an update should apply.
     |        - `hint` (optional): An index to use to support the query
     |          predicate specified either by its string name, or in the same
     |          format as passed to
     |          :meth:`~pymongo.collection.Collection.create_index` (e.g.
     |          ``[('field', ASCENDING)]``). This option is only supported on
     |          MongoDB 4.2 and above.
     |        - `session` (optional): a
     |          :class:`~pymongo.client_session.ClientSession`.
     |        - `let` (optional): Map of parameter names and values. Values must be
     |          constant or closed expressions that do not reference document
     |          fields. Parameters can then be accessed as variables in an
     |          aggregate expression context (e.g. "$$var").
     |        - `comment` (optional): A user-provided comment to attach to this
     |          command.
     |
     |      :Returns:
     |        - An instance of :class:`~pymongo.results.UpdateResult`.
     |
     |      .. versionchanged:: 4.1
     |         Added ``let`` parameter.
     |         Added ``comment`` parameter.
     |      .. versionchanged:: 3.11
     |         Added ``hint`` parameter.
     |      .. versionchanged:: 3.9
     |         Added the ability to accept a pipeline as the ``update``.
     |      .. versionchanged:: 3.6
     |         Added the ``array_filters`` and ``session`` parameters.
     |      .. versionchanged:: 3.4
     |        Added the ``collation`` option.
     |      .. versionchanged:: 3.2
     |        Added ``bypass_document_validation`` support.
     |
     |      .. versionadded:: 3.0
     |
     |  update_search_index(self, name: 'str', definition: 'Mapping[str, Any]', session: 'Optional[ClientSession]' = None, comment: 'Optional[Any]' = None, **kwargs: 'Any') -> 'None'
     |      Update a search index by replacing the existing index definition with the provided definition.
     |
     |      :Parameters:
     |        - `name`: The name of the search index to be updated.
     |        - `definition`: The new search index definition.
     |        - `session` (optional): a
     |          :class:`~pymongo.client_session.ClientSession`.
     |        - `comment` (optional): A user-provided comment to attach to this
     |          command.
     |        - `**kwargs` (optional): optional arguments to the updateSearchIndexes
     |          command (like maxTimeMS) can be passed as keyword arguments.
     |
     |      .. note:: requires a MongoDB server version 7.0+ Atlas cluster.
     |
     |      .. versionadded:: 4.5
     |
     |  watch(self, pipeline: 'Optional[_Pipeline]' = None, full_document: 'Optional[str]' = None, resume_after: 'Optional[Mapping[str, Any]]' = None, max_await_time_ms: 'Optional[int]' = None, batch_size: 'Optional[int]' = None, collation: 'Optional[_CollationIn]' = None, start_at_operation_time: 'Optional[Timestamp]' = None, session: 'Optional[ClientSession]' = None, start_after: 'Optional[Mapping[str, Any]]' = None, comment: 'Optional[Any]' = None, full_document_before_change: 'Optional[str]' = None, show_expanded_events: 'Optional[bool]' = None) -> 'CollectionChangeStream[_DocumentType]'
     |      Watch changes on this collection.
     |
     |      Performs an aggregation with an implicit initial ``$changeStream``
     |      stage and returns a
     |      :class:`~pymongo.change_stream.CollectionChangeStream` cursor which
     |      iterates over changes on this collection.
     |
     |      .. code-block:: python
     |
     |         with db.collection.watch() as stream:
     |             for change in stream:
     |                 print(change)
     |
     |      The :class:`~pymongo.change_stream.CollectionChangeStream` iterable
     |      blocks until the next change document is returned or an error is
     |      raised. If the
     |      :meth:`~pymongo.change_stream.CollectionChangeStream.next` method
     |      encounters a network error when retrieving a batch from the server,
     |      it will automatically attempt to recreate the cursor such that no
     |      change events are missed. Any error encountered during the resume
     |      attempt indicates there may be an outage and will be raised.
     |
     |      .. code-block:: python
     |
     |          try:
     |              with db.collection.watch([{"$match": {"operationType": "insert"}}]) as stream:
     |                  for insert_change in stream:
     |                      print(insert_change)
     |          except pymongo.errors.PyMongoError:
     |              # The ChangeStream encountered an unrecoverable error or the
     |              # resume attempt failed to recreate the cursor.
     |              logging.error("...")
     |
     |      For a precise description of the resume process see the
     |      `change streams specification`_.
     |
     |      .. note:: Using this helper method is preferred to directly calling
     |          :meth:`~pymongo.collection.Collection.aggregate` with a
     |          ``$changeStream`` stage, for the purpose of supporting
     |          resumability.
     |
     |      .. warning:: This Collection's :attr:`read_concern` must be
     |          ``ReadConcern("majority")`` in order to use the ``$changeStream``
     |          stage.
     |
     |      :Parameters:
     |        - `pipeline` (optional): A list of aggregation pipeline stages to
     |          append to an initial ``$changeStream`` stage. Not all
     |          pipeline stages are valid after a ``$changeStream`` stage, see the
     |          MongoDB documentation on change streams for the supported stages.
     |        - `full_document` (optional): The fullDocument to pass as an option
     |          to the ``$changeStream`` stage. Allowed values: 'updateLookup',
     |          'whenAvailable', 'required'. When set to 'updateLookup', the
     |          change notification for partial updates will include both a delta
     |          describing the changes to the document, as well as a copy of the
     |          entire document that was changed from some time after the change
     |          occurred.
     |        - `full_document_before_change`: Allowed values: 'whenAvailable'
     |          and 'required'. Change events may now result in a
     |          'fullDocumentBeforeChange' response field.
     |        - `resume_after` (optional): A resume token. If provided, the
     |          change stream will start returning changes that occur directly
     |          after the operation specified in the resume token. A resume token
     |          is the _id value of a change document.
     |        - `max_await_time_ms` (optional): The maximum time in milliseconds
     |          for the server to wait for changes before responding to a getMore
     |          operation.
     |        - `batch_size` (optional): The maximum number of documents to return
     |          per batch.
     |        - `collation` (optional): The :class:`~pymongo.collation.Collation`
     |          to use for the aggregation.
     |        - `start_at_operation_time` (optional): If provided, the resulting
     |          change stream will only return changes that occurred at or after
     |          the specified :class:`~bson.timestamp.Timestamp`. Requires
     |          MongoDB >= 4.0.
     |        - `session` (optional): a
     |          :class:`~pymongo.client_session.ClientSession`.
     |        - `start_after` (optional): The same as `resume_after` except that
     |          `start_after` can resume notifications after an invalidate event.
     |          This option and `resume_after` are mutually exclusive.
     |        - `comment` (optional): A user-provided comment to attach to this
     |          command.
     |        - `show_expanded_events` (optional): Include expanded events such as DDL events like `dropIndexes`.
     |
     |      :Returns:
     |        A :class:`~pymongo.change_stream.CollectionChangeStream` cursor.
     |
     |      .. versionchanged:: 4.3
     |         Added `show_expanded_events` parameter.
     |
     |      .. versionchanged:: 4.2
     |         Added ``full_document_before_change`` parameter.
     |
     |      .. versionchanged:: 4.1
     |         Added ``comment`` parameter.
     |
     |      .. versionchanged:: 3.9
     |         Added the ``start_after`` parameter.
     |
     |      .. versionchanged:: 3.7
     |         Added the ``start_at_operation_time`` parameter.
     |
     |      .. versionadded:: 3.6
     |
     |      .. seealso:: The MongoDB documentation on `changeStreams <https://mongodb.com/docs/manual/changeStreams/>`_.
     |
     |      .. _change streams specification:
     |          https://github.com/mongodb/specifications/blob/master/source/change-streams/change-streams.rst
     |
     |  with_options(self, codec_options: 'Optional[bson.CodecOptions[_DocumentTypeArg]]' = None, read_preference: 'Optional[_ServerMode]' = None, write_concern: 'Optional[WriteConcern]' = None, read_concern: 'Optional[ReadConcern]' = None) -> 'Collection[_DocumentType]'
     |      Get a clone of this collection changing the specified settings.
     |
     |        >>> coll1.read_preference
     |        Primary()
     |        >>> from pymongo import ReadPreference
     |        >>> coll2 = coll1.with_options(read_preference=ReadPreference.SECONDARY)
     |        >>> coll1.read_preference
     |        Primary()
     |        >>> coll2.read_preference
     |        Secondary(tag_sets=None)
     |
     |      :Parameters:
     |        - `codec_options` (optional): An instance of
     |          :class:`~bson.codec_options.CodecOptions`. If ``None`` (the
     |          default) the :attr:`codec_options` of this :class:`Collection`
     |          is used.
     |        - `read_preference` (optional): The read preference to use. If
     |          ``None`` (the default) the :attr:`read_preference` of this
     |          :class:`Collection` is used. See :mod:`~pymongo.read_preferences`
     |          for options.
     |        - `write_concern` (optional): An instance of
     |          :class:`~pymongo.write_concern.WriteConcern`. If ``None`` (the
     |          default) the :attr:`write_concern` of this :class:`Collection`
     |          is used.
     |        - `read_concern` (optional): An instance of
     |          :class:`~pymongo.read_concern.ReadConcern`. If ``None`` (the
     |          default) the :attr:`read_concern` of this :class:`Collection`
     |          is used.
     |
     |  ----------------------------------------------------------------------
     |  Readonly properties defined here:
     |
     |  database
     |      The :class:`~pymongo.database.Database` that this
     |      :class:`Collection` is a part of.
     |
     |  full_name
     |      The full name of this :class:`Collection`.
     |
     |      The full name is of the form `database_name.collection_name`.
     |
     |  name
     |      The name of this :class:`Collection`.
     |
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |
     |  __annotations__ = {}
     |
     |  __iter__ = None
     |
     |  __orig_bases__ = (<class 'pymongo.common.BaseObject'>, typing.Generic[...
     |
     |  __parameters__ = (~_DocumentType,)
     |
     |  ----------------------------------------------------------------------
     |  Readonly properties inherited from pymongo.common.BaseObject:
     |
     |  codec_options
     |      Read only access to the :class:`~bson.codec_options.CodecOptions`
     |      of this instance.
     |
     |  read_concern
     |      Read only access to the :class:`~pymongo.read_concern.ReadConcern`
     |      of this instance.
     |
     |      .. versionadded:: 3.2
     |
     |  read_preference
     |      Read only access to the read preference of this instance.
     |
     |      .. versionchanged:: 3.0
     |        The :attr:`read_preference` attribute is now read only.
     |
     |  write_concern
     |      Read only access to the :class:`~pymongo.write_concern.WriteConcern`
     |      of this instance.
     |
     |      .. versionchanged:: 3.0
     |        The :attr:`write_concern` attribute is now read only.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from pymongo.common.BaseObject:
     |
     |  __dict__
     |      dictionary for instance variables (if defined)
     |
     |  __weakref__
     |      list of weak references to the object (if defined)
     |
     |  ----------------------------------------------------------------------
     |  Class methods inherited from typing.Generic:
     |
     |  __class_getitem__(...) from builtins.type
     |      Parameterizes a generic class.
     |
     |      At least, parameterizing a generic class is the *main* thing this
     |      method does. For example, for some generic class `Foo`, this is called
     |      when we do `Foo[int]` - there, with `cls=Foo` and `params=int`.
     |
     |      However, note that this method is also called when defining generic
     |      classes in the first place with `class Foo[T]: ...`.
     |
     |  __init_subclass__(...) from builtins.type
     |      Function to initialize subclasses.
    


## Insert One Document

- let's insert one document into our recipe collection
- document is equivalent to row/record in SQL databases


```python
elotes = {"name": "elotes", "ingredients": ["corn", "mayonnaise", "cotija cheese", "sour cream", "lime"], "prep_time": 35}
```


```python
# if the insert_one API runs successfully, double check on Atlas to see the recipe
try:
    my_collection.insert_one(elotes)
except OperationFailure as ex:
    print(ex)
    raise ex
    
```

## Insert Many Documents

- let's create a list of python dictionaries as documents


```python
recipes = []
```


```python
loco = { "name": "loco moco", "ingredients": ["ground beef", "butter", "onion", "egg", "bread bun", "mushrooms"], "prep_time": 54 }
```


```python
recipes.append(loco)
```


```python
recipes
```




    [{'name': 'loco moco',
      'ingredients': ['ground beef',
       'butter',
       'onion',
       'egg',
       'bread bun',
       'mushrooms'],
      'prep_time': 54}]




```python
patatas =  { "name": "patatas bravas", "ingredients": ["potato", "tomato", "olive oil", "onion", "garlic", "paprika"], "prep_time": 80 }
```


```python
recipes.append(patatas)
```


```python
fried_rice = { "name": "fried rice", "ingredients": ["rice", "soy sauce", "egg", "onion", "pea", "carrot", "sesame oil"], "prep_time": 40 }
```


```python
recipes.append(fried_rice)
```


```python
recipes
```




    [{'name': 'loco moco',
      'ingredients': ['ground beef',
       'butter',
       'onion',
       'egg',
       'bread bun',
       'mushrooms'],
      'prep_time': 54},
     {'name': 'patatas bravas',
      'ingredients': ['potato',
       'tomato',
       'olive oil',
       'onion',
       'garlic',
       'paprika'],
      'prep_time': 80},
     {'name': 'fried rice',
      'ingredients': ['rice',
       'soy sauce',
       'egg',
       'onion',
       'pea',
       'carrot',
       'sesame oil'],
      'prep_time': 40}]




```python
try:
    my_collection.insert_many(recipes)
except OperationFailure as ex:
    raise ex
```

## Read/Search/Find Document

### Find all
- retrieve all the documents with `find()` with an empty filter


```python
result = my_collection.find()
```


```python
if result:
    for doc in result:
        recipe = doc['name']
        ing_count = len(doc['ingredients'])
        prep_time = doc['prep_time']
        print(f'{recipe} has {ing_count} ingredients and takes {prep_time} minutes to make.')
else:
    print('No recipes found!')
```

    elotes has 5 ingredients and takes 35 minutes to make.
    loco moco has 6 ingredients and takes 54 minutes to make.
    loco moco has 6 ingredients and takes 54 minutes to make.
    patatas bravas has 6 ingredients and takes 80 minutes to make.
    fried rice has 7 ingredients and takes 40 minutes to make.


### Find One Document

- use find_one API with dictionary as filter - `find_one({<filter>})`


```python
# find a single document that has string 'potato' in the ingredient list
pot_recipe = my_collection.find_one({"ingredients": "potato"})
```


```python
if pot_recipe is not None:
    print("A recipe which uses potato:")
    print(pot_recipe)
else:
    print("No recipes found that contain 'potato' as an ingredient.")
```

    A recipe which uses potato:
    {'_id': ObjectId('65246969eff7a7b93ceedc0f'), 'name': 'patatas bravas', 'ingredients': ['potato', 'tomato', 'olive oil', 'onion', 'garlic', 'paprika'], 'prep_time': 80}


## Update Documents

- You can update a single document or multiple documents in a single call
- Note the 'new=True' option: if omitted, `find_one_and_update()` returns the original document instead of the updated one
- let's change the prep time of the recipe with 'potato' as an ingredient to 72


```python
updated = my_collection.find_one_and_update({'ingredients': 'potato'}, {'$set': {'prep_time': 72}}, new=True)
```


```python
if updated:
    print("Here's the updated recipe:")
    print(updated)
else:
    print("No recipes found that contain 'potato' as an ingredient.")
```

    Here's the updated recipe:
    {'_id': ObjectId('65246969eff7a7b93ceedc0f'), 'name': 'patatas bravas', 'ingredients': ['potato', 'tomato', 'olive oil', 'onion', 'garlic', 'paprika'], 'prep_time': 72}


## Delete Documents

- can delete a single document of all documents that match a specified filter
- to delete all the docuemnts in a collection, pass an emtpy filter to the `delete_many()` API
- let's delete documents in which name field is either 'elotes' or 'fried rice'
- we should delete 2 documents that match the filter


```python
result = my_collection.delete_many({"$or": [{"name": "elotes"}, {"name": "fried rice"}]})
```


```python
print(f'{result.deleted_count} records deleted!')
```

    2 records deleted!


## MongoDB Query Operators

- [See docs](https://www.w3schools.com/mongodb/mongodb_query_operators.php)


```python

```
