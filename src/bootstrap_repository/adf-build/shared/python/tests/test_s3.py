# Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

# pylint: skip-file

import os
import boto3
from pytest import fixture
from .stubs import s3
from mock import Mock
from s3 import S3


@fixture
def cls():
    cls = S3(
        'us-east-1',
        boto3,
        'some_bucket'
    )
    cls.client = Mock()

    return cls
