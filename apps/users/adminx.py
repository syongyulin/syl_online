from .models import UserProfile,EmailVerifyRecord
import xadmin
from xadmin import views

class BaseSetting(object):
    enable_themes = True                #切换xadmin主题
    use_bootswatch = True               #切换主题，和enable_themes一起用。

class GlobalSettings(object):
#     设置网站标题和页面
    site_title='在线教育'               #设置页面标题
    site_footer="Powered By 1906c-2020" #设置页脚
    menu_style='accordion'              #设置菜单折叠

class UserProfileAdmin(object):
    list_display =['username','gender','mobile','address']
    search_fields=['username','gender','mobile','address']
    list_filter=['username','gender','mobile','address']
    model_icon='fa fa-user'             #设置图片，图片都在http://www.fontawesome.com.cn/
    style_fields = {"address": "ueditor"}
    ordering=['date_joined']   #排序
    readonly_fields=['nick_name']
    exclude=['gender']
    list_editable=['mobile']
    refresh_times=[3,5]

xadmin.site.unregister(UserProfile)
xadmin.site.register(UserProfile,UserProfileAdmin)
xadmin.site.register(views.CommAdminView,GlobalSettings)
xadmin.site.register(views.BaseAdminView,BaseSetting)