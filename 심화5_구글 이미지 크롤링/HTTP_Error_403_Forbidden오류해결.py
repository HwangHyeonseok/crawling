    # HTTP Error 403: Forbidden ���� �ذ��� ���� �ڵ� ("�� ��� �ƴϰ� ����̾�!")
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-Agent', 'Mozila/5.0')]
    urllib.request.install_opener(opener)