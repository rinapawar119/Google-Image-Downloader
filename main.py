user = input("Enter Image name : ")
lim = int(input("How many images you want? "))

from bing_image_downloader import downloader  #importing the library





query_string = user

downloader.download(query_string, limit=lim,
                    output_dir='dataset', adult_filter_off = True, force_replace=False, timeout=60)   #passing the arguments to the function  #printing absolute paths of the downloaded images