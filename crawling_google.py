from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()
arguments = {"keywords":"횡성 소고기", "limit":100, "print_urls":True}
# {"keywords":"한우", "limit":100, "print_urls":True,
# "keywords":"꽃등심", "limit":100, "print_urls":True}
paths = response.download(arguments)
print(paths)
