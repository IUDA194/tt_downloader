from django.shortcuts import render, HttpResponse
from api.tik_tok import TikTok_video


def tt_download(request):
    if request.method == "GET":
        url = request.GET.get("url")

        if url:
            if "tiktok" in url:
                TikTok = TikTok_video(url, "test").download()
                return HttpResponse("This is tik-tok")
            elif "youtube" in url:
                return HttpResponse("This is youtube")
            elif "instagram" in url:
                return HttpResponse("This is instagram")
            else: return HttpResponse("Url is bad")
        else: return HttpResponse("In get response shoud be a ulr for video")
    else:
        return HttpResponse("ERROR. THIS IS A GET REQUEST")