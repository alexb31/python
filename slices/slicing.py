from random import sample


sample_url = "http://coreyms.com"
print(sample_url)

# reverse url
print(sample_url[::-1])

# Get top level domain
print(sample_url[-4:])

# print url without the http://
print(sample_url[7:])

# print url without the http:// or top level domain
print(sample_url[7:-4])