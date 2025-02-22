from django.urls import path,include
from django.conf.urls.static import static
from .views import *  # Ensure you import views from your app
from django.conf import settings
from rest_framework.routers import SimpleRouter

router = SimpleRouter()


router.register(r'banners', BannerViewSet, basename='banners')
router.register(r'college-updates',CollegeUpdatesViewSet,basename='college-updates')
router.register(r'student-counts',StudentsCountViewSet,basename='student-counts')
router.register(r'faculty-counts',FactulyCountViewSet,basename='faculty-counts')
router.register(r'programs-counts',ProgramsCountViewSet,basename='programs-counts')
router.register(r'ImportantSites',ImportantSitesViewSet,basename='ImportantSites')
router.register(r'student-form',StudentFormViewSet,basename='student-form')
router.register(r'syllabus',SyllabusViewSet,basename='syllabus')
router.register(r'alumni',AlumniViewSet,basename='alumni')
router.register(r'LibraryInfo',LibraryInfoViewSet,basename='LibraryInfo')
router.register(r'Library_Books',Library_BooksViewSet,basename='Library_Books')
router.register(r'committees',CommitteesViewSet,basename='committees')
router.register(r'Mba_Faculty_Images',Mba_Faculty_ImagesViewSet,basename='Mba_Faculty_Images')
router.register(r'faculty-mba',Faculty_MbaViewSet,basename='faculty-mba')
router.register(r'faculty-pharmacy',Faculty_PharamacyViewSet,basename='faculty-pharmacy')
router.register(r'Course_Admissions',Course_AdmissionsViewSet,basename='Course_Admissions')
router.register(r'gallery-images',GalleryImagesViewSet,basename='gallery-images')
router.register(r'gallery-videos',GalleryVideosViewSet,basename='gallery-videos')
router.register(r'eventsandactivites',EventsandActivitesViewSet,basename='eventsandactivites')


urlpatterns = [
    path('', include(router.urls)),
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),

    path('Home_Page/banners/',banner_list, name='banner_list'),
    path('Home_Page/banners/add/', banner_add, name='banner_add'),
    path('Home_Page/banners/edit/<int:pk>/', banner_edit, name='banner_edit'),
    path('Home_Page/banners/delete/<int:pk>/', banner_delete, name='banner_delete'),

    path('Home_Page/college-updates/', college_update_list_view, name='college_update_list'),
    path('Home_Page/college-updates/new/', college_update_create_view, name='college_update_create'),
    path('Home_Page/college-updates/edit/<int:id>/', college_update_edit_view, name='college_update_edit'),
    path('Home_Page/college-updates/delete/<int:id>/',college_update_delete_view, name='college_update_delete'),

    path('Home_Page/student-counts/', student_count_list_view, name='student_count_list'),
    path('Home_Page/student-counts/create/', student_count_create_view, name='student_count_create'),
    path('Home_Page/student-counts/<int:id>/edit/', student_count_edit_view, name='student_count_edit'),
    path('Home_Page/student-counts/<int:id>/delete/', student_count_delete_view, name='student_count_delete'),
    
    path('Home_Page/faculty-counts/', faculty_count_list_view, name='faculty_count_list'),
    path('Home_Page/faculty-counts/create/', faculty_count_create_view, name='faculty_count_create'),
    path('Home_Page/faculty-counts/<int:id>/edit/', faculty_count_edit_view, name='faculty_count_edit'),
    path('Home_Page/faculty-counts/<int:id>/delete/', faculty_count_delete_view, name='faculty_count_delete'),
    
    path('Home_Page/programs-counts/', programs_count_list_view, name='programs_count_list'),
    path('Home_Page/programs-counts/create/', programs_count_create_view, name='programs_count_create'),
    path('Home_Page/programs-counts/<int:id>/edit/', programs_count_edit_view, name='programs_count_edit'),
    path('Home_Page/programs-counts/<int:id>/delete/', programs_count_delete_view, name='programs_count_delete'),
    
    path('Home_Page/important_sites/', important_sites_list_view, name='important_sites_list'),
    path('Home_Page/important_sites/create/', important_sites_create_view, name='important_sites_create'),
    path('Home_Page/important_sites/<int:id>/edit/', important_sites_update_view, name='important_sites_update'),
    path('Home_Page/important_sites/<int:id>/delete/', important_sites_delete_view, name='important_sites_delete'),

    path('send-form/',send_form_email,name='sendform'),
    path('Home_Page/student-forms/', student_form_list_view, name='student_form_list'),
    path('Home_Page/student_forms/<int:pk>/delete/', student_form_delete_view, name='student_form_delete'),
    
    path('syllabusupload/', syllabus_view, name='syllabus_file_upload'),
    path('syllabusfiles/', syllabus_list_view, name='syllabus_list'),
    path('syllabusfiles/<int:pk>/edit/', syllabus_update_view, name='syllabus_file_update'),
    path('syllabusfiles/<int:pk>/delete/', syllabus_delete_view, name='syllabus_file_delete'),

    path('alumni_list/', alumni_list, name='alumni_list'),
    path('alumni_create/', alumni_create, name='alumni_create'),
    path('alumni_edit/<int:pk>/', alumni_edit, name='alumni_edit'),
    path('alumni_delete/<int:pk>/', alumni_delete, name='alumni_delete'),
    
    path('libarayinfo/', librayinfo_list_view, name='libraryinfo_list'),
    path('libarayinfo_create/', libraryinfo_create_view, name='libraryinfo_create'),
    path('libarayinfo_edit/<int:id>/', libraryinfo_edit_view, name='libraryinfo_edit'),
    path('libraryinfo_delete/<int:id>/', libraryinfo_delete_view, name='libraryinfo_delete'),
    
    path('librarybooks/', libraybooks_list_view, name='librarybooks_list'),
    path('librarybooks_create/', libraybooks_create_view, name='librarybooks_create'),
    path('librarybooks_edit/<int:id>/', libraybooks_edit_view, name='librarybooks_edit'),
    path('librarybooks_delete/<int:id>/', libraybooks_delete_view, name='librarybooks_delete'),
    
    path('upload/', committees_view, name='committees_file_upload'),
    path('files/', committees_list_view, name='committees_list'),
    path('files/<int:pk>/edit/', committees_update_view, name='committees_file_update'),
    path('files/<int:pk>/delete/', committees_delete_view, name='committees_file_delete'),
    
    path('faculty/mba_Images/', mba_faculty_Images_list_view, name='mba_faculty_Images_list'),
    path('faculty/mba_Images/add/', mba_faculty_Images_create_view, name='mba_faculty_Images_create'),
    path('faculty/mba_Images/edit/<int:id>/', mba_faculty_Images_edit_view, name='mba_faculty_Images_edit'),
    path('faculty/mba_Images/delete/<int:id>/',mba_faculty_Images_delete_view, name='mba_faculty_Images_delete'),
    
    path('faculty/mba/', faculty_mba_list_view, name='faculty_mba_list'),
    path('faculty/mba/add/', faculty_mba_create_view, name='faculty_mba_create'),
    path('faculty/mba/bulk-upload/', bulk_upload_mba_faculty, name='bulk_upload_mba_faculty'),
    path('faculty/mba/edit/<int:id>/', faculty_mba_edit_view, name='faculty_mba_edit'),
    path('faculty/mba/delete/<int:id>/',faculty_mba_delete_view, name='faculty_mba_delete'),

    # URLs for Faculty_Pharamacy
    path('faculty/pharmacy/', faculty_pharmacy_list_view, name='faculty_pharmacy_list'),
    path('faculty/pharmacy/add/', faculty_pharmacy_create_view, name='faculty_pharmacy_create'),
    path('faculty/pharamacy/bulk-upload/', bulk_upload_pharamacy_faculty, name='bulk_upload_pharamcy_faculty'),
    path('faculty/pharmacy/edit/<int:id>/', faculty_pharmacy_edit_view, name='faculty_pharmacy_edit'),
    path('faculty/pharmacy/delete/<int:id>/',faculty_pharmacy_delete_view, name='faculty_pharmacy_delete'),
    
    path('course_Admissions/', course_Admissions_list_view, name='course_Admissions_list'),
    path('course_Admissions/add/', course_Admissions_create_view, name='course_Admissions_create'),
    path('course_Admissions/edit/<int:id>/', course_Admissions_edit_view, name='course_Admissions_edit'),
    path('course_Admissions/delete/<int:id>/',course_Admissions_delete_view, name='course_Admissions_delete'),
    
    path('gallery/images/', gallery_image_list, name='gallery_images_list'),
    path('gallery/images/add/', gallery_image_create, name='gallery_images_create'),
    path('gallery/images/<int:pk>/edit/', gallery_image_edit, name='gallery_images_edit'),
    path('gallery/images/<int:pk>/delete/', gallery_image_delete, name='gallery_images_delete'),

    # Gallery Videos URLs
    path('gallery/videos/', gallery_video_list, name='gallery_videos_list'),
    path('gallery/videos/add/', gallery_video_create, name='gallery_videos_create'),
    path('gallery/videos/<int:pk>/edit/',gallery_video_edit, name='gallery_videos_edit'),
    path('gallery/videos/<int:pk>/delete/', gallery_video_delete, name='gallery_videos_delete'),

    path('events/', events_list, name='events_list'),
    path('events/create/', events_create, name='events_activities_create'),
    path('events/<int:id>/edit/', events_edit, name='events_activities_edit'),
    path('events/<int:id>/delete/', events_delete, name='events_activities_delete'),
    path('studentRegisterForm/',send_registration_email,name='studentregisterform'),

]+  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)