from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.clock import Clock
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.properties import ObjectProperty, StringProperty
from kivymd.uix.button import MDRectangleFlatButton
from kivy.core.audio import SoundLoader
from kivymd.uix.button import MDIconButton
from kivymd.uix.label import MDIcon
from kivymd.icon_definitions import md_icons
from kivymd.uix.progressbar import MDProgressBar
import threading
import time
import sqlite3
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.label import MDLabel
from kivy.clock import Clock
from kivymd.uix.fitimage import FitImage
from kivymd.uix.card import MDCard
from kivymd.toast import toast
from kivymd.uix.behaviors import CircularRippleBehavior, CommonElevationBehavior
from kivymd.uix.tab import MDTabs,MDTabsBase
from kivy.metrics import dp

kv ='''
MDScreen:
    
    md_bg_color:"lightgreen"
    MDScrollView:
    #full test now
        MDBoxLayout:  
            md_bg_color:"white"
            size_hint_y:(None)
            height:profile_post_holder.height+postbox_forpic_others.height+postbox_text.height+comment_text_box.height
            width:self.width
            radius:[20, 20, 20, 20]
            id:post_box_fit
            orientation:"vertical"
            padding:["10sp", 0, "10sp", 0]
            MDRelativeLayout:       
                radius:[20, 20, 0, 0]
                size_hint_y:(None)
                height:post_profile_card.height
                md_bg_color:"white"
                id:profile_post_holder
                post_profile_card:post_profile_card
                MDCard:
                    #on_select:app.expand_profile_box()
                    #contains the senders id
                    id:post_profile_card
                    size_hint:(None, None)
                    height:"80sp"
                    width:"110sp"
                    pos_hint:{"left":2}
                    md_bg_color:"white"
                    radius:[20, 20, 20, 20]
                    padding:["20sp", 0, 0, 0]
                    
                    MDRelativeLayout
                        orientation:"vertical"
                        #in declarative you will have 
                        #to create an object of the 
                        #circular elevation button
                        CircularElevationButton:
                            size_hint : (None, None)
                            size : (dp(50), dp(50))
                            radius : dp(50) / 2
                            shadow_radius : dp(60) / 2
                            pos_hint:{"top":1}
                        MDLabel:
                            text:"user_name"
                            pos_hint:{"top":.78}
                            padding:["4sp"]
                        
            MDRelativeLayout:
                id:postbox_forpic_others
                size_hint_y:None
                height:post_pic_1.height
                md_bg_color:"white"
                MDCard:
                    id:post_pic_1
                    size_hint:None, None
                    
                    #when we have four
                    #height: "200sp"
                    #width:"341sp"  
                    #pos_hint:{"top":1, "left":1}
                    
                    #when we have three
                    #height: "280sp"
                    #width:"185sp"  
                    #pos_hint:{"top":1, "left":1}
                    
                    #when we have two
                    #height: "280sp"
                    #width:"240sp"  
                    #pos_hint:{"top":1, "left":1}
                    
                    #when we have one
                    height: "280sp"
                    width:"341sp"                
                    pos_hint:{"top":1}
                    FitImage:
                        source:"new2.jpg"          
                               
                #MDCard:
    #                id:post_pic_2
    #                size_hint:None, None
    #                
    #                #when we have four
    #                #height: "200sp"
    #                #width:"150sp"
    #                #pos_hint:{"bottom":1, "right":.72}
    #                
    #                #when we have three
    #                #height: "150sp"
    #                #width:"160sp"
    #                #pos_hint:{"top":1, "right":1} 
    #                
    #                #when we have two
    #                #height: "280sp"
    #                #width:"100sp"
    #                #pos_hint:{"top":1, "right":1}  
    #               
    #                pos_hint:{"top":1, "right":1}     
    #                FitImage:
    #                    source:"new1.jpg"             
                                 
                #MDCard:
    #                #remember to change d id to be unique for touch events
    #                id:post_pic_3
    #                size_hint:None, None
    #                
    #                #when we have four
    #                #height: "200sp"
    #                #width:"100sp"
    #                #pos_hint:{"bottom":1, "right":1}
    #                
    #                #when we have three
    #                #height: "140sp"
    #                #width:"160sp"
    #                #pos_hint:{"bottom":1, "right":1}
    #                
    #                pos_hint:{"bottom":1, "right":1}
    #                FitImage:
    #                    source:"new2.jpg"
                        
                #MDCard:
    #                id:post_pic_4
    #                size_hint:None, None
    #                #when we have four
    #                height: "200sp"
    #                width:"100sp"
    #                pos_hint:{"bottom":1, "left":1}
    #                FitImage:
    #                    source:"new2.jpg"
       
            MDBoxLayout:
                id:postbox_text
                md_bg_color:"blue"
                size_hint_y:None
                height:post_txt_card.height
                orientation:"vertical"
                MDCard:
                    id:post_txt_card
                    size_hint_y:None
                    height: post_txt_label.height
                    MDLabel:
                        id:post_txt_label
                        size_hint_y:None
                        height:self.height
                        text:"visit or dial Your Berekete Your Berekete has expired To buy a data plan of your choice visit or dial Your Berekete has Your Berekete has expired To buy a data plan of your choice visit or dial Your Berekete Your Berekete has expired To buy a data plan of your choice visit or dial Your Berekete has expired. To buy a data plan of your choice"
                    
                #MDLabel:
#                    id:bb_label
#                    size_hint_y:None
#                    height:self.height
#                    text:"Your Berekete has expired To buy a data plan of your choice visit or dial Your Berekete has expired. To buy a data plan of your choice visit http://hsi.glo.com or dial *312# Your Berekete has expired To buy a data plan of your choice visit or dial Your Berekete Your Berekete has expired To buy a data plan of your choice visit or dial Your Berekete has Your Berekete has expired To buy a data plan of your choice visit or dial Your Berekete Your Berekete has expired To buy a data plan of your choice visit or dial Your Berekete has expired. To buy a data plan of your choice visit http://hsi.glo.com or dial *312# expired. To buy a data plan of your choice visit http://hsi.glo.com or dial *312#. To buy a data plan of your choice visit http://hsi.glo.com or dial *312# expired. To buy a data plan of your choice visit http://hsi.glo.com or dial *312# "
                    
            MDBoxLayout:
                size_hint_y:(None)
                height:cc_label.height+reaction_box.height+comment_putcontainer.height+comment_text_container.height
                id:comment_text_box
                orientation:"vertical"
                #box for comment, like, etc
                
                MDLabel:
                    halign:"center"
                    pos_hint:{'center_x':.5, 'center_y':.1}
                    text:"comments"
                    id:cc_label
                    #pos_hint:{"top":1}
                MDBoxLayout:
                    orientation:"vertical"
                    pos_hint:{"top":.9}
                    id:comment_putcontainer
                    size_hint_y:None
                    md_bg_color:"beige"
                    height:comentview_expand_btn.height+comment_db_holder.height
                    
                    MDBoxLayout:
                        #set it to expand to view two children
                        #after which when d btn below is pressed
                        #expand fully to accomodate children
                        id:comment_db_holder
                        orientation:"vertical"
                                
                    MDRectangleFlatButton:
                        #handles on press to expand panel
                        id:comentview_expand_btn
                        halign:"center"
                        pos_hint:{"center_x":.5}
                        text:'view more'
                        md_bg_color:[1,1,1,0]
         
                MDRelativeLayout:
                    pos_hint:{"top":.8}
                    size_hint_y:None
                    height:"50sp"
                    orientation:"horizontal"
                    id:reaction_box
                    MDBoxLayout:                 
                        ##contains like and dislike
                        size_hint:(None, None)
                        height:self.height
                        width:"50sp"
                        pos_hint:{'left':1}
                        orientation:"horizontal"      
                                    
                        MDIconButton:
                            icon:"thumb-down-outline"
                            MDIcon:
                                icon:"thumb-down-outline"
                                badge_icon: "numeric-6"
                                
                        MDIconButton:
                            icon:"thumb-up-outline"
                            MDIcon:
                                icon:"thumb-up-outline"
                                badge_icon: "numeric-8"
                                
                    MDBoxLayout:
                        ##contains share and heart
                        pos_hint:{'right':.9}                  
                        size_hint:(None, None)
                        height:self.height
                        width:"50sp"
                        orientation:"horizontal"
                        MDIconButton:
                            icon:"heart-outline"
                            MDIcon:
                                icon:"heart-outline"
                                badge_icon: "numeric-10"
                                
                        MDIconButton:
                            icon:"share-outline"
                            MDIcon:
                                icon:"share-outline"
                                badge_icon: "numeric-10"     
                        
                MDBoxLayout:
                    #contains text
                    md_bg_color:"white"
                    orientation:"vertical"
                    size_hint_y:None
                    id:comment_text_container
                    height:comment_card_height.height
                    MDBoxLayout:
                        orientation:"vertical"
                        id:comment_card_height
                        size_hint:None,None
                        height:comment_box.height+comment_pic_card.height
                        width:"350sp"
                        pos_hint:{'center_x':.5, 'center_x':.5}
                        radius:["30sp", "30sp", "30sp", "30sp"]
                        MDCard:
                            id:comment_pic_card
                            size_hint:(None, None)
                            height:"12px"
                            width:"340sp"
                            md_bg_color:"lightblue"
                            pos_hint:{"top":.1, "center_x":.5}
                        
                        MDBoxLayout:
                            orientation:"vertical"
                            md_bg_color:"white"
                            size_hint:None, None
                            height:"50sp"
                            width:"340sp"
                            pos_hint:{"center_x":.5}
                            id:comment_box
                            MDScrollView:
                                MDBoxLayout:
                                    size_hint_y:None
                                    radius:["20sp", "20sp", "20sp", "20sp"]
                                    height:comment_text_field.height
                                    orientation:"horizontal"
                            
                                    MDTextField:
                                        hint_text:"add comments"
                                        
                                        id:comment_text_field
                                        size_hint:(None, None)
                                        height:self.height
                                        width:"250sp"
                                        multiline:True
                                        #halign:"center"
                                        pos_hint:{'center_x':.5, 'center_y':.5}
                                        on_text:app.set_comment()
                                    MDIconButton:
                                        icon: "send-outline"
                                        halign:"center"
                                        pos_hint:{'center_x':.6, 'center_y':.5}          
                                    MDIconButton:
                                        icon: "file"
                                        halign:"center"
                                        pos_hint:{'center_x':.2, 'center_y':.5}         
         
'''
class CircularElevationButton(
CommonElevationBehavior,
ButtonBehavior,
MDFloatLayout,):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.size = (dp(80), dp(80))
        self.radius = dp(80) / 2
        self.shadow_radius = dp(80) / 2
        
        self.profile_picture=FitImage(source="new1.jpg",
        id="profile_pic",
        pos_hint={"center_x": .5, "center_y": .5},
        radius=dp(80)/2)
        self.add_widget(self.profile_picture)
   

class AudioPlayerApp(MDApp):
    post_box_fit='ObjectProperty()'
    post_profile_card="ObjectProperty()"
    txt_id="StringProperty()"
    len_cnt="StringProperty()"
    def build(self):
        self.root = Builder.load_string(kv)
        return self.root    
    def set_comment(self):
        self.root.ids.post_box_fit.pos_hint={"y":.7}
        
    def expand_profile_box(self):
       pass
AudioPlayerApp().run()