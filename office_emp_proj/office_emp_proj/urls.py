"""from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Include admin URLs
    path('admin/', admin.site.urls),

    # Include URLs from the emp_app
    path('emp/',include('emp_app.urls'))

]"""
from django.contrib import admin
from django.urls import path, include
from emp_app import views  # Import views from your emp_app

urlpatterns = [
    path('', views.index, name='index'),  # Define the view for the root URL
    path('admin/', admin.site.urls),
    path('emp/', include('emp_app.urls')), 
    path('view_emp', views.view_emp, name='view_emp'),
    path('add_emp', views.add_emp, name='add_emp'),
    path('rem_emp', views.rem_emp, name='rem_emp'),
    path('rem_emp/<int:emp_id>', views.rem_emp, name='rem_emp'),
    path('filt_emp', views.filt_emp, name='filt_emp'), # Include URLs from the emp_app
]
