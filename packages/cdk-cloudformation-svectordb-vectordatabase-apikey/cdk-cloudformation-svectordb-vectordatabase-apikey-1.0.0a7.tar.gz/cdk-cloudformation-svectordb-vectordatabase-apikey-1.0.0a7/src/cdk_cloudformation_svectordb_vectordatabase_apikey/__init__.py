'''
# svectordb-vectordatabase-apikey

> AWS CDK [L1 construct](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html) and data structures for the [AWS CloudFormation Registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) type `SvectorDB::VectorDatabase::ApiKey` v1.0.0.

## Description

Generates an API key to access a SvectorDB serverless vector database, sign up at https://svectordb.com to get started

## Usage

In order to use this library, you will need to activate this AWS CloudFormation Registry type in your account. You can do this via the AWS Management Console or using the [AWS CLI](https://aws.amazon.com/cli/) using the following command:

```sh
aws cloudformation activate-type \
  --type-name SvectorDB::VectorDatabase::ApiKey \
  --publisher-id a867ba60608173fcd64ddc25dcbee967cb54dbb4 \
  --type RESOURCE \
  --execution-role-arn ROLE-ARN
```

Alternatively:

```sh
aws cloudformation activate-type \
  --public-type-arn arn:aws:cloudformation:us-east-1::type/resource/a867ba60608173fcd64ddc25dcbee967cb54dbb4/SvectorDB-VectorDatabase-ApiKey \
  --execution-role-arn ROLE-ARN
```

You can find more information about activating this type in the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html).

## Feedback

This library is auto-generated and published to all supported programming languages by the [cdklabs/cdk-cloudformation](https://github.com/cdklabs/cdk-cloudformation) project based on the API schema published for `SvectorDB::VectorDatabase::ApiKey`.

* Issues related to this generated library should be [reported here](https://github.com/cdklabs/cdk-cloudformation/issues/new?title=Issue+with+%40cdk-cloudformation%2Fsvectordb-vectordatabase-apikey+v1.0.0).
* Issues related to `SvectorDB::VectorDatabase::ApiKey` should be reported to the [publisher](undefined).

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


class CfnApiKey(
    _aws_cdk_ceddda9d.CfnResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdk-cloudformation/svectordb-vectordatabase-apikey.CfnApiKey",
):
    '''A CloudFormation ``SvectorDB::VectorDatabase::ApiKey``.

    :cloudformationResource: SvectorDB::VectorDatabase::ApiKey
    :link: http://unknown-url
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        database_id: builtins.str,
        integration_id: builtins.str,
        endpoint_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new ``SvectorDB::VectorDatabase::ApiKey``.

        :param scope: - scope in which this resource is defined.
        :param id: - scoped id of the resource.
        :param database_id: Database ID.
        :param integration_id: Integration ID.
        :param endpoint_url: (Advanced use cases only) - Custom endpoint URL for contacting the SvectorDB API.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bdd5f88570b584cff61b8a15e0994ed154c3dbaccf5d23c791b901ce29434708)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnApiKeyProps(
            database_id=database_id,
            integration_id=integration_id,
            endpoint_url=endpoint_url,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrApiKey")
    def attr_api_key(self) -> builtins.str:
        '''Attribute ``SvectorDB::VectorDatabase::ApiKey.ApiKey``.

        :link: http://unknown-url
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrApiKey"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CfnApiKeyProps":
        '''Resource props.'''
        return typing.cast("CfnApiKeyProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="@cdk-cloudformation/svectordb-vectordatabase-apikey.CfnApiKeyProps",
    jsii_struct_bases=[],
    name_mapping={
        "database_id": "databaseId",
        "integration_id": "integrationId",
        "endpoint_url": "endpointUrl",
    },
)
class CfnApiKeyProps:
    def __init__(
        self,
        *,
        database_id: builtins.str,
        integration_id: builtins.str,
        endpoint_url: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Generates an API key to access a SvectorDB serverless vector database, sign up at https://svectordb.com to get started.

        :param database_id: Database ID.
        :param integration_id: Integration ID.
        :param endpoint_url: (Advanced use cases only) - Custom endpoint URL for contacting the SvectorDB API.

        :schema: CfnApiKeyProps
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2024c705042748fd4d01af0985145d3f31bc60013114e1283cec85f930da757a)
            check_type(argname="argument database_id", value=database_id, expected_type=type_hints["database_id"])
            check_type(argname="argument integration_id", value=integration_id, expected_type=type_hints["integration_id"])
            check_type(argname="argument endpoint_url", value=endpoint_url, expected_type=type_hints["endpoint_url"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "database_id": database_id,
            "integration_id": integration_id,
        }
        if endpoint_url is not None:
            self._values["endpoint_url"] = endpoint_url

    @builtins.property
    def database_id(self) -> builtins.str:
        '''Database ID.

        :schema: CfnApiKeyProps#DatabaseId
        '''
        result = self._values.get("database_id")
        assert result is not None, "Required property 'database_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def integration_id(self) -> builtins.str:
        '''Integration ID.

        :schema: CfnApiKeyProps#IntegrationId
        '''
        result = self._values.get("integration_id")
        assert result is not None, "Required property 'integration_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def endpoint_url(self) -> typing.Optional[builtins.str]:
        '''(Advanced use cases only) - Custom endpoint URL for contacting the SvectorDB API.

        :schema: CfnApiKeyProps#EndpointUrl
        '''
        result = self._values.get("endpoint_url")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApiKeyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnApiKey",
    "CfnApiKeyProps",
]

publication.publish()

def _typecheckingstub__bdd5f88570b584cff61b8a15e0994ed154c3dbaccf5d23c791b901ce29434708(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    database_id: builtins.str,
    integration_id: builtins.str,
    endpoint_url: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2024c705042748fd4d01af0985145d3f31bc60013114e1283cec85f930da757a(
    *,
    database_id: builtins.str,
    integration_id: builtins.str,
    endpoint_url: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
