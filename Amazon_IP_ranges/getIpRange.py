#!/usr/bin/env python
import requests

ipv4_ranges = requests.get('https://ip-ranges.amazonaws.com/ip-ranges.json').json()['prefixes']
amazon_ipv4s = [item['ip_prefix'] for item in ipv4_ranges if item["region"] == "us-west-2" and item["service"] in ("AMAZON", "S3") ]
ipv6_ranges = requests.get('https://ip-ranges.amazonaws.com/ip-ranges.json').json()['ipv6_prefixes']
amazon_ipv6s = [item['ipv6_prefix'] for item in ipv6_ranges if item["region"] == "us-west-2" and item["service"] in ("AMAZON", "S3") ]

amazon_ips = list(set(amazon_ipv4s).union(set(amazon_ipv6s)))

f= open("/Users/mathurv/Desktop/temp_folder/amz_ips")
listed_ips = []
listed_ips = f.read().splitlines()

for ip in list(set(amazon_ips)-set(listed_ips)):
        print("missing " + str(ip))
        listed_ips.append(ip)

for ip in list(set(listed_ips)-set(amazon_ips)):
        print("extra " + str(ip))
        listed_ips.remove(ip)


# amazon_ips_less_ec2=[]
     
# for ip in amazon_ips:
#     if ip not in ec2_ips:
#         amazon_ips_less_ec2.append(ip)

# set(listed_ips) & set(amazon_ips_less_ec2) 

fw= open("/Users/mathurv/Desktop/temp_folder/amz_ips","w")    
for ip in listed_ips:
        #print(str(ip))
        fw.write(str(ip)+"\n")
        
fw.close()

