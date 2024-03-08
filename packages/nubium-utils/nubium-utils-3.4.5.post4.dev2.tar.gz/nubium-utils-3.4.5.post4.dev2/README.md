# Nubium Utils

## Environment Variables

Nubium-Utils now has a prefix for every environment variable it uses. Every environment
variable related to Nubium-Utils starts with `NU_`.

Similarly, anything DUDE-related will start with `DUDE_`.

### Important Environment Variables

Nubium-Utils relies on having these environment variables defined:
- `NU_SCHEMA_REGISTRY_URL`: schema registry url
- `NU_SCHEMA_REGISTRY_USERNAME`: schema registry username (if applicable)
- `NU_SCHEMA_REGISTRY_PASSWORD`: schema registry password (if applicable)
- `NU_KAFKA_CLUSTERS_CONFIGS_JSON`: json of clusters and their respective connection settings. EX:
`'{"cluster_0": {"url": "url", "username": "un", "password": "pw"}, "cluster_1": {"url": "url", "username": "un", "password": "pw"}}'`
- `NU_TOPIC_CONFIGS_JSON`: json of topics and their respective cluster name (will reference NU_KAFKA_CLUSTERS) + (optional) create settings. EX:
`'{"topic_a": {"cluster": "cluster_0", "configs": {"num_partitions": 2, "replication_factor": 2, "config": {"segment.ms": 120000}}}, "topic_b": {"cluster": cluster_1}}'`
- `NU_HOSTNAME`: used for identifying unique consumer instances
- `NU_APP_NAME`: used to define your consumer group
- `NU_MP_PROJECT`: used for openshift deployment


## Confluent-Kafka GTFO App Classes

### Overview
Nubium Utils now has an app framework for managing exactly-once processing confluent-kafka applications, named `GTFO`. 
The idea is to simplify confluent-kafka down to a kafka-streams-like interface, where consumer management is largely
handled for you under the hood. This is particularly nice for having to manage exactly-once processing, 
which the class implements and uses by default.

There are some other subclasses for some more specific use cases, namely `GtfoBatchApp` and `GtfoTableApp`, but
the base class `GtfoApp` has been written with the intention of being easily extensible. Further details in
terms of the recommended approaches of this will be described below.


### The `Transaction` and `Gtfo` classes

There are two essential classes you should understand before you dive in. 

The `Transaction` classes are actually the heart of the `GTFO` framework; they are what your business
logic methods will actually be interacting with on a message-to-message basis. That being said, for most
use cases, you wont even need to do much with them other than `Transaction.messages()` to get the currently consumed
message, and `Transaction.produce()` to send a new message out.

The `Gtfo`-based classes generally wrap/interface with the `Transaction` objects, generating a new one for
every new transaction (which generally consists of consuming a message, produce desired messages, commit
consumed message.) In general, you will really only use the `Gtfo` class to initialize everything, and it doesn't
take much.

Finally, as a general rule of thumb for both, there are not many methods to interact with on either class...
on purpose! The functionality outlined in here will likely cover >90% of use cases.


### Initializing/running a `GtfoApp`: basic example

NOTE: there is a lot that is managed for you via environment variables, so definitely take a look at the 
"**Important Environment Variables**" section to see what you should have defined before trying to run a `GTFO` app.

There are two basic components you need to initialize an app at all:

- `app_function`: the business logic of your application, which should use exactly 1 argument: the `Transaction` objects
that will be handed to it for every message.

- `consume_topics_list`: the topics you are consuming. Can be comma-separated string or python list.

That's it! That being said, this is if your app only consumes. To produce, you will additionally need, at minimum:

- `produce_topic_schema_dict`: a dict that maps {'topic_name': _schema_obj_}, where the _schema_obj_ is a valid avro
schema dict.

Then, to run the app, do:

`GtfoApp.run()`

Altogether, that might look something like this:

```python
from nubium_utils.confluent_utils.transaction_utils import GtfoApp

useless_schema = {
    "name": "CoolSchema",
    "type": "record",
    "fields": [
        {
            "name": "cool_field",
            "type": "string"
        }
    ]
}


def useless_example_func(transaction, thing_inited_at_runtime):
    msg = transaction.messages() # can also do transaction.value(); uses the confluent-kafka method with single messages
    cool_message_out = msg.value()
    cool_message_out['cool_field'] = thing_inited_at_runtime #  'cool value'
    transaction.produce({'topic':'cool_topic_out', 'key': msg.key(), 'value': cool_message_out, 'headers': msg.headers()})

init_at_runtime_thing = 'cool value' # can hand off objects you need to init at runtime, like an api session object
    
gtfo_app = GtfoApp(
    app_function=useless_example_func, 
    consume_topics_list=['test_topic_1', 'test_topic_2'],
    produce_topic_schema_dict={'cool_topic_out': useless_schema},
    app_function_arglist = [init_at_runtime_thing])  # optional! Here to show functionality.
gtfo_app.run()
```

### Using `GtfoBatchApp` (plus `BatchTransaction`)

Sometimes, you want to handle multiple messages at once, such as doing a bulk upload of data to an API. 
In this case, treating each message as a separate transaction doesn't make much sense! For this, we have `GtfoBatchApp`!

We still rely on much of what `Gtfo` and `Transaction` lays out, but now we can specify how many messages should
be consumed by default for a given transaction. Additionally, you can consume more messages on demand with the
`BulkTransaction` object via `BulkTransaction.consume()` in your `app_function`, in case you'd like to do the normal 
consume pattern most of the time, but might need that to change on demand.

Biggest thing to note here: all messages for that transaction will (just like `Transaction`) be accessible via 
`BatchTransaction.messages()`. Also, all of them get committed when you finish with that instance of `app_function` just
like a typical singleton run of `app_function`, so keep that in mind!

You can tweak the default batch size via `NU_CONSUMER_DEFAULT_BATCH_CONSUME_MAX_COUNT`; defaulted to 1.

Here is an example:

```python
from nubium_utils.confluent_utils.transaction_utils import GtfoBatchApp
from cool_api import bulk_upload

useless_schema = {
    "name": "CoolSchema",
    "type": "record",
    "fields": [
        {
            "name": "cool_field",
            "type": "string"
        }
    ]
}

def prep_data(msg_val):
    # do stuff
    pass

def useless_example_func(bulk_transaction):
    msg = transaction.messages()
    last_msg = msg[-1]
    # I originally set my max to 10 via the env var...but with some logic, if a message says I should do a bigger batch...
    if last_msg.headers()['needs_bigger_bulk'] == 'true':
        bulk_transaction.consume(consume_max_count=500) # allow me to raise that max to 500, and consume up to that (will consume up to 490 more)!
    bulk_upload([prep_data(msg.value()) for msg in bulk_transaction.messages()]) # push all 500 messages
    
gtfo_app = GtfoBatchApp(
    app_function=useless_example_func, 
    consume_topic='test_topic_in',
    produce_topic_schema_dict={'cool_topic_out': useless_schema})
gtfo_app.run()
```


### Using `GtfoTableApp` (plus `TableTransaction`)

One of the more complex components of GTFO is the `GtfoTableApp`. It allows you to store state based on a 
kafka topic via a localized datastore. Basically, you can store whatever you want with respect to a given kafka key, 
and later reference/compare that data against a new version of that key.

There are some functional caveats/limitations that come along with this feature set:
- The app can only consume from one topic (you can make an upstream "funnel" app as needed).
- You must make a topic named the same as `{NU_APP_NAME}__changelog`, with the same partition count as the topic it 
would consume from.
- You can only store/reference things based on the same key as the current message.
- Each instance of your application needs to use the same volume.
- Data needs to be stored as a json/dict (it is stored as a string and `json.load`-ed at runtime)

With that in mind, set up is almost exactly the same as `GtfoApp`; here is an example:

```python
from nubium_utils.confluent_utils.transaction_utils import GtfoTableApp

useless_schema = {
    "name": "CoolSchema",
    "type": "record",
    "fields": [
        {
            "name": "cool_field",
            "type": "string"
        }
    ]
}


def useless_example_func(transaction):
    msg = transaction.messages() # can also do transaction.value(); uses the confluent-kafka method with single messages
    cool_message_out = msg.value()
    previous_message = transaction.read_table_entry()
    # lets only do stuff if our previous version for the same key was "just cool"!
    if previous_message['cool_field'] == 'just cool':
        cool_message_out['cool_field'] = 'very cool now'
        transaction.update_table_entry(cool_message_out) # we want to update the table with our new value. It does not do this automatically!
        transaction.produce({'topic':'cool_topic_out', 'key': msg.key(), 'value': cool_message_out, 'headers': msg.headers()})

    
gtfo_app = GtfoTableApp(
    app_function=useless_example_func, 
    consume_topic='test_topic_in',
    produce_topic_schema_dict={'cool_topic_out': useless_schema})
gtfo_app.run()
```

### Extending `GtfoApp` and `Transaction`

Of course, you can never cover _every_ use case! As such, each class was designed
with extensibility in mind!

Most often, what needs more customization is your consumption pattern (hence why there was already a bulk class!), 
and there is a relatively painless way to address that with minimal alterations.

There is an `init` argument on `GtfoApp` named `transaction_type`; this allows you to easily pass an augmented
version of `Transaction` with your changed consumption pattern, potentially without changing the `Transaction` class
at all!

Otherwise, hopefully things have been compartimentalized enough that you can just replace methods as needed, but
in general, usually you'll need to mess a little with both classes, but likely mostly `Transaction`.

## Monitoring
The monitoring utils enable metrics to be surfaced from the kafka applications
so the Prometheus server can scrape them.
The Prometheus server can't dynamically figure out pod IPs and scrape the
services directly, so we're using a metrics cache instead.

The metrics cache is a StatefulSet with 2 services assigned to it.
One service is a normal service, with a unique cluster IP address.
The prometheus server scrapes this service endpoint.
The other service doesn't have a cluster IP,
which means that the monitoring utility can find the IP addresses of each
of the backing pods, and send metrics to all of the pods.
This setup gives us high-availability guarantees.

The Monitoring utils are organized into two classes, `MetricsPusher` and `MetricsManager`.

The `MetricsManager` is a container for all of the metrics for the app,
and contains convenience methods for the 3 standardized metrics.
These metrics are
- `messages_consumed`: The number of messages consumed by the app
- `messages_produced`: The number of messages produced by the app
- `message_errors`: The number of exceptions caught in the app (labeled by type)

The `MetricsPusher` handles pushing the applications metrics to the metrics cache.
It determines the list of IP addresses for all of the metrics cache pods,
and sends the current metrics values for all of the metrics.

### Metric names and labels
The names of the metrics in Prometheus are the same as their names as parameters
- `messages_consumed`
- `messages_produced`
- `message_errors`

Two labels exist for every metric:
- `app`: The name of the microservice the metric came from
- `job`: The name of the individual pod the metric came from
The `message_errors` metric also has another label:
- `exception`: The name of the exception that triggered the metric

### Monitoring Setup Examples
The initialization and update loop for application monitoring will differ
from application to application based on their architecture.
The following examples should cover the standard designs we use.

#### Default Kafka Client Application
A Kafka application that directly relies on interacting with Producer or
Consumer clients should have it's monitoring classes set up and its
pushing thread started in the main run function and passed to the loop, as follows:
```python
import os

from confluent_kafka import Consumer, Producer
from nubium_utils.metrics import MetricsManager, MetricsPusher, start_pushing_metrics

def run_function():

    consumer = Consumer()
    producer = Producer()

    metrics_pusher = MetricsPusher(
        os.environ['HOSTNAME'],
        os.environ['METRICS_SERVICE_NAME'],
        os.environ['METRICS_SERVICE_PORT'],
        os.environ['METRICS_POD_PORT'])
    metrics_manager = MetricsManager(job=os.environ['HOSTNAME'], app=os.environ['APP_NAME'], metrics_pusher=metrics_pusher)
    start_pushing_metrics(metrics_manager, int(os.environ['METRICS_PUSH_RATE']))

    try:
        while True:
            loop_function(consumer, producer, metrics_manager=metrics_manager)
    finally:
        consumer.close()

```

The `consume_message()` function from this library expects a metrics_manager object
as an argument, so that it can increment the `messages_consumed` metric.

The application itself needs to increment the `messages_produced` metric
needs to be incremented as necessary by the application itself
whenever a Kafka message is produced. The convenience method on the metrics_manager
`inc_messages_produced()` makes this easier,
since it automatically adds the necessary labels to the metric.

The application also needs to be set to increment the `message_errors` metric
whenever an exception is caught.

An example loop function might look like this:
```python
import os
import logging

from nubium_utils import consume_message
from nubium_utils.custom_exceptions import NoMessageError


def loop_function(consumer, producer, metrics_manager):
    try:
        message = consume_message(consumer, int(os.environ['CONSUMER_POLL_TIMEOUT']), metrics_manager)
        outgoing_key = message.value()['email_address']
        producer.produce(topic='outgoing_topic',key=outgoing_key,value=message.value())
        metrics_manager.inc_messages_produced(1)
    except NoMessageError:
        pass
    except KeyError as error:
        metrics_manager.inc_message_errors(error)
        logging.debug('Message missing email address')


```

#### Flask Kafka Application
The setup becomes a little bit different with a Flask application.
The metrics_manager should be accessible through the app's configuration,
so that it can be accessed in route functions.

The preferred method for error monitoring is to hook into the built in
flask error handling loop, using the `@app.errorhandler` decorator.
Here is an example `create_app()` function

```python
import flask
from werkzeug.exceptions import HTTPException

from .forms_producer_app import forms_producer
from .util_blueprint import app_util_bp

def create_app(config):
    """
    Creates app from config and needed blueprints
    :param config: (Config) object used to configure the flask app
    :return: (flask.App) the application object
    """
    app = flask.Flask(__name__)
    app.config.from_object(config)

    app.register_blueprint(forms_producer)
    app.register_blueprint(app_util_bp)

    @app.errorhandler(HTTPException)
    def handle_exception(e):
        """
        Increment error gauge on metrics_manager before returning error message
        """
        response = e.get_response()
        response.data = f'{e.code}:{e.name} - {e.description}'
        app.config['MONITOR'].inc_message_errors(e)
        return response

    @app.errorhandler(Exception)
    def unhandled_exception(error):
        app.logger.error(f'Unhandled exception: {error}')
        app.config['MONITOR'].inc_message_errors(error)
        return f'Unhandled exception: {error}', 500

    return app
```

The route functions for produced messages should increase the `messages_produced`
metric when necessary.
Example:
```python

@forms_producer.route('/', methods=["POST"])
@AUTH.login_required
def handle_form():
    """
    Ingests a dynamic form from Eloqua and produces it to the topic
    """
    values = request.json
    string_values = {key: str(value) for key, value in values.items()}
    LOGGER.debug(f'Processing form: {values}')

    current_app.config['PRODUCER'].produce(
        topic=current_app.config['TOPIC'],
        key=values['C_EmailAddress'],
        value={'form_data': string_values},
        on_delivery=produce_message_callback
    )
    current_app.config['MONITOR'].inc_messages_produced(1)

    return jsonify(success=True)
```