from django.urls import path,include

from tvshow_app import views

urlpatterns = [

    path('index/',views.index),
    path('email_ex/', views.email_exist),
    path('login/',views.login),
    path('login_post/',views.login_post),
    path('logout/',views.logout),
    path('forget_password/',views.forget_password),
    path('forget_password_post/',views.forget_password_post),
    path('admin_home/',views.admin_home),
    path('category/',views.category),
    path('category_post/',views.category_post),
    path('category_view/',views.category_view),
    path('category_view_search/',views.category_view_search),
    path('catagory_delete/<int:id>',views.catagory_delete),
    path('category_edit/<int:id>',views.category_edit),
    path('category_edit_post/', views.category_edit_post),
    path('tv_shows/', views.tv_shows),
    path('tv_shows_post/', views.tv_shows_post),
    path('tvshow_view/',views.tvshow_view),
    path('tvshow_view_post',views.tvshow_view_post),
    path('view_tv_shows_post/',views.view_tv_shows_post),
    path('tv_show_delete/<int:id>',views.tv_show_delete),
    path('tv_show_edit/<int:id>',views.tv_show_edit),
    path('tv_show_edit_post/',views.tv_show_edit_post),

    path('admin_change_password/', views.admin_change_password),
    path('admin_change_password_post/', views.admin_change_password_post),
    path('complaint_reply/<int:id>',views.complaint_reply),
    path('complaint_reply_post/',views.complaint_reply_post),


    path('view_user',views.view_user),
    path('view_user_post/', views.view_user_post),
    path('view_review/<int:id>',views.view_review),
    path('view_complaints/',views.view_complaints),
    path('view_complaints_search/',views.view_complaints_search),


    # user
    path('signup/',views.signup),
    path('signup_post/',views.signup_post),
    path('user_home_index/',views.user_home_index),
    path('view_tv_shows/',views.view_tv_shows),
    path('view_user_profile/',views.view_user_profile),
    path('user_change_password/',views.user_change_password),
    path('user_password_post/',views.user_password_post),

    path('sent_review/<id>',views.sent_review),
    path('sent_review_post/',views.sent_review_post),
    path('user_view_review/<id>',views.user_view_review),
    path('sent_complaint/',views.sent_complaint),
    path('sent_complaint_post/',views.sent_complaint_post),
    path('user_view_reply/',views.user_view_reply),
    path('user_view_replysearch/',views.user_view_replysearch),
    path('viewgeneratedratings/',views.viewgeneratedratings),



    ]

