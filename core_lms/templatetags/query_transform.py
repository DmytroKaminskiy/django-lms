from django import template

register = template.Library()


# {% query_transform_tag page=page_num.previous_page_number %}
@register.simple_tag(takes_context=True)
def query_transform_tag(context, **kwargs):
    query = context['request'].GET.copy()

    for k, v in kwargs.items():
        query[k] = v
    return query.urlencode()
