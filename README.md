Here is everything in **plain text (no code blocks, no formatting distractions)**:

---

1. Create app
   Run: python manage.py startapp vazifa5

---

2. Update settings.py
   Open settings.py → find INSTALLED_APPS → add:
   rest_framework
   vazifa5

---

3. Create model (vazifa5/models.py)
   Create class Vazifa5 with fields:

* title → CharField (max_length=200)
* is_active → BooleanField (default=True)
* status → CharField with choices: yangi, jarayonda, tugadi (default='yangi')

Also add **str** method returning title

---

4. Run migrations
   Run:
   python manage.py makemigrations
   python manage.py migrate

---

5. Create serializer (vazifa5/serializers.py)
   Create ModelSerializer:

* model = Vazifa5
* fields = '**all**'

---

6. Create view (vazifa5/views.py)
   Create ModelViewSet:

* queryset = Vazifa5.objects.all()
* serializer_class = Vazifa5Serializer

---

7. Create urls inside app (vazifa5/urls.py)

* Import DefaultRouter
* Register Vazifa5ViewSet with route 'vazifa5'
* Include router.urls in urlpatterns

---

8. Connect main urls (project urls.py)
   Open main urls.py and add:
   path('vazifa5/', include('vazifa5.urls'))

---

9. Run server
   Run: python manage.py runserver

---

10. Open in browser
    Go to:
    [http://127.0.0.1:8000/vazifa5/vazifa5/](http://127.0.0.1:8000/vazifa5/vazifa5/)

---

Result:
You will get DRF page with:

* GET list
* POST form (title, is_active, status)
* Full CRUD working

