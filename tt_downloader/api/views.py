from django.shortcuts import render, HttpResponse
from django.http import FileResponse
from api.tik_tok import TikTok_video
from api.youtube import short
import os


def tt_download(request):
    if request.method == "GET":
        url = request.GET.get("url")

        if url:
            if "tiktok" in url:
                TikTok = TikTok_video(url, "1")
                TikTok.download()
                with open(TikTok.path, 'rb') as file:
                    response = HttpResponse(file.read(), content_type='application/octet-stream')
                    response['Content-Disposition'] = f'attachment; filename="{file.name}"'
                    return response
            elif "youtube" in url:
                Short = short(url, "1")
                Short.download()
                with open(Short.path, 'rb') as file:
                    response = HttpResponse(file.read(), content_type='application/octet-stream')
                    response['Content-Disposition'] = f'attachment; filename="{file.name}"'
                    return response
                return HttpResponse("This is youtube")
            elif "instagram" in url:
                return HttpResponse("This is instagram")
            else: return HttpResponse("Url is bad")
        else: return HttpResponse("In get response shoud be a ulr for video")
    else:
        return HttpResponse("ERROR. THIS IS A GET REQUEST")