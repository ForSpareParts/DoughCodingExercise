from rest_framework import filters


# snippet below from ember-django-adapter documentation
# enables coalescing find requests in Django REST Framework
#
# http://dustinfarris.com/ember-django-adapter/coalesce-find-requests/
class CoalesceFilterBackend(filters.BaseFilterBackend):
    """
    Support Ember Data coalesceFindRequests.

    """
    def filter_queryset(self, request, queryset, view):
        id_list = request.QUERY_PARAMS.getlist('ids[]')
        if id_list:
            queryset = queryset.filter(id__in=id_list)
        return queryset
