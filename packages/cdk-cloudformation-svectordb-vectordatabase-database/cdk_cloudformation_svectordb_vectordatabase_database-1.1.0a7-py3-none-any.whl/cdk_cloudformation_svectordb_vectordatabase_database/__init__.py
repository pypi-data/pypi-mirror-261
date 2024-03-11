'''
# svectordb-vectordatabase-database

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `SvectorDB::VectorDatabase::Database` v1.1.0.

## Description

Creates a serverless vector database with SvectorDB, sign up at https://svectordb.com to get started

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name SvectorDB::VectorDatabase::Database \
  --publisher-id a867ba60608173fcd64ddc25dcbee967cb54dbb4 \
  --type RESOURCE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/resource/a867ba60608173fcd64ddc25dcbee967cb54dbb4/SvectorDB-VectorDatabase-Database \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `SvectorDB::VectorDatabase::Database`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Fsvectordb-vectordatabase-database+v1.1.0).
* Issues related to `SvectorDB::VectorDatabase::Database` should be reported to the [publisher](undefined).

## License

Distributed under the Apache-2.0 License.
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from ._jsii import *

import aws_cdk as _aws_cdk_ceddda9d
import constructs as _constructs_77d1e7e8


class CfnDatabase(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/svectordb-vectordatabase-database.CfnDatabase",
):
    '''A CloudFormation ``SvectorDB::VectorDatabase::Database``.

    :cloudformationResource: SvectorDB::VectorDatabase::Database
    :link: http://unknown-url
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        dimension: jsii.Number,
        integration_id: builtins.str,
        metric: "CfnDatabasePropsMetric",
        endpoint_url: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        type: typing.Optional["CfnDatabasePropsType"] = None,
    ) -> None:
        '''Create a new ``SvectorDB::VectorDatabase::Database``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param dimension: 
        :param integration_id: Integration ID.
        :param metric: 
        :param endpoint_url: (Advanced use cases only) - Custom endpoint URL for contacting the SvectorDB API.
        :param name: Name that appears in the SvectorDB console.
        :param type: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a83436ea75bc59e28eb6198361b34581d52cf2547fedeb1600b2d4430137e70)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDatabaseProps(
            dimension=dimension,
            integration_id=integration_id,
            metric=metric,
            endpoint_url=endpoint_url,
            name=name,
            type=type,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''Attribute ``SvectorDB::VectorDatabase::Database.Id``.

        :link: http://unknown-url
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnDatabaseProps":
        '''Resource props.'''
        return typing.cast("CfnDatabaseProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/svectordb-vectordatabase-database.CfnDatabaseProps",
    jsii_struct_bases=[],
    name_mapping={
        "dimension": "dimension",
        "integration_id": "integrationId",
        "metric": "metric",
        "endpoint_url": "endpointUrl",
        "name": "name",
        "type": "type",
    },
)
class CfnDatabaseProps:
    def __init__(
        self,
        *,
        dimension: jsii.Number,
        integration_id: builtins.str,
        metric: "CfnDatabasePropsMetric",
        endpoint_url: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        type: typing.Optional["CfnDatabasePropsType"] = None,
    ) -> None:
        '''Creates a serverless vector database with SvectorDB, sign up at https://svectordb.com to get started.

        :param dimension: 
        :param integration_id: Integration ID.
        :param metric: 
        :param endpoint_url: (Advanced use cases only) - Custom endpoint URL for contacting the SvectorDB API.
        :param name: Name that appears in the SvectorDB console.
        :param type: 

        :schema: CfnDatabaseProps
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9c1eba5f90b1f142d1408993d51049b967af0230e9c9db44c08bb1952b9fd01)
            check_type(argname="argument dimension", value=dimension, expected_type=type_hints["dimension"])
            check_type(argname="argument integration_id", value=integration_id, expected_type=type_hints["integration_id"])
            check_type(argname="argument metric", value=metric, expected_type=type_hints["metric"])
            check_type(argname="argument endpoint_url", value=endpoint_url, expected_type=type_hints["endpoint_url"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "dimension": dimension,
            "integration_id": integration_id,
            "metric": metric,
        }
        if endpoint_url is not None:
            self._values["endpoint_url"] = endpoint_url
        if name is not None:
            self._values["name"] = name
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def dimension(self) -> jsii.Number:
        '''
        :schema: CfnDatabaseProps#Dimension
        '''
        result = self._values.get("dimension")
        assert result is not None, "Required property 'dimension' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def integration_id(self) -> builtins.str:
        '''Integration ID.

        :schema: CfnDatabaseProps#IntegrationId
        '''
        result = self._values.get("integration_id")
        assert result is not None, "Required property 'integration_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def metric(self) -> "CfnDatabasePropsMetric":
        '''
        :schema: CfnDatabaseProps#Metric
        '''
        result = self._values.get("metric")
        assert result is not None, "Required property 'metric' is missing"
        return typing.cast("CfnDatabasePropsMetric", result)

    @builtins.property
    def endpoint_url(self) -> typing.Optional[builtins.str]:
        '''(Advanced use cases only) - Custom endpoint URL for contacting the SvectorDB API.

        :schema: CfnDatabaseProps#EndpointUrl
        '''
        result = self._values.get("endpoint_url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''Name that appears in the SvectorDB console.

        :schema: CfnDatabaseProps#Name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def type(self) -> typing.Optional["CfnDatabasePropsType"]:
        '''
        :schema: CfnDatabaseProps#Type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional["CfnDatabasePropsType"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDatabaseProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(
    jsii_type="@cdk-cloudformation/svectordb-vectordatabase-database.CfnDatabasePropsMetric"
)
class CfnDatabasePropsMetric(enum.Enum):
    '''
    :schema: CfnDatabasePropsMetric
    '''

    EUCLIDEAN = "EUCLIDEAN"
    '''EUCLIDEAN.'''
    DOT_UNDERSCORE_PRODUCT = "DOT_UNDERSCORE_PRODUCT"
    '''DOT_PRODUCT.'''
    COSINE = "COSINE"
    '''COSINE.'''


@jsii.enum(
    jsii_type="@cdk-cloudformation/svectordb-vectordatabase-database.CfnDatabasePropsType"
)
class CfnDatabasePropsType(enum.Enum):
    '''
    :schema: CfnDatabasePropsType
    '''

    SANDBOX = "SANDBOX"
    '''SANDBOX.'''
    STANDARD = "STANDARD"
    '''STANDARD.'''


__all__ = [
    "CfnDatabase",
    "CfnDatabaseProps",
    "CfnDatabasePropsMetric",
    "CfnDatabasePropsType",
]

publication.publish()

def _typecheckingstub__2a83436ea75bc59e28eb6198361b34581d52cf2547fedeb1600b2d4430137e70(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    dimension: jsii.Number,
    integration_id: builtins.str,
    metric: CfnDatabasePropsMetric,
    endpoint_url: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    type: typing.Optional[CfnDatabasePropsType] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9c1eba5f90b1f142d1408993d51049b967af0230e9c9db44c08bb1952b9fd01(
    *,
    dimension: jsii.Number,
    integration_id: builtins.str,
    metric: CfnDatabasePropsMetric,
    endpoint_url: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    type: typing.Optional[CfnDatabasePropsType] = None,
) -> None:
    """Type checking stubs"""
    pass
