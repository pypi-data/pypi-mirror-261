# Unsplash Library

With this library you can download/upload/delete ... images with just one api key ✨

## Installation

For installation, run the following command ⬇️

```
pip install unsplash_lib
```

Having issue with pip?

## How can i get a unsplash api key?
- Well, at first you should make an [unsplash account](https://unsplash.com/join).
- After that, [create a new application](https://unsplash.com/oauth/applications/new) on the site.
- Then scroll down a bit and copy your Access Key.

## Usage
For importing ⬇️
```python
from unsplash_lib import Photos, Collection, Search
```
---
### Photos explanation
**First step**: make an instance
```python
Photos_instance = Photos('Your api key 🔑')
```
### 1 - random_photo

Download photos by search results.
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

### 2 - photos_statistics
Retrieve total number of downloads, views and likes of a single photo, as well as the historical breakdown of these stats in a specific timeframe (default is 30 days)
|param     |Description     |
---|---|
|`id`: | The public id of the photo. Required.|
|`resolution`:  |  The frequency of the stats. (Optional; default: “days”)|
|`quantity`: | The amount of for each stat. (Optional; default: 30)|'''

---
### Search Explanation


### Search_photo
**First step**: make an instance
```python
Photos_instance = Search('Your api key 🔑')
```
### 1 - search_photo
Download photos by search results.

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

### 2 - search_users

Search for a user and getting back the results as list that contain a dictionary.
    If the operation was successful, returns a list with dictionary inside that contain search info. Raise the error message if the operation was unsuccessful.

| param | Description|
---|---|
| `query` : |	Search terms.|
| `page` : | The page number of the results to download. (Optional; default: 1)
| `per_page` : | The number of images to download per page.  (Optional; default: 10)
| `_pass_errors` : | If there an error during the process. It won't break the program. It will just skip the process|

---

### Collection Explanation
**First step**: make an instance
```python
Photos_instance = Collection('Your api key 🔑')
``` 

### 1 - download_collection
Download a collection's photos.
| param | Description |
---|---|
| `ID` : | 	The collection's ID. Required. |
| `page` : | Page number to retrieve. (Optional; default: 1) |
| `per_page` : | Number of items per page. (Optional; default: 10) | 
| `orientation` : | Filter by photo orientation. Optional. (Valid values: landscape, portrait, squarish) |
| `DownloadImg`: |  A boolean value indicating whether to download the images. |
| `FileName`: |  The name of the file to save the images to. |
| `UPath`: |  The path to the directory to save the images to. |
| `_pass_errors` : | If there an error during the process. It won't break the program. It will just skip the process|

### 2 - get_collections_id
You can search for collection and get the collection's id, Then you can use it in download_collection() func to download images.
| param | Description |
---|---|
|`query` : | Search terms. |
| `page`: |  The page number of the results to download. (Optional; default: 1) |
| `per_page`:  |  The number of images to download per page. (Optional; default: 10) |
| `_pass_errors` : | If there an error during the process. It won't break the program. It will just skip the process|

### 3 - create_collection
Create a new collection. This requires the `write_collections` permission. Enable it on  Redirect URI & Permissions on your profile.

return True if the operation was successful and return error message if operation was unsuccessful
| param |	Description |
---|---|
|`client_id`: |  Your Unsplash Access Key. |
| `title`: |	The title of the collection. (Required.) |
| `description`: | 	The collection's description. (Optional.) |
| `private`: |	Whether to make this collection private. (Optional; default false). |
| `_pass_errors`: | If there an error during the process. It won't break the program. It will just skip the process|

### 4 - update_collection
Update an existing collection belonging to the logged-in user. This requires the write_collections permission. Enable it on  Redirect URI & Permissions on your profile.

return True if the operation was successful and return error message if operation was unsuccessful
| param |	Description |
---|---|
| `ID` : | 	The collection's ID. Required. |
| `title`:  |	The title of the collection. (Optional.) |
| `description`: | 	The collection's description. (Optional.) |
| `private`: |	Whether to make this collection private. (Optional; default false). |
| `_pass_errors`:  |  If there an error during the process. It won't break the program. It will just skip the process|

### 4 -  delete_collection
Delete a collection belonging to the logged-in user. This requires the write_collections permission. Enable it on Redirect URI & Permissions on your profile.

return True if the operation was successful and return error message if operation was unsuccessful
| param | Description |
---|---|
| `ID` : | 	The collection's ID. Required. |
| `_pass_errors`:  |  If there an error during the process. It won't break the program. It will just skip the process|

### 5 - add_to_collection
Add a photo to one of the logged-in user's collections. Requires the write_collections permission. Enable it on Redirect URI & Permissions on your profile.

returns True if the operation was successful and returns an error message if operation was unsuccessful.
Note: If the photo is already in the collection, this action has no effect.
| param | Description |
---|---|
|`client_id`: |  Your Unsplash Access Key. |
| `collection_id` : | The collection's ID. Required. |
| `photo_id` : | The photo's ID that you want to add it. Required. |
| `_pass_errors`:  |  If there an error during the process. It won't break the program. It will just skip the process|
    