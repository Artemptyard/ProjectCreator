import shutil
import os


templates = 'data/templates/'


def QtCreater(fPath, Data, Design, Img, Files, AppD, Db):
    newPath = fPath + '/mainQt.py'
    shutil.copyfile(templates + 'mainQt.py', newPath)
    os.rename(newPath, fPath + '/main.py')
    shutil.copyfile(templates + 'testing.py', fPath + '/testing.py')
    if Data:
        os.mkdir(fPath + '/data')
        if Design:
            os.mkdir(fPath + '/design')
        if Img:
            os.mkdir(fPath + '/img')
        if Files:
            os.mkdir(fPath + '/files')
        if AppD:
            newPath = fPath + '/appdata'
            os.mkdir(newPath)
            shutil.copyfile(templates + 'function.py', newPath + '/function.py')
            shutil.copyfile(templates + 'classes.py', newPath + '/classes.py')
        if Db:
            os.mkdir(fPath + '/databases')


def cmdCreater(fPath, Data, Img, Files, AppD, Db):
    newPath = fPath + '/mainCMD.py'
    shutil.copyfile(templates + 'mainCMD.py', newPath)
    os.rename(newPath, fPath + '/main.py')
    shutil.copyfile(templates + 'testing.py', fPath + '/testing.py')
    if Data:
        os.mkdir(fPath + '/data')
        if Img:
            os.mkdir(fPath + '/img')
        if Files:
            os.mkdir(fPath + '/files')
        if AppD:
            newPath = fPath + '/appdata'
            os.mkdir(newPath)
            shutil.copyfile(templates + 'function.py', newPath + '/function.py')
            shutil.copyfile(templates + 'classes.py', newPath + '/classes.py')
        if Db:
            os.mkdir(fPath + '/databases')


def WebCreater(fPath, Temp, Static, Img, Css, AppD, Files, Db):
    newPath = fPath + '/mainWeb.py'
    shutil.copyfile(templates + 'mainWeb.py', newPath)
    os.rename(newPath, fPath + '/main.py')
    shutil.copyfile(templates + 'testing.py', fPath + '/testing.py')
    if Temp:
        os.mkdir(fPath + '/templates')
        shutil.copyfile(templates + 'base.html', fPath + '/templates/base.html')
    if Static:
        os.mkdir(fPath + '/data')
        if Img:
            os.mkdir(fPath + '/img')
        if Css:
            os.mkdir(fPath + '/css')
            shutil.copyfile(templates + 'css.css', fPath + '/css/css.css')
        if AppD:
            newPath = fPath + '/appdata'
            os.mkdir(newPath)
            shutil.copyfile(templates + 'function.py', newPath + '/function.py')
            shutil.copyfile(templates + 'classes.py', newPath + '/classes.py')
        if Files:
            os.mkdir(fPath + '/files')
        if Db:
            os.mkdir(fPath + '/databases')