# Copyright 2019 Jose Antonio Alvarez Cubero. All Rights Reserved.
#
# This file is licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License. A copy of the
# License is located at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS
# OF ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License. 

import requests
import json
import csv


""" Download the ip-ranges.json file with current AWS IP Ranges. Reference:
https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/LocationsOfEdgeServers.html.

"""
def main():

    URL_IP_RANGES = 'https://ip-ranges.amazonaws.com/ip-ranges.json'
 
    with requests.Session() as s:
        IPRanges = s.get(URL_IP_RANGES)
        IPRanges_json = IPRanges.json()

    f = csv.writer(open("ip-ranges.csv", "wb+"))

    # Write CSV Header
    f.writerow(["IpPrefix", "Region", "Service", "IpVersion"])

    for ipv4range in IPRanges_json["prefixes"]:
        f.writerow([ipv4range["ip_prefix"], ipv4range["region"], ipv4range["service"], "IPv4"])

    for ipv6range in IPRanges_json["ipv6_prefixes"]:
        f.writerow([ipv6range["ipv6_prefix"], ipv6range["region"], ipv6range["service"], "IPv6"])
 

if __name__ == '__main__':
    main()
