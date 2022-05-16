# I tried to make thing done by backend and do not depends on frontend like use localStorage.. to try make more things in backend position
# Filter will apply on each page separately

def sortFliter(model, sort, country):

    if int(sort[0]) == 2 and country != ['']:
        sort_values = model.objects.values(
            'id', 'title', 'image', 'details', 'published_date').filter(country__in=country).order_by('published_date')

    elif int(sort[0]) == 2 and country == ['']:
        sort_values = model.objects.values(
            'id', 'title', 'image', 'details', 'published_date').order_by('-published_date')

    elif int(sort[0]) == 1 and country != ['']:
        sort_values = model.objects.values(
            'id', 'title', 'image', 'details', 'published_date').filter(country__in=country)

    elif int(sort[0]) == 1 and country == ['']:
        sort_values = model.objects.values(
            'id', 'title', 'image', 'details', 'published_date')
    else:
        sort_values = model.objects.values(
            'id', 'title', 'image', 'details', 'published_date')

    return sort_values
