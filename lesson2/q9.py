# Modify the get_next_target procedure so that
# if there is a link it behaves as before, but
# if there is no link tag in the input string,
# it returns None, 0.

# Note that None is not a string and so should
# not be enclosed in quotes.

# Also note that your answer will appear in
# parentheses if you print it.

def get_next_target(page):
    start_link=page.find('<a href=')
    if start_link == -1:
        return None, 0
    start_quote=page.find('"', start_link)
    end_quote=page.find('"', start_quote+1)
    url=page[start_quote+1:end_quote]
    return url,end_quote

def print_all_links(page):
    while True:
        url, endpos=get_next_target(page)
        if url:
            print url
            page=page[endpos:]
            print page
        else:
            break

page='<a href="https://review.openstack.org/#/c/360388/">https://review.openstack.org/#/c/360388/</a>  about adding magnum deployment ...</p></p><p class="btn-read"><a href="/how-to-install-openstack-packstack-from-source-and-test-individual-patches-locally.html">Read more</a></p>'
print_all_links(page)
