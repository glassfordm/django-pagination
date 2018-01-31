def get_page(self, suffix):
    """
    A function which will be monkeypatched onto the request to get the current
    integer representing the current page.
    """
    try:
        if self.method == 'POST':
            request = self.POST
        elif self.method == 'GET':
            request = self.GET
        else:
            request = None
        return int(request['page%s' % suffix])
    except (KeyError, ValueError, TypeError):
        return 1

class PaginationMiddleware(object):
    """
    Inserts a variable representing the current page onto the request object if
    it exists in either **GET** or **POST** portions of the request.
    """
    def process_request(self, request):
        request.__class__.page = get_page
