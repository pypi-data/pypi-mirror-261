# Github: https://github.com/beh185
# Telegram: https://T.me/dr_xz
# e-mail: BehnamH.dev@gmail.com
# ____________________________________________

# ======== # Import Modules # ======== #
try:
    from os import path, name
    from requests import get, post, delete, put , Response, exceptions
    from urllib.request import urlretrieve
    from urllib.error import URLError
    from tqdm import trange
except ImportError:
    raise ImportError("[+] One of the required modules is missing. Please Install the required modules by reinstalling the library")

# =========== # Functions # =========== #

# ======== # Checking for http errors # ======== #
def __check_http_error(respond) -> None:
    if(respond.status_code == 400):
        print("[400 Error] The request was unacceptable, often due to missing a required parameter")
    elif(respond.status_code == 401):
        print("[401 Error] Invalid Access Token")
    elif(respond.status_code == 403):
        print("[403 Error] Missing permissions to perform request")
    elif(respond.status_code == 404):
        print("[404 Error] The requested resource doesn't exist")
    elif(respond.status_code == 500 or respond.status_code == 503):
        print(f"[{respond.status_code} Error] Something went wrong on unsplash's end")
    else:
        print(f"[{respond.status_code} Error] Something went wrong")

class Photos:
    def __init__(self, client_id:str) -> None:
        '''`client_id`:   Your Unsplash Access Key. [For More Help](https://unsplash.com/documentation#creating-a-developer-account)'''
        Photos.client_id :str = client_id
    
    # ======== # Downloading random images from unsplash. # ======== #
    def random_photo(self, count:int = 1, query:str = str(),topics:str = str() ,collections:str = str(), username:str = str(), orientation:str = str(), content_filter:str = 'low', DownloadImg=True, FileName: str = 'S-image', UPath: str = str(), pass_errors: bool = False):
        '''Download photos by search results.
    All parameters are Optional.
    |param     | Description   |    
    ---|---|   
    | `count`: |  The number of photos to return. (Default: 1; max: 30) |
    | `query`: |  Search terms. |
    | `topics`: |  Public topic ID('s) to filter selection. If multiple, comma-separated
    | `collections`: |  Collection ID('s) to narrow search. Optional. If multiple, comma-separated. |
    | `content_filter`: |  Limit results by [content safety](https://unsplash.com/documentation#content-safety). (Optional; default: low). Valid values are low and high. |
    | `orientation`: |  The orientation of the images to download. |
    | `DownloadImg`: |  A boolean value indicating whether to download the images. |
    | `FileName`: |  The name of the file to save the images to. |
    | `UPath`: |  The path to the directory to save the images to. |
    | `_pass_errors` : | If there an error during the process. It won't break the program. It will just skip the process|
        '''
        payload: dict = {
            'client_id': self.client_id,
            'query':query,
            'count':count,
            'topics':topics,
            'collections':collections,
            'username': username,
            'orientation': orientation,
            'content_filter':content_filter}
        # ======== # Making copy to prevent RuntimeError: dictionary changed size during iteration # ======== #
        PayLoad: dict = payload.copy()

        # ====== # Removing values that user didn't specified # ====== #
        for key, value in payload.items():
            if (value == '' or value == 0):
                PayLoad.pop(key)

        
        unsplash_api = 'https://api.unsplash.com/photos/random'
        try:
            ResponseData: Response = get(unsplash_api, allow_redirects=True, timeout=25, params=PayLoad)
        except exceptions.ConnectionError:
            if(pass_errors == False):
                raise TypeError("Connection Failed. It's might because of your network connection")
            else:
                return("Connection Failed. It's might because of your network connection")
        except KeyboardInterrupt:
            if(pass_errors == False):
                raise TypeError('\nOperation canceled by user')
            else:
                pass
                return('\nOperation canceled by user')
        except exceptions.ReadTimeout:
            if(pass_errors == False):
                raise TypeError('Time out has reached')
            else:
                return('Time out reached')
            
        # ======== # Checking for http errors # ======== #
        if(ResponseData.ok == False):
            if pass_errors == False:
                raise Exception(__check_http_error(ResponseData))
            else:
                pass
                return(__check_http_error(ResponseData))
        else:        
            JsonImg: dict = ResponseData.json()
        
        # ======== # Download photos # ======== #
        if(DownloadImg):
            print('Downloading images ...')
            if(UPath != str()):
                
                # ==== # Check if given path is valid # ==== # 
                if(path.exists(UPath) == False):
                    if(pass_errors):
                        print(f'The path was invalid. saving on {__file__.replace("unsplash.py", "")}')
                    exit(f'"{UPath}" is not exist')

                if(name == 'nt' and UPath.endswith('\\') == False):
                    UPath: str = UPath + '\\'
                elif(name == 'posix' and UPath.endswith('/') == False):
                    UPath: str = UPath + '/'

            # ==== # If count var is given, data will be change  # ==== #
            if(count != 0):
                for i in trange(count):
                    ImgLink: str = JsonImg[i]['urls']['full'] 
                    try:
                        urlretrieve(ImgLink, f"{UPath}{FileName}-{JsonImg[i]['id']}.jpg")
                    except URLError:
                        if(pass_errors):
                            pass
                            return('Error! It might be because of the network problem or your setting issues, such as proxy setting')
                        else:
                            raise ConnectionError ('Error! It might be because of the network problem or your setting issues, such as proxy setting')
        else:
            return JsonImg
    
    def photos_statistics(self, ID: str, resolution:str = 'days', quantity:int = 30, pass_errors: bool = False) -> None | str:
        '''Retrieve total number of downloads, views and likes of a single photo, as well as the historical breakdown of these stats in a specific timeframe (default is 30 days)
|param     |Description     |
---|---|
|`id`: | The public id of the photo. Required.|
|`resolution`:  |  The frequency of the stats. (Optional; default: “days”)|
|`quantity`: | The amount of for each stat. (Optional; default: 30)|'''
        payload: dict = {
            'client_id': self.client_id,
            'ID':ID,
            'resolution':resolution,
            'quantity':quantity
        }
        
        unsplash_api = f'https://api.unsplash.com/photos/{ID}/statistics'
        try:
            ResponseData: Response = get(unsplash_api, allow_redirects=True, timeout=25, params=payload)
        except exceptions.ConnectionError:
            if(pass_errors == False):
                raise TypeError("Connection Failed. It's might because of your network connection")
            else:
                return("Connection Failed. It's might because of your network connection")
        except KeyboardInterrupt:
            if(pass_errors == False):
                raise TypeError('\nOperation canceled by user')
            else:
                pass
                return('\nOperation canceled by user')
        except exceptions.ReadTimeout:
            if(pass_errors == False):
                raise TypeError('Time out has reached')
            else:
                return('Time out reached')
            
        # ======== # Checking for http errors # ======== #
        if(ResponseData.ok == False):
            if pass_errors == False:
                raise Exception(__check_http_error(ResponseData))
            else:
                pass
                return(__check_http_error(ResponseData))
        else:
            return ResponseData.json()
        
class Search:
    def __init__(self, client_id:str) -> None:
        '''`client_id`:   Your Unsplash Access Key. [For More Help](https://unsplash.com/documentation#creating-a-developer-account)'''
        Search.client_id :str = client_id
        
    # ======== # Downloading Images results for a query. # ======== #
    def search_photo(self, query: str, page: int = int(), per_page:int = int(), order_by:str = str(), collections = str(), content_filter = str(), color = str(), orientation = str(), DownloadImg=True, FileName: str = 'S-image', UPath: str = str(), pass_errors: bool = False) -> dict | None | str: # type: ignore
        '''Download photos by search results.
    |param     | Description   |    
    ---|---|   
    | `query`: |  Search terms. |
    | `page`: |  The page number of the results to download. (Optional; default: 1) |
    | `per_page`: |  The number of images to download per page. (Optional; default: 10)
    | `order_by`: |  The order in which to sort the results. (Optional; default: relevant). Valid values are latest and relevant. |
    | `collections`: |  Collection ID('s) to narrow search. Optional. If multiple, comma-separated. |
    | `content_filter`: |  Limit results by [content safety](https://unsplash.com/documentation#content-safety). (Optional; default: low). Valid values are low and high. |
    | `color`: |  Filter results by color. Optional. Valid values are: black_and_white, black, white, yellow, orange, red, purple, magenta, green, teal, and blue. |
    | `orientation`: |  The orientation of the images to download. |
    | `DownloadImg`: |  A boolean value indicating whether to download the images. |
    | `FileName`: |  The name of the file to save the images to. |
    | `UPath`: |  The path to the directory to save the images to. |
    | `_pass_errors` : | If there an error during the process. It won't break the program. It will just skip the process|
        '''
        payload: dict = {
            'client_id': self.client_id,
            'query':query,
            'page':page,
            'per_page':per_page,
            'collections':collections,
            'order_by': order_by,
            'color':color,
            'orientation': orientation,
            'content_filter':content_filter}

        # ======== # Making copy to prevent RuntimeError: dictionary changed size during iteration # ======== #
        PayLoad: dict = payload.copy()

        # ====== # Removing values that user didn't specified # ====== #
        for key, value in payload.items():
            if (value == '' or value == 0):
                PayLoad.pop(key)

        
        unsplash_api = 'https://api.unsplash.com/search/photos'
        try:
            ResponseData: Response = get(unsplash_api, allow_redirects=True, timeout=25, params=payload)
        except exceptions.ConnectionError:
            if(pass_errors == False):
                raise TypeError("Connection Failed. It's might because of your network connection")
            else:
                return("Connection Failed. It's might because of your network connection")
        except KeyboardInterrupt:
            if(pass_errors == False):
                raise TypeError('\nOperation canceled by user')
            else:
                return('\nOperation canceled by user')
        except exceptions.ReadTimeout:
            if(pass_errors == False):
                raise TypeError('Time out has reached')
            else:
                return('Time out reached')
            
        # ======== # Checking for http errors # ======== #
        if(ResponseData.ok == False):
            if pass_errors == False:
                raise Exception(__check_http_error(ResponseData))
            else:
                pass
                return(__check_http_error(ResponseData))
        else:        
            JsonImg: dict = ResponseData.json()
            
        # ======= # Download images# ======= #
        if(DownloadImg):
            print('Downloading images ...')
            if(UPath != str()):
                if(path.exists(UPath) == False):
                    exit(f'"{UPath}" is not exist')

                if(name == 'nt' and UPath.endswith('\\') == False):
                    UPath: str = UPath + '\\'
                elif(name == 'posix' and UPath.endswith('/') == False):
                    UPath: str = UPath + '/'

            for i in range(per_page):
                ImgLink: str = JsonImg['results'][i]['urls']['full'] #type: ignore
                try:
                    urlretrieve(ImgLink, f"{UPath}{FileName}-{i}.jpg")
                except URLError:
                    exit('Error! It might be because of the network problem or your setting issues, such as proxy setting')
        else:
            return JsonImg
    
       # ======== # Get a single page of user results for a query # ======== #
    def search_users(self, query: str, page: int = 1, per_page: int = 10, pass_errors: bool = False) -> list[dict] | str:
        '''Search for a user and getting back the results as list that contain a dictionary.
    If the operation was successful, returns a list with dictionary inside that contain search info. Raise the error message if the operation was unsuccessful.
    | param | Description|
    ---|---|

    | `query` : |	Search terms.|
    | `page` : | The page number of the results to download. (Optional; default: 1)
    | `per_page` : | The number of images to download per page.  (Optional; default: 10)
    | `_pass_errors` : | If there an error during the process. It won't break the program. It will just skip the process|'''

        PayLoad: dict = {
            'client_id': self.client_id,
            'query':query,
            'page': page,
            'per_page':per_page}

        
        unsplash_api: str = 'https://api.unsplash.com/search/users'
        
        try:
            ResponseData: Response = get(unsplash_api, allow_redirects=True, timeout=25, params=PayLoad)
        except exceptions.ConnectionError:
            if(pass_errors == False):
                raise TypeError("Connection Failed. It's might because of your network connection")
            else:
                return(("Connection Failed. It's might because of your network connection"))
        except KeyboardInterrupt:
            if(pass_errors == False):
                raise TypeError('\nOperation canceled by user')
            else:
                return('\nOperation canceled by user')
        except exceptions.ReadTimeout:
            if(pass_errors == False):
                raise TypeError('Time out has reached')
            else:
                return('Time out has reached')
        
        # ======== # Checking for http errors # ======== #
        if(ResponseData.ok == False):
            if pass_errors == False:
                raise Exception(__check_http_error(ResponseData))
            else:
                pass
                return __check_http_error(ResponseData) # type: ignore
        else:
            JsonData: dict = ResponseData.json()
        
        return JsonData['results']

        
class Collection:
    def __init__(self, client_id:str) -> None:
        '''`client_id`:   Your Unsplash Access Key. [For More Help](https://unsplash.com/documentation#creating-a-developer-account)'''
        Collection.client_id :str = client_id
    
    # ========== # Retrieve a collection’s photos. # ========== #
    def download_collection(self, ID, page: int = int(), per_page: int = int(), orientation: str = str(), DownloadImg: bool = True, FileName: str = 'C-image', UPath: str = str(), pass_errors: bool = False) -> dict | None | str: # type: ignore
        '''Download a collection's photos.
    | param | Description |
    ---|---|

    | `ID` : | 	The collection's ID. Required. |
    | `page` : | Page number to retrieve. (Optional; default: 1) |
    | `per_page` : | Number of items per page. (Optional; default: 10) | 
    | `orientation` : | Filter by photo orientation. Optional. (Valid values: landscape, portrait, squarish) |
    | `DownloadImg`: |  A boolean value indicating whether to download the images. |
    | `FileName`: |  The name of the file to save the images to. |
    | `UPath`: |  The path to the directory to save the images to. |
    | `_pass_errors` : | If there an error during the process. It won't break the program. It will just skip the process|'''

        payload: dict = {
            'client_id': self.client_id,
            'page':page,
            'per_page':per_page,
            'orientation': orientation}
        
        # ======== # Making copy to prevent RuntimeError: dictionary changed size during iteration # ======== #
        PayLoad: dict = payload.copy()
        
        # ====== # Removing values that user didn't specified # ====== #
        for key, value in payload.items():
            if (value == '' or value == 0):
                PayLoad.pop(key)

        # ======== # Checking requirement var # ======== #
        
        unsplash_api: str = f'https://api.unsplash.com/collections/{str(ID)}/photos'
        try:
            ResponseData: Response = get(unsplash_api, allow_redirects=True, timeout=25, params=PayLoad)
        except exceptions.ConnectionError:
            if(pass_errors == False):
                raise TypeError("Connection Failed. It's might because of your network connection")
            else:
                return("Connection Failed. It's might because of your network connection")
        except KeyboardInterrupt:
            if(pass_errors == False):
                raise TypeError('\nOperation canceled by user')
            else:
                return('\nOperation canceled by user')
        except exceptions.ReadTimeout:
            if(pass_errors == False):
                raise TypeError('Time out has reached')
            else:
                return('Time out has reached')
        
        # ======== # Checking for http errors # ======== #
        if(ResponseData.ok == False):
            if pass_errors == False:
                raise Exception(__check_http_error(ResponseData))
            else:
                pass
                return(__check_http_error(ResponseData))
        else:
            JsonImg: dict = ResponseData.json()
            
        # ======= # Download images# ======= #
        if(DownloadImg):
            print('Downloading images ...')
            if(UPath != str()):
                if(path.exists(UPath) == False):
                    exit(f'"{UPath}" is not exist')

                if(name == 'nt' and UPath.endswith('\\') == False):
                    UPath: str = UPath + '\\'
                elif(name == 'posix' and UPath.endswith('/') == False):
                    UPath: str = UPath + '/'
            for i in range(per_page):  # type: ignore
                ImgLink: str = JsonImg[i]['urls']['full']
                try:
                    urlretrieve(ImgLink, f"{UPath}{FileName}-{i}.jpg")
                except URLError:
                    exit('Error! It might be because of the network problem or your setting issues, such as proxy setting')
                except KeyboardInterrupt:
                    exit('\nOperation canceled by user')
        else:
            return JsonImg


    def get_collections_id(self, query: str, page: int = int(), per_page: int = int(), pass_errors: bool = False) -> list | str:
        '''You can search for collection and get the collection's id, Then you can use it in download_collection() func to download images
    | param | Description |
    ---|---|

    |`query` : | Search terms. |
    | `page`: |  The page number of the results to download. (Optional; default: 1) |
    | `per_page`:  |  The number of images to download per page. (Optional; default: 10) |
    | `_pass_errors` : | If there an error during the process. It won't break the program. It will just skip the process|'''
        
        payload: dict = {
            'client_id': self.client_id,
            'query':query,
            'page': page,
            'per_page':per_page}
        # ======== # Making copy to prevent RuntimeError: dictionary changed size during iteration # ======== #
        PayLoad: dict = payload.copy()

        # ====== # Removing values that user didn't specified # ====== #
        for key, value in payload.items():
            if (value == '' or value == 0):
                PayLoad.pop(key)
        
        unsplash_api: str = 'https://api.unsplash.com/search/collections'
        try:
            ResponseData: Response = get(unsplash_api, allow_redirects=True, timeout=25, params=PayLoad)
        except exceptions.ConnectionError:
            if(pass_errors == False):
                raise TypeError("Connection Failed. It's might because of your network connection")
            else:
                return("Connection Failed. It's might because of your network connection")
        except KeyboardInterrupt:
            if(pass_errors == False):
                raise TypeError('\nOperation canceled by user')
            else:
                return('\nOperation canceled by user')
        except exceptions.ReadTimeout:
            if(pass_errors == False):
                raise TypeError('Time out has reached')
            else:
                return('Time out has reached')

        # ======== # Checking for http errors # ======== #
        if(ResponseData.ok == False):
            if pass_errors == False:
                raise Exception(__check_http_error(ResponseData))
            else:
                pass
                return __check_http_error(ResponseData) # type: ignore
        else:
            JsonData: dict = ResponseData.json()
        
        # ======= # Returning collection id # ======= #
        id_list : list = list()
        for i in range(per_page):
            id_list.append(JsonData['results'][i]['id'])
        return(id_list)


    # ======= # Create a new collection. This requires the write_collections scope that can be activated on your api.unsplash.com account # ======= #
    def create_collection(self, title: str, description: str = str(), private: bool = False, pass_errors: bool = False) -> bool | str:
        '''Create a new collection. This requires the `write_collections` permission. Enable it on  Redirect URI & Permissions on your profile.
    return True if the operation was successful and return error message if operation was unsuccessful
    | param |	Description |
    ---|---|
    |`client_id`: |  Your Unsplash Access Key. |
    | `title`: |	The title of the collection. (Required.) |
    | `description`: | 	The collection's description. (Optional.) |
    | `private`: |	Whether to make this collection private. (Optional; default false). |
    | `_pass_errors`: | If there an error during the process. It won't break the program. It will just skip the process|
    '''
        payload: dict = {
            'client_id': self.client_id,
            'title': title,
            'description':description,
            'private': private}
        # ======== # Making copy to prevent RuntimeError: dictionary changed size during iteration # ======== #
        PayLoad: dict = payload.copy()

        # ====== # Removing values that user didn't specified # ====== #
        for key, value in payload.items():
            if (value == '' or value == 0):
                PayLoad.pop(key)
            
        unsplash_api: str = 'https://api.unsplash.com/collections'
        
        try:
            ResponseData: Response = post(unsplash_api, allow_redirects=True, timeout=25, params=PayLoad)
        except exceptions.ConnectionError:
            if(pass_errors == False):
                raise TypeError("Connection Failed. It's might because of your network connection")
            else:
                return("Connection Failed. It's might because of your network connection")    
        except KeyboardInterrupt:
            if(pass_errors == False):
                raise TypeError('\nOperation canceled by user')
            else:
                return('\nOperation canceled by user')
        except exceptions.ReadTimeout:
            if(pass_errors == False):
                raise TypeError('Time out has reached')
            else:
                return('Time out has reached')
        
        # ======== # Checking for http errors # ======== #
        if(ResponseData.ok == False):
            if pass_errors == False:
                raise Exception(__check_http_error(ResponseData))
            else:
                pass
                return(__check_http_error(ResponseData)) # type: ignore

        return True

    # ======== # Update an existing collection belonging to the logged-in user. This requires the write_collections scope. # ======== #
    def update_collection(self, ID, title: str = str(), description: str = str(), private: bool = False, pass_errors: bool = False) -> bool | str:
        '''Update an existing collection belonging to the logged-in user. This requires the write_collections permission. Enable it on  Redirect URI & Permissions on your profile.
    return True if the operation was successful and return error message if operation was unsuccessful
    | param |	Description |
    ---|---|
    | `ID` : | 	The collection's ID. Required. |
    | `title`:  |	The title of the collection. (Optional.) |
    | `description`: | 	The collection's description. (Optional.) |
    | `private`: |	Whether to make this collection private. (Optional; default false). |
    | `_pass_errors`:  |  If there an error during the process. It won't break the program. It will just skip the process|
        '''
        payload: dict = {
            'client_id': self.client_id,
            'title': title,
            'description':description,
            'private': private}
        # ======== # Making copy to prevent RuntimeError: dictionary changed size during iteration # ======== #
        PayLoad: dict = payload.copy()

        # ====== # Removing values that user didn't specified # ====== #
        for key, value in payload.items():
            if (value == '' or value == 0):
                PayLoad.pop(key)
            
        unsplash_api: str = f'https://api.unsplash.com/collections/{ID}'
        
        try:
            ResponseData: Response = put(unsplash_api, allow_redirects=True, timeout=25, params=PayLoad)
        except exceptions.ConnectionError:
            if(pass_errors == False):
                raise TypeError("Connection Failed. It's might because of your network connection")
            else:
                return("Connection Failed. It's might because of your network connection")
        except KeyboardInterrupt:
            if(pass_errors == False):
                raise TypeError('\nOperation canceled by user')
            else:
                return('\nOperation canceled by user')
        except exceptions.ReadTimeout:
            if(pass_errors == False):
                raise TypeError('Time out has reached')
            else:
                return('Time out has reached')
        
        # ======== # Checking for http errors # ======== #
        if(ResponseData.ok == False):
            if pass_errors == False:
                raise Exception(__check_http_error(ResponseData))
            else:
                pass
                return (__check_http_error(ResponseData)) # type: ignore
            
        return True

    # ======== # Delete a collection belonging to the logged-in user # ======== #
    def delete_collection(self, ID, pass_errors: bool = False) -> bool | str:
        '''Delete a collection belonging to the logged-in user. This requires the write_collections permission. Enable it on Redirect URI & Permissions on your profile.
    return True if the operation was successful and return error message if operation was unsuccessful
    | param | Description |
    ---|---|
    | `ID` : | 	The collection's ID. Required. |
    | `_pass_errors`:  |  If there an error during the process. It won't break the program. It will just skip the process|'''
            
        PayLoad: dict = {
            'client_id': self.client_id}
            
        unsplash_api: str = f'https://api.unsplash.com/collections/{ID}'
        
        try:
            ResponseData: Response = delete(unsplash_api, allow_redirects=True, params=PayLoad)
        except exceptions.ConnectionError:
            if(pass_errors == False):
                raise TypeError("Connection Failed. It's might because of your network connection")
            else:
                return("Connection Failed. It's might because of your network connection")
        except KeyboardInterrupt:
            if(pass_errors == False):
                raise TypeError('\nOperation canceled by user')
            else:
                return('\nOperation canceled by user')
        except exceptions.ReadTimeout:
            if(pass_errors == False):
                raise TypeError('Time out has reached')
            else:
                return('Time out has reached')
        
        if ResponseData.ok == False:
            if pass_errors == False:
                raise Exception(__check_http_error(ResponseData))
            else:
                pass
                return(__check_http_error(ResponseData)) #type: ignore
        
        return True

    # ======== # Add a photo to one of the logged-in user’s collections # ======== #
    def add_to_collection(self, collection_id, photo_id, pass_errors: bool = False) -> bool | str :
        '''Add a photo to one of the logged-in user's collections. Requires the write_collections permission. Enable it on Redirect URI & Permissions on your profile.
    returns True if the operation was successful and returns an error message if operation was unsuccessful.
    Note: If the photo is already in the collection, this action has no effect.
    | param | Description |
    ---|---|
    |`client_id`: |  Your Unsplash Access Key. |
    | `collection_id` : | The collection's ID. Required. |
    | `photo_id` : | The photo's ID that you want to add it. Required. |
    | `_pass_errors`:  |  If there an error during the process. It won't break the program. It will just skip the process|
        '''
        PayLoad: dict = {
            'client_id': self.client_id,
            'photo_id': photo_id,
            'collection_id' : collection_id
        }

        unsplash_api: str = f'https://api.unsplash.com/collections/{collection_id}/add' 
        
        # ======== # Sending requests to add the photo # ======== #
        try:
            ResponseData: Response = post(unsplash_api, allow_redirects=True, params=PayLoad)
        except exceptions.ConnectionError:
            if(pass_errors == False):
                raise TypeError("Connection Failed. It's might because of your network connection")
            else:
                return("Connection Failed. It's might because of your network connection")
        except KeyboardInterrupt:
            if(pass_errors == False):
                raise TypeError('\nOperation canceled by user')
            else:
                return('\nOperation canceled by user')
        except exceptions.ReadTimeout:
            if(pass_errors == False):
                raise TypeError('Time out has reached')
            else:
                return('Time out has reached')

        if (ResponseData.ok == False):
            if (pass_errors == False):
                raise Exception(__check_http_error(ResponseData))
            else:
                pass
                return(__check_http_error(ResponseData)) #type: ignore
            
        return True