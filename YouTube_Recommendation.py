from youtubesearchpython import *

videosSearch = VideosSearch('MachineLearning', limit = 2)

result = videosSearch.result()
# print(result['result'][0].keys())
# print(result['result'][0].values())
# print(result['result'][0]['link'])

customSearch = CustomSearch('Machine Learning',VideoSortOrder.viewCount,10,'en','US')

for i in range(0,10):
    video_desc = ""
    print(f"Title - {customSearch.result()['result'][i]['title']}")
    print(f"Duration - {customSearch.result()['result'][i]['duration']}")
    print(f"ViewCount - {customSearch.result()['result'][i]['viewCount']['text']}")
    for j in range(0,len(customSearch.result()['result'][i]['descriptionSnippet'])):
        video_desc = video_desc + customSearch.result()['result'][i]['descriptionSnippet'][j]['text']
    print(f"Video desc - {video_desc}")
    print(f"Link - {customSearch.result()['result'][i]['link']}\n")