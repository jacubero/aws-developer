AWS Global Infrastructure
#########################

This is the script used to obtain this AWS Region List:

.. literalinclude:: global_d/describe_regions.py
  :language: python


.. literalinclude:: global_d/describe_azs.sh
  :language: bash

Amazon Web Services (AWS) publishes its current IP address ranges in JSON format. To view the current ranges, download ip-ranges.json. For more information, see AWS IP Address Ranges in the Amazon Web Services General Reference.

`Locations and IP Address Ranges of CloudFront Edge Servers <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/LocationsOfEdgeServers.html>`_.

.. literalinclude:: global_d/get_ip_ranges.py
  :language: python
