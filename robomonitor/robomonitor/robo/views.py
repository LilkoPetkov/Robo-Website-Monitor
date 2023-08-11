from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from .dns_check import DNS
from .forms import RegisterForm, UserLoginForm, DNSCheckForm, WebsiteCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import get_user_model as gum
from .models import Profile, Websites, Logs
from django.contrib.auth.decorators import login_required
from .tables import LogsTable


class IndexView(LoginRequiredMixin, views.ListView):
    template_name = "app/index.html"
    model = gum()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["websites"] = Websites.objects.filter(user=self.request.user.pk)

        return context


class UserCreateView(views.CreateView):
    template_name = "app/user_create.html"
    form_class = RegisterForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        profile = Profile(user_name="Username", first_name="First Name", last_name="Last Name",
                          profile_picture="https://media.istockphoto.com/id/1332100919/vector/man-icon-black-icon-person-symbol"
                                          ".jpg?s=612x612&w=0&k=20&c=AVVJkvxQQCuBhawHrUhDRTCeNQ3Jgt0K1tXjJsFy1eg=",
                          user=self.request.user)
        profile.save()

        return result


class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = "app/user_login.html"


class UserLogoutView(LoginRequiredMixin, LogoutView):
    pass


class ProfileUpdateView(LoginRequiredMixin, views.UpdateView):
    model = Profile
    fields = ["user_name", "first_name", "last_name", "profile_picture"]
    template_name = "app/user_update.html"
    success_url = reverse_lazy("websites")


@login_required
def WebsitesView(request):
    user_websites = Websites.objects.filter(user=request.user.pk)

    if request.method == "POST" and "review" in request.POST:
        redirect("websites/verify/<int:pk>/")

    context = {
        "websites": user_websites,
    }

    return render(request, "app/websites.html", context=context)


@login_required
def dns_check_page(request, pk):
    form = DNSCheckForm(request.POST or None)
    domain = Websites.objects.get(pk=pk)

    if form.is_valid():
        D = DNS(domain)
        D.get_website()
        D.record_check()

        return redirect(f"http://127.0.0.1:8000/websites/review/{pk}")

    context = {
        "form": form,
        "domain": domain,
    }

    return render(request, "app/verification-page.html", context=context)


class WebsiteCreateView(LoginRequiredMixin, views.CreateView):
    template_name = "app/create_website.html"
    form_class = WebsiteCreationForm

    def form_valid(self, form):
        obj = form.save(commit=False)

        domain = obj.domain
        exists = Websites.objects.filter(domain=domain)

        if exists:
            messages.error(self.request, f'{domain} is already added in our system.')
            return redirect("website create")
        else:
            D = DNS(domain)

            obj.verification_record = D.generate_record()
            obj.user_id = self.request.user.id
            obj.verification_status = "NOT VERIFIED"
            obj.save()

            return redirect("websites")


class WebsiteUpdateView(LoginRequiredMixin, views.UpdateView):
    model = Websites
    template_name = "app/websites_update.html"
    fields = ["domain", "checker_rate"]
    success_url = reverse_lazy("websites")


class WebsiteDeleteView(LoginRequiredMixin, views.DeleteView):
    model = Websites
    success_url = reverse_lazy("websites")

    template_name = "app/websites-delete.html"


def logs_page(request, pk):
    logs = Logs.objects.filter(website=pk)
    table = LogsTable(logs)
    page = request.GET.get("page", 1)
    table.paginate(page=page, per_page=6)

    context = {
        "logs": logs,
        "table": table,
    }

    return render(request, "app/logs.html", context)


def four_o_four(request):
    if request.method == ("POST" or None):
        return redirect("index")

    return render(request, "app/404.html")


def error_404_view(request, exception=None):
    return redirect('four_o_four')
