LÀM LÀ PHẢI MỞ TỚI COURSEAPP luôn không mở ở backeddjango

Trong thằng này phải bật cmd pip install django python.exe -m pip install --upgrade pip django-admin startproject courseapp cd courseapp Khai báo app mới trong settings

django-admin startapp courses pip install pymysql

Kết nối database

Tạo models python manage.py makemigrations python manage.py migrate

thêm AUTH_USER_MODEL = 'courses.User'

thử tác động:

python manage.py shell

from courses.models import *

Category.objects.create(name="A") exit()

python manage.py createsuperuser thêm admin

from .models import Category admin.site.register(Category)

thêm MEDIA_ROOT = '%s/courses/static/' % BASE_DIR -> nữa nhớ sửa trên app

pip install Pillow

#Dùng show ảnh from django.utils.html import mark_safe

 readonly_fields = ['img']

def img(self, course):
    if course:
        return mark_safe(
            '<img src="/static/{url}" width="120" />' \
                .format(url=course.image.name)
        )
#Rich text pip install django-ckeditor

khai bao trong app 'ckeditor', 'ckeditor_uploader' nơi upload -> settings CKEDITOR_UPLOAD_PATH = "ckeditor/images/"

qua urls -> projects

from django.urls import re_path ,include re_path(r'^ckeditor/',include('ckeditor_uploader.urls')),

qua models thêm from ckeditor.fields import RichTextField

upload -> ben admin

from django import forms from ckeditor_uploader.widgets
import CKEditorUploadingWidget

Inline này dùng cho 2N2
pip install django-ckeditor-5

Trong trang Lesson sẽ có cả Tag

Inline này dùng cho 2N2 giữa Lesson và Tag
class LessonAdmin(admin.ModelAdmin): form = LessonForm inlines = ['LessonTagInlineAdmin' ]

class LessonTagInlineAdmin(admin.TabularInline): model = Lesson.tags.through

class TagAdmin(admin.ModelAdmin): inlines = [LessonTagInlineAdmin, ]

pip install django-debug-toolbar khai báo trong setting app

'debug_toolbar'

from debug_toolbar.toolbar import debug_toolbar_urls urlpatterns = [ # ... the rest of your URLconf goes here ... ] + debug_toolbar_urls()

thêm trong midleware "debug_toolbar.middleware.DebugToolbarMiddleware"

INTERNAL_IPS = [ # ... "127.0.0.1", # ... ]

tạo dao.py python manage.py shell from courses.models import *

->Lấy tất cả bài học thuộc danh mục 1 c= Category.objects.get(pk=1) c.courses_set.all()

values là các trường dữ liệu mà mình muốn lấy

Lessons = Lesson.objects.values('id', 'subject','course__subject').filter(active=True) print(lessons) <QuerySet [{'id': 1, 'subject': 'Giới thiệu', 'course__subject': 'Các công nghệ lập trình hiện đại'}]>

bấm nút lên nó sẽ chạy lại các lệnh cũ pip install cryptography

đếm số bài học (lesson) cả khóa học c = Course.objects.annotate(Count('my_lesson')) print(c[0].my_lesson__count)

related_query_name thêm vào khóa ngoại ở bảng kia để bảng còn lại thế truy vấn ngược

ví dụ : Course có khóa ngoại category = ...... related_query_name ='course' để course có thể có trường course__id có thể lấy cả course__name="ABC"

Thuộc tính Mục đích Sử dụng related_name Đặt tên cho liên kết ngược (reverse relation) từ model liên quan. Truy cập liên kết ngược: category.courses.all() related_query_name Đặt tên cho liên kết truy vấn filter (trong các querysets). Truy vấn filter: Category.objects.filter(course__name="Python")

Đi tạo adminsite để có thể thay đổi tiêu đề admin .....

ở bên admin class CourseAppAdminSite(admin.AdminSite): site_header = 'iSuccess' admin_site =CourseAppAdminSite(name='TheAnh_App')

roi sửa thành : admin_site hết

admin_site.register(Category,CategoryAdmin) admin_site.register(Course,CourseAdmin) admin_site.register(Lesson,LessonAdmin) admin_site.register(Tag,TagAdmin)

rồi urls projects thêm from courseapp.courses.admin import admin_site path('admin/', admin_site.site.urls),

thêm vào để trả về templates def stats_view(self, request): return TemplateResponse(request,'admin/stats.html')

rồi bổ sung các phương thức

class CourseAppAdminSite(admin.AdminSite): site_header = 'AdminTheAnh' # Bổ sung thêm method này để có thể thêm view cho admin def get_urls(self): return [ path('course-stats/', self.stats_view) ] + super().get_urls() def stats_view(self, request): return TemplateResponse(request, 'admin/stats.html')

Stats

arrow function window.onload() => { bỏ nguyê các chart.js vào}

const obj = { name: "Arrow Function", arrowMethod: () => { console.log(this.name); // undefined (kế thừa this từ phạm vi global - window) }, functionMethod: function () { console.log(this.name); // Arrow Function (trỏ tới obj) }, };

obj.arrowMethod(); obj.functionMethod();

function OuterFunction() { this.value = 42;

const innerArrow = () => {
    console.log(this.value); // 42 (kế thừa từ OuterFunction)
};

function innerFunction() {
    console.log(this.value); // undefined (this trỏ tới global object trong strict mode)
}

innerArrow();
innerFunction();
}

new OuterFunction();

const button = document.querySelector("button");

// Arrow function button.addEventListener("click", () => { console.log(this); // window });

// Regular function button.addEventListener("click", function () { console.log(this); // (trỏ tới phần tử DOM đã kích hoạt sự kiện) });

Các sự kiên window.load thì nên xài arroww func giúp truy vấn nhanh vì không pơhiar tương tác với cây DOM ảo

Làm restful pip install djangorestframework

Xong rồi tạo serializers.py -> chỉ lại setting cho venv

rồi bổ sung thêm bên views.py

Serializers là gì? Serializers giúp:
Chuyển đổi dữ liệu phức tạp (ví dụ, QuerySet của Django) sang các định dạng dễ sử dụng (như JSON hoặc XML). Xác thực dữ liệu đầu vào trước khi lưu vào cơ sở dữ liệu. Tạo hoặc cập nhật đối tượng từ dữ liệu đã xác thực.

Tạo urls bên app và thêm qua bên projects

path('' , include('courses.urls')),

cài bên urls xong rồi vào settings thêm install app mới

pip install drf-yasg

install app 'drf_yasg',

cập nhật trong urls projects from rest_framework import permissions from drf_yasg.views import get_schema_view from drf_yasg import openapi schema_view = get_schema_view( openapi.Info( title="Course API", default_version='v1', description="APIs for CourseApp", contact=openapi.Contact(email="thanh.dh@ou.edu.vn"), license=openapi.License(name="Dương Hữu Thành@2021"), ), public=True, permission_classes=(permissions.AllowAny,),

Trong Django, path, re_path, và include là các công cụ được sử dụng để định tuyến (routing) URL đến các views. Dưới đây là chi tiết về chúng, cũng như sự khác nhau giữa path, re_path, và include.

path là gì? path là hàm định tuyến đơn giản, được giới thiệu từ Django 2.0, sử dụng cú pháp định tuyến URL dễ đọc hơn. Nó không dùng biểu thức chính quy (regex), mà dựa trên cú pháp trực quan để mô tả các URL patterns.
Cách sử dụng path:

python Sao chép mã from django.urls import path from . import views

urlpatterns = [ path('home/', views.home, name='home'), # URL: /home/ path('post/int:id/', views.post_detail, name='post_detail'), # URL với tham số ] Ưu điểm: Dễ sử dụng, không cần kiến thức về regex. Nhược điểm: Không đủ mạnh để xử lý các mẫu URL phức tạp (ví dụ: những mẫu yêu cầu biểu thức chính quy). 2. re_path là gì? re_path (regex path) là một phiên bản cũ hơn và mạnh mẽ hơn của path, cho phép sử dụng biểu thức chính quy (regex) để định nghĩa URL patterns. Điều này rất hữu ích khi bạn cần kiểm soát chặt chẽ cách URL được xử lý.

Cách sử dụng re_path:

python Sao chép mã from django.urls import re_path from . import views

urlpatterns = [ re_path(r'^home/$', views.home, name='home'), # URL: /home/ re_path(r'^post/(?P\d+)/$', views.post_detail, name='post_detail'), # URL với tham số ] Ưu điểm: Có thể xử lý các mẫu URL phức tạp. Nhược điểm: Biểu thức chính quy khó đọc và viết. So sánh path và re_path Đặc điểm path re_path Dễ đọc, dễ viết Rất dễ đọc và viết Khó đọc hơn do sử dụng regex Hỗ trợ regex Không Có hỗ trợ regex Hiệu suất Nhanh hơn (do không cần phân tích regex) Chậm hơn một chút do phải phân tích regex Trường hợp sử dụng URL đơn giản, không cần regex phức tạp URL phức tạp yêu cầu regex 3. include là gì? include được sử dụng để gộp nhiều file urls.py nhỏ hơn vào một file chính, giúp tổ chức và quản lý URL patterns dễ dàng hơn, đặc biệt trong các dự án lớn với nhiều ứng dụng.

Cách sử dụng include:

python Sao chép mã from django.urls import path, include

urlpatterns = [ path('blog/', include('blog.urls')), # Gộp các URL của app blog vào đây path('shop/', include('shop.urls')), # Gộp các URL của app shop vào đây ] Khi sử dụng include, Django sẽ chuyển hướng tất cả các URL bắt đầu bằng blog/ sang tệp urls.py trong app blog. Tệp blog/urls.py: python Sao chép mã from django.urls import path from . import views

urlpatterns = [ path('', views.index, name='index'), # URL: /blog/ path('int:id/', views.detail, name='detail'), # URL: /blog// ] So sánh path, re_path, và include Đặc điểm path re_path include Mục đích chính Định nghĩa URL đơn giản Định nghĩa URL phức tạp Gộp URL của các app khác Cú pháp dễ hiểu Rất dễ hiểu Cần hiểu regex Không liên quan đến định nghĩa URL Ứng dụng thực tế URL thông thường (CRUD, routes cơ bản) URL yêu cầu regex phức tạp Tổ chức URL trong dự án lớn 4. Khi nào nên dùng? path: Sử dụng cho hầu hết các URL thông thường trong Django (CRUD, routes thông thường). re_path: Chỉ sử dụng khi bạn cần URL phức tạp và yêu cầu regex. include: Sử dụng để tổ chức và gộp các file urls.py trong dự án lớn với nhiều app.

Sau khi chạy xong vào api/swagger

Quy trình tạo API -> tạo ser -> tạo view ->vafoo urls đăng ky APi (nếu đó là API mới)

pip install cloudinary

them pip install django-oauth-toolkit 'oauth2_provider',

#Chung thuc REST_FRAMEWORK = { 'DEFAULT_AUTHENTICATION_CLASSES': ( 'oauth2_provider.contrib.rest_framework.OAuth2Authentication', ) } url project path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),

python manage.py migrate oauth2_provider

xong rồi vào http://127.0.0.1:8000/o/applications/ -> nhớ copy key trước khi bấm save nếu không nó bị băm ra

JhHd3S0AhDhK4pmZZ8Tdy0GWs4TRxXvUEMiSf608

Ams4KVNEUZG8WpRwKM7Ok8C2a0FsCQChu0M7nzw1kgNaaAsYPvkPI7ax5crp6CwRtN6HbY9c3AIMa7EgUuZBUQKKdfrg1X2EbnquldVri6qJKQbDFnrSDbxzlPXaG8GH

lấy đc token

"access_token": "9Lb6DbYPXkU7aLCq1rL1Xop7SZ8Ov9",
"expires_in": 36000,
"token_type": "Bearer",
"scope": "read write",
"refresh_token": "BRRb3f6CW9cqUCF4mc8xxQzItHVPUs"
Tạo file perms để tự định nghĩa các hàm permission của mình -> chứng thực quyền người dùng -> dùng trước khi xóa

phải thêm cor
