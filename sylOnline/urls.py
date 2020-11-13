"""sylOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,include,re_path

from django.views.generic import TemplateView

from apps.users.views import LoginView,RegisterView,ActiveUserView,ForgetPwdView,ModifyPwdView,ResetView
import xadmin

from django.views.static import serve
from sylOnline.settings import MEDIA_ROOT

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('login/',LoginView.as_view(),name = 'login'),
    # 文件
    path('media/<path:path>',serve,{'document_root':MEDIA_ROOT}),
    path('ueditor/',include('DjangoUeditor.urls')),

    path('register/',RegisterView.as_view(),name='register'),
    path('captcha/',include('captcha.urls')),
    re_path('active/(?P<active_code>.*)/',ActiveUserView.as_view(),name='user_active'),
    path('forget/',ForgetPwdView.as_view(),name='forget_pwd'),
    re_path('reset/(?P<active_code>.*)/', ResetView.as_view(), name='reset_pwd'),
    path('modify_pwd/', ModifyPwdView.as_view(), name='modify_pwd'),
    path('org/', include('organization.urls', namespace="org")),
#     处理图片的url，使用django自带serve，传入参数告诉它去哪个路径找，我们有配置好的MEDIAROOT
    re_path(r'^media/(?P<path>.*)',serve,{'document_root':MEDIA_ROOT}),
    path("course/",include('course.urls',namespace="course")),
]
