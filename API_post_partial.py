from functools import partial

def form_request(url, method='GET', headers=None, data=None, params=None):
    dict_ = {"headers": headers,
           "data": data,
           "params": params}
    return f"{url}-::-{method}-::-{dict_}"


form_post_request = partial(form_request, method='POST')