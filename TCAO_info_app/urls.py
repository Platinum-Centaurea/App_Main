from django.contrib import admin
from django.urls import path, include
from . import views, chat

app_name = 'AntenaMuroran'
urlpatterns = [
    # 起動画面
    path('', views.main, name='main'), 
    # ログイン画面
    path('login', views.login, name='login'), 
    # ログアウト処理
    path('logout', views.logout, name='logout'), 
    # マイページ画面（ログイン中のみ遷移）
    path('mypage', views.mypage, name='mypage'), 
    # 新規登録画面
    path('adduser', views.addUser, name='addUser'), 
    # 新規登録結果画面
    path('adduserresult', views.addUserResult, name='addUserResult'), 
    # マップ画面
    path('map', views.map, name='map'), 
    # 店・イベント・観光情報画面
    path('contents', views.contents, name='contents'), 
    # 店・イベント登録画面
    path('addcontent', views.addContent, name='addContent'), 
    # 店・イベント登録結果
    path('addcontent/result', views.addContentResult, name='addContentResult'), 
    # 質問箱画面
    path('qboxes', views.QBoxes, name='QBoxes'), 
    # 質問箱画面
    path('qboxes/<int:id>', views.QBoxes, name='QBoxes'), 
    # 質問箱追加
    path('qboxAdd', views.QBoxAdd, name='QBoxAdd'), 
    # 求人画面
    path('recuruits', views.recruits, name='recruits'), 
    # 求人追加画面
    path('addRecuruit', views.addRecruit, name='addRecruit'), 
    # 求人追加結果
    path('addRecuruitResult', views.addRecruitResult, name='addRecruitResult'), 
    
    # それぞれの個別情報画面は後に作る
    path('indiv/recruit/<int:status>:<int:id>', views.indiv, name='indivRecruit'), 
    path('indiv/event/<int:status>:<int:id>', views.indiv, name='indivEvent'), 
    path('indiv/store/<int:status>:<int:id>', views.indiv, name='indivStore'), 
    
    path('kobetu', views.kobetu, name='kobetu'), 
    
    
    # チャット処理１：全メッセージの取得     
    path('getChatMessage/<int:id>', chat.getChatMessage, name='getChatMessage'),     
    # チャット処理２：新規メッセージの投稿     
    path('submitChatMessage/<int:id>', chat.submitChatMessage, name='submitChatMessage'),     
    # チャット処理３：指定メッセージの削除    
    path('deleteChatMessage/<int:id>', chat.deleteChatMessage, name='deleteChatMessage'),
]
