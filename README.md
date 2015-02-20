# Nutch-Polar #
Crawling and Deduplication of Polar Datasets Using Nutch and Tika
------------------------------------------------------------------------------------------------------------------------
###fetch_url.py###
A program to fetch the content of the urls crawled by Apache Nutch.
#####Usage:#####
python fetch_url.py inputfile string_to_be_searched

inputfile is the dump data of CrawlDb.

string_to_be_searched is any string you want to find in the file

Output: Dictionary conatining those snippets with count.

