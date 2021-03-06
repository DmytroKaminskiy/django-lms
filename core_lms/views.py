from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.views.decorators.cache import cache_page


@cache_page(60 * 15)  # 60 * 15 == 15 min
def index(request):
    return render(request, 'index.html')


class EditView(object):
    model = None
    success_url = None
    form = None
    template_name = None

    def update_instance(self, request, id):
        instance = get_object_or_404(self.model, pk=id)

        if request.method == 'POST':
            form = self.form(request.POST, instance=instance)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(
                    self.get_success_url(instance)
                )
        else:
            form = self.form(instance=instance)

        return render(
            request, self.template_name,
            self.get_context(
                {
                    'form': form,
                    'instance': instance
                }
            ))

    def get_success_url(self, instance):
        return reverse(self.success_url)

    def get_context(self, context):
        return context
