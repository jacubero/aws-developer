Introduction
############

Overview of Amazon Web Services
*******************************

AWS products and services
=========================

AWS technology consists of a series of interrelated products or services whose release frecuency varies among services. AWS has significantly increase the number of services and features released during the last years as you can see in figure :ref:`fig-innovation`. You can read `Release Notes <https://aws.amazon.com/releasenotes/>`_ to have a summary of all new features, resolved issues, and known issues in the latest versions of AWS products and services.

.. figure:: /services_d/innovation.png
   :name: fig-innovation
   :target: /services_d/innovation.png
   :alt: Number of services and features released during the last years

    Number of services and features released during the last years

.. csv-table:: AWS Services List
   :file: introduction_d/services.csv
   :widths: 15, 85
   :header-rows: 1


.. code-block:: console
   :caption: Get available partitions

    >>> import boto3
    >>> session = boto3.Session()
    >>> session.get_available_partitions()
    [u'aws', u'aws-cn', u'aws-us-gov', u'aws-iso', u'aws-iso-b']


.. code-block:: console
   :caption: Get available regions

    >>> session.get_available_regions('ec2')
    [u'ap-east-1', u'ap-northeast-1', u'ap-northeast-2', u'ap-south-1', u'ap-southeast-1', u'ap-southeast-2', u'ca-central-1', u'eu-central-1', u'eu-north-1', u'eu-west-1', u'eu-west-2', u'eu-west-3', u'me-south-1', u'sa-east-1', u'us-east-1', u'us-east-2', u'us-west-1', u'us-west-2']


.. code-block:: console
   :caption: Get available resources

    >>> session.get_available_resources()
    ['cloudformation', 'cloudwatch', 'dynamodb', 'ec2', 'glacier', 'iam', 'opsworks', 's3', 'sns', 'sqs']

`Region Table <https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/>`_ 

AWS Global Infrastructure
*************************

AWS Regions
===========

The global infrastructure that supports AWS cloud platform is distributed in several separate geographic areas around the world. These areas are called **regions** which consist of two or more **Availability Zones** (AZ) - most of the regions have 3 AZs. Currently, these are the following regions represented by a region code:

.. csv-table:: AWS Region List
   :file: intro_d/regions.csv
   :widths: 20, 40, 40
   :header-rows: 1

.. Note:: Available Regions.

   AWS GovCloud (US-West) account provides access to the AWS GovCloud (US-West) Region only. An Amazon AWS (China) account provides access to the Beijing and Ningxia Regions only. 

   You can't describe or access additional Regions from an AWS account, such as AWS GovCloud (US-West) or the China Regions.

   To use a Region introduced after March 20, 2019, you must enable the Region. For more information, see `Managing AWS Regions <https://docs.aws.amazon.com/general/latest/gr/rande-manage.html>`_ in the AWS General Reference.

.. Note:: Enabled Regions.

   If the Region is enabled by default, the output includes the following:

   *"OptInStatus": "opt-in-not-required"*

   If the Region is not enabled, the output includes the following:

   *"OptInStatus": "not-opted-in"*

   After an opt-in Region is enabled, the output includes the following:

   *"OptInStatus": "opted-in"*

This is the script used to obtain this AWS Region List:

.. literalinclude:: intro_d/describe_regions.py
  :language: python

AWS Availability Zones
======================

An Availability Zone (AZ) consists of several datacenters, all of them linked via intra-AZ connections and each with with redundant power supplies, networking and connectivity, housed in separated facilitiess. All AZ are connected among them through inter-AZ connections and to the exterior via Transit Center connections. AZs are represented by a region code followed by a letter identifier.

.. csv-table:: AWS Availability Zones List
   :file: intro_d/azs.csv
   :widths: 20, 40, 40
   :header-rows: 1

.. literalinclude:: intro_d/describe_azs.sh
  :language: bash

AWS Edge Locations
==================

Amazon Web Services (AWS) publishes its current IP address ranges in JSON format. To view the current ranges, download ip-ranges.json. For more information, see AWS IP Address Ranges in the Amazon Web Services General Reference.

`Locations and IP Address Ranges of CloudFront Edge Servers <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/LocationsOfEdgeServers.html>`_.

.. literalinclude:: intro_d/get_ip_ranges.py
  :language: python
