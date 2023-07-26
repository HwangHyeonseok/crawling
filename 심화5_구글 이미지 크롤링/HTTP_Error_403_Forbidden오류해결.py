    # HTTP Error 403: Forbidden 에러 해결을 위한 코드 ("나 기계 아니고 사람이야!")
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent', 'Mozila/5.0')]
    urllib.request.install_opener(opener)