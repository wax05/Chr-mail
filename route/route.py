import json
from datetime import timedelta
from flask import Blueprint, render_template, request, redirect, session, url_for, jsonify
from Mod.model import *

UserRoute = Blueprint("UserRoute", __name__)

@UserRoute.route("/",methods=["GET"])#MainPage
def Main():
    return render_template("Main.html")

@UserRoute.route("/login",methods=["GET", "POST"])#Login
def Login():
    return "SOON"

@UserRoute.route("/logout",methods=["GET"])#LogOut
def Logout():
    return "SOON"
    
@UserRoute.route("/signup",methods=["GET", "POST"])#Signup
def Signup():
    return "SOON"

@UserRoute.route("/report",methods=["GET", "POST"])
def ReportPage():
    return "SOON"

@UserRoute.route("/signup/email",methods=["GET", "POST"])#EmailAuth
def EmailAuth():
    return "SOON"

@UserRoute.route("/letter",methods=["GET", "POST"])#LetterMainPage
def LetterMain():
    return "SOON"

@UserRoute.route("/letter/help",methods=["GET", "POST"])#Letter Help Docs
def LetterHelp():
    return "SOON"

@UserRoute.route("/letter/<str:UserID>",methods=["GET", "POST"])#UserLetter Page
def UserLetter():
    return "SOON"

@UserRoute.route("/letter/view",methods=["GET","POST"])#Only Admin Letter View Page
def LetterView():
    return "SOON"

@UserRoute.route("/admin",methods=["GET", "POST"])
def AdminPage():
    return "SOON"

@UserRoute.route("/admin/user",methods=["GET", "POST"])
def AdminUserControl():
    return "SOON"

@UserRoute.route("/report",methods=["GET","POST"])
def ViewReport():
    return "SOON"
